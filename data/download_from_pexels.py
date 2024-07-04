import os

import requests


def main():
    with open(r"list_of_all_urls.csv", "r") as file:
        urls = file.readlines()

    os.makedirs("images", exist_ok=True)
    for idx, url in enumerate(urls):
        filename = url.strip().split('/')[-1]
        r = requests.get(url, allow_redirects=True)
        open(f"images/{filename}", 'wb').write(r.content)
        print(f"\r{100 * idx / len(urls):7.3f}% Complete", end="")


if __name__ == '__main__':
    main()