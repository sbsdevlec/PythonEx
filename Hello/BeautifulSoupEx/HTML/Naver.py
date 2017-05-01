import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "http://www.naver.com"
    req = urllib.request.Request(url);
    data = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(data, 'html.parser')
    # BeautifulSoup 생성자에서 html_doc를 파싱하고
    # 그 결과를 BeautifulSoup 객체로 반환한다.
    # print(bs.prettify())
    lis = bs.find_all("li",{"class":"ah_item"})
    #print(type(lis))
    #print(len(lis))
    #print(lis[0])
    #print("_"*90)
    for li in lis:
        a = li.select("a")
        if len(a)==2:
            span = li.select('span')
            print(span[0].string, span[1].string)
            a_href = li.find('a')['href']
            print(a_href)