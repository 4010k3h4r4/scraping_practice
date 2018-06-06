#!/usr/bin/env python3

#ライブラリの取り込み
import sys
import urllib.request as req
import urllib.parse as parse

#コマンドライン引数の取得
if len(sys.argv) <= 1:
    print("USAGE : hyakunin-issyu.py (keyword)")
    sys.exit()
keyword = sys.argv[1]

#パラメータのエンコード
api = "http://api.aoikujira.com/hyakunin/get.php"
query = {
    "fmt":"ini",
    "key":keyword
}
params = parse.urlencode(query)
url = api + "?" + params
print("URL = ", url)

#ダウンロード
with req.urlopen(url) as r:
    b = r.read()
    data = b.decode("utf-8")
    print(data)