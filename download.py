import asyncio
import aiohttp
import aiofile
from argparse import ArgumentParser, Namespace
from pathlib import Path

DATASET_DIR = './data'


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        '-s', '--source',
        dest='source',
        default=DATASET_DIR + '/sources.txt',
        help='Path to the source file containing list of URLs to download'
    )
    parser.add_argument(
        '-d', '--dataset-dir',
        dest='dataset_dir',
        default=DATASET_DIR,
        help='Directory where the dataset will be downloaded'
    )
    parser.add_argument(
        '-m', '--max-connections',
        dest='max_connections',
        type=int,
        default=8,
        help='Maximum number of concurrent download connections'
    )
    parser.add_argument(
        '-R', '--replace',
        dest='replace',
        action='store_true',
        help='Replace existing files if they already exist'
    )
    return parser.parse_args()


def extract_image_urls(source_path: Path) -> list[str]:
    with open(source_path) as f:
        urls = [
            url.strip()
            for url in f.read().splitlines()
        ]
    urls = [url for url in urls if len(url) > 0]
    return urls


def download_images(
        image_urls: list[str],
        dataset_dir: Path,
        *,
        replace: bool = False,
        max_connections: int = 8
        ):
    semaphore = asyncio.BoundedSemaphore(max_connections)

    async def download_file(session, url):
        file_path = dataset_dir / url.split("/")[-1]
        if not replace and file_path.exists():
            return

        async with semaphore:
            async with session.get(url) as resp:
                assert resp.status == 200
                data = await resp.read()

        async with aiofile.async_open(file_path, 'wb') as f:
            await f.write(data)

    async def bulk_download_files():
        async with aiohttp.ClientSession() as session:
            tasks = [download_file(session, url) for url in image_urls]
            await asyncio.gather(*tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(bulk_download_files())
    loop.close()


if __name__ == "__main__":
    args = parse_args()
    source_path = Path(args.source)
    dataset_dir = Path(args.dataset_dir)

    image_urls = extract_image_urls(source_path)
    download_images(
        image_urls,
        dataset_dir,
        replace=args.replace,
        max_connections=args.max_connections
    )
