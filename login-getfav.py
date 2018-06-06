import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

#user and password
USER = "JS-TESTER"
PASS = "ipCU12ySxI"

#start session
session = requests.session()

#login
login_info = {
    "username_mmlbbs6":USER,
    "password_mmlbbs6":PASS,
    "back":"index.php",
    "mml_id":"O"
}

url_login = "https://uta.pw/sakusibbs/users.php?action=login&m=try"
res = session.post(url_login, data=login_info)
res.raise_for_status()

soup = bs(res.text, "html.parser")
a = soup.select_one(".islogin a")
if a is None:
    print("マイページが取得できませんでした")
    quit()
#URLの変換
url_mypage = urljoin(url_login, a.attrs["href"])
print("マイページ = ", url_mypage)

#マイページへのアクセス
res = session.get(url_mypage)
res.raise_for_status()

#お気に入りの詞のタイトル
soup = bs(res.text, "html.parser")
print(res.text)
links = soup.select("#favlist li > a")
for a in links:
    href = a.attrs["href"]
    title = a.get_text()
    print("-", title, ">", href)