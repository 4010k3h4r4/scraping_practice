from bs4 import BeautifulSoup as bs

html = """
<ul id = "bible">
    <li id = "ge">Genesis</li>
    <li id = "ex">Exodus</li>
    <li id = "le">Leviticus</li>
    <li id = "nu">Numbers</li>
    <li id = "de">Deutronomy</li>
</ul>
"""

soup = bs(html,"html.parser")

sel = lambda q : print(soup.select_one(q).string)

sel("#nu")
sel("li#nu")
sel("ul > li#nu")
sel("ul li#nu")
sel("#bible > #nu")
sel("li[id='nu']")
sel("li:nth-of-type(4)")
