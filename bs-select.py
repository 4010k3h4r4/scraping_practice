from bs4 import BeautifulSoup as bs

#解析対象HTML
html = """
<html><body>
    <div id = "meigen">
        <h1>トルストイの名言</h1>
        <ul class = "items">
            <li>汝の心におしえよ、心に学ぶな。</li>
            <li>謙虚な人は誰からも好かれる。</li>
            <li>強い人々は気取らない。</li>
        </ul>
    </div>
</body></html>
"""

#html解析
soup = bs(html,'html.parser')

#必要な部分をCSSクエリで書き出す
#タイトルの取得
h1 = soup.select_one("div#meigen > h1").string
print("h1 = ",h1)

#リストの取得
li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
    print("li = ",li.string)
