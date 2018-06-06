from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 id = "title">スクレイピングとは</h1>
    <p id = "body">Webページから任意のデータを抽出すること</p>
</body></html>
"""

#htmlの解析
soup = BeautifulSoup(html, 'html.parser')

#findメソッドで取り出し
title = soup.find(id = "title")
body = soup.find(id = "body")

#テキスト部分の表示
print("#title = ", title.string)
print("#body = ", body.string)