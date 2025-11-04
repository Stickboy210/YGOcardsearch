#!/usr/bin/env python3
import requests, zipfile, io, json, sys, os

URL = "https://ygocdb.com/api/v0/cards.zip"
LOCAL = "cards.json"

def main():
    print("↓ 下载压缩包 ...")
    r = requests.get(URL, timeout=30)
    r.raise_for_status()

    print("↓ 解压 ...")
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        with z.open("cards.json") as f:
            data = json.load(f)

    print("↓ 写入本地 cards.json ...")
    with open(LOCAL, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("√ 完成！文件大小：{:.2f} MB".format(os.path.getsize(LOCAL)/1024/1024))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("✗ 失败：", e)
        sys.exit(1)
