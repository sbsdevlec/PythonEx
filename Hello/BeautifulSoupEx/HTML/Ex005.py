import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "http://astro.kasi.re.kr/Life/Knowledge/solar2lunar/convert_monthly.php"
    # year = input("년도")
    year = '2017'
    query = "?sol_year="+year
    # month = input("년도")
    month='4'
    query += "&sol_month="+month

    req = urllib.request.Request(url  + query);
    data = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')

    l = bs.find_all('tr')
    print(type(l))
    for tr in l:
        td = tr.find_all('td')
        for t in td:
            print(t.string.strip())
