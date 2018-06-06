from bs4 import BeautifulSoup as bs
import  urllib.request as req

#htmlの取得
url = "http://api.aoikujira.com/kawase/xml/usd"
res = req.urlopen(url)

#HTML解析
soup = bs(res, "html.parser")

#任意データの抽出
price = soup.select_one("jpy").string
print("usd/jpy = ",price)