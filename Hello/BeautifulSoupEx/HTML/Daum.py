import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "http://www.daum.net"
    req = urllib.request.Request(url);
    data = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(data, 'html.parser')
    # BeautifulSoup 생성자에서 html_doc를 파싱하고
    # 그 결과를 BeautifulSoup 객체로 반환한다.
    # print(bs.prettify())
    divs = bs.find_all("div",{"class":"rank_cont"})
    print(type(divs))
    print(len(divs))
    print(divs[0])
    print("_"*90)
    sw=1
    for div in divs:
        if sw==1:
            spans = div.find_all('span',{'class':'ir_wa'})
            result = div.find('em')
            a_title = div.find('a')['title']
            a_href = div.find('a')['href']
            print(spans[0].string,a_title, a_href,result.text)
        sw *= -1