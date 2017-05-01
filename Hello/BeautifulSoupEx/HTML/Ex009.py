import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "http://astro.kasi.re.kr/Life/Knowledge/solar2lunar/convert_monthly.php"
    query = "?sol_year=2017"
    query += "&sol_month=4"

    req = urllib.request.Request(url  + query);
    data = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(data, 'html.parser')

    trs = bs.find_all('tr')
    print(type(trs))
    """
    # print(dir(trs))
    #print(trs[0].__dict__)
    print(trs[0].contents)
    for s in trs[0].contents:
        if s!='\n':  print(type(s), s, s.string)
    """
    """
    tds = trs[1].select('td')
    print(type(tds))
    print(tds[0].string.strip())
    print(tds[1].string.strip())
    print(tds[2].string.strip())
    """
    for tr in trs:
        tds = trs[1].select('td')
        if len(tds)>0:
            print(tds[0].string.strip())
            print(tds[1].string.strip())
            print(tds[2].string.strip())
        print("_"*60)