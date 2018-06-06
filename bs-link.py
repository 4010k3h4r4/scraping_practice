from bs4 import BeautifulSoup as bs

html = """
<html><body>
    <ul>
        <li><a href = "http://uta.pw">uta</a></li>
        <li><a href = "http://oto.chu.jp">oto</a></li>
    </ul>
</body></html>
"""

#html解析
soup = bs(html,'html.parser')

#find_allメソッドの利用
links = soup.find_all("a")

#リンク一覧の取得
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text," > ",href)