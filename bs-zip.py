from bs4 import BeautifulSoup as bs
import  urllib.request as req

url = "http://api.aoikujira.com/zip/xml/1540004"

#urlopen()でデータの取得
res = req.urlopen(url)

#Beutifulsoupで解析
soup = bs(res,"html.parser")

#任意のデータ抽出
pref = soup.find("ken")
city = soup.find("shi")
town = soup.find("cho")
print(pref,city,town)