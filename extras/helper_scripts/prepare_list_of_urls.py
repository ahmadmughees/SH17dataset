
import json
import os

PATH = r"C:\Users\ahmad\repos\pylabel\SH17\SH17\meta-data"
paths = os.listdir(PATH)
URLS = []
for path in paths:
    if not path.endswith(".json"): continue
    print(path)
    with open(f"{PATH}/{path}", 'r') as json_file:
        data = json.load(json_file)
    URLS.append(data.get("src")["original"])

print(len(URLS), "urls found")
with open("../../data/list_of_all_urls.csv", 'w') as f:
    for url in URLS:
        f.write(f"{url}\n")

print("DONE!!!")