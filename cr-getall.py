from bs4 import BeautifulSoup as bs
from urllib import request
from urllib import parse
from os import makedirs
import os.path, time, re

#処理済み判断変数
proc_files = {}

#HTML内のリンク抽出
def enum_links(html, base):
    soup = bs(html, "html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    result = []
    #hrefを取り出してリンクを絶対パスに変換
    for a in links:
        href = a.attrs['href']
        url = request.urljoin(base, href)
        result.append(url)
    return result

def download_file(url):
    o = parse.urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath):
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    if os.path.exists(savepath): return savepath
    if not os.path.exists(savedir):
        print("mkdir = ", savedir)
        makedirs(savedir)
    try:
        print("download = ", url)
        request.urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print("ダウンロード失敗 : ", url)
        return None

def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return
    proc_files[savepath] = True
    print("analyze_html = ", url)
    #リンクを抽出
    html = open(savepath, "r", encoding = 'utf-8').read()
    links = enum_links(html, url)
    for link_url in links:
        if link_url.find(root_url) != 0:
            if not re.search(r".css$",link_url): continue
        if re.search(r".(html|htm)$", link_url):
            analyze_html(link_url, root_url)
            continue
        download_file(link_url)

if __name__ == "__main__":
    url = "http://docs.python.jp/3.6/library/"
    analyze_html(url, url)