import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse


def download_image(url, save_dir="images"):
    """下载单个图片并保存到指定目录"""
    try:
        # 提取文件名（处理 URL 中的查询参数和路径）
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or f"image_{hash(url)}.jpg"
        filepath = os.path.join(save_dir, filename)

        # 检查文件是否已存在
        if os.path.exists(filepath):
            return "skipped", url, "File already exists"

        # 下载文件
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查 HTTP 错误

        # 保存文件
        with open(filepath, "wb") as f:
            f.write(response.content)

        return "success", url, None
    except Exception as e:
        return "failed", url, str(e)


def main():
    # 读取 URL 列表文件
    with open("list_of_all_urls.csv", "r") as file:
        urls = [url.strip() for url in file.readlines() if url.strip()]

    # 创建图片保存目录
    os.makedirs("images", exist_ok=True)

    # 多线程下载（默认使用 8 个线程）
    success_count = 0
    skipped_count = 0
    failed_downloads = []

    with ThreadPoolExecutor(max_workers=8) as executor:
        # 提交所有下载任务
        future_to_url = {
            executor.submit(download_image, url): url
            for url in urls
        }

        # 处理完成的任务
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                status, url, error = future.result()
                if status == "success":
                    success_count += 1
                elif status == "skipped":
                    skipped_count += 1
                else:
                    failed_downloads.append((url, error))
            except Exception as e:
                failed_downloads.append((url, str(e)))

            # 实时显示进度
            processed = success_count + skipped_count + len(failed_downloads)
            print(
                f"\rProgress: {processed / len(urls) * 100:.1f}% "
                f"({processed}/{len(urls)}) "
                f"- OK: {success_count} | Skipped: {skipped_count} | Failed: {len(failed_downloads)}",
                end=""
            )

    # 打印结果
    print("\n\nDownload complete!")
    if failed_downloads:
        print("\nFailed downloads:")
        for url, error in failed_downloads:
            print(f"- {url} ({error})")


if __name__ == '__main__':
    main()
