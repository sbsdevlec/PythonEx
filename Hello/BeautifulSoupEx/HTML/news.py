import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "http://rss.ohmynews.com/rss/top.xml"
    req = urllib.request.Request(url);
    data = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(data, 'html.parser')
    # BeautifulSoup 생성자에서 html_doc를 파싱하고
    # 그 결과를 BeautifulSoup 객체로 반환한다.
    # print(bs.prettify())
    channel = bs.find('title')
    link = bs.find('link')
    copyright = bs.find('copyright')
    print(channel.string, link.string, copyright.string)

    items = bs.find_all("item")
    print(len(items))
    for item in items:
        title = item.find('title')
        link = item.find('link')
        print(title.text,"[",link,"]")