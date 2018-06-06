from selenium import webdriver

#user and password
USER = "JS-TESTER"
PASS = "ipCU12ySxI"

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

url_login = "https://uta.pw/sakusibbs/users.php?action=login&m=try"

browser.get(url_login)
print("ログインページにアクセスしました。")

e = browser.find_element_by_id("user")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pass")
e.clear()
e.send_keys(PASS)

frm = browser.find_element_by_css_selector("#loginForm form")
frm.submit()
print("ログイン情報を入力してログインボタンを押しました")

a = browser.find_element_by_css_selector(".islogin a")
url_mypage = a.get_attribute("href")
print("マイページのURL = ", url_mypage)

browser.get(url_mypage)
print("マイページにアクセスしました")

links = browser.find_elements_by_css_selector("#favlist li > a")
print("リンクの一覧を取得しました")

for link in links:
    href =  link.get_attribute("href")
    title =  link.text
    print("-",title,">",href)