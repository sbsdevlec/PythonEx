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
    print(trs[0].__dict__)
    print(trs[0].contents)
    for t in trs[0].contents:
        if t != '\n':
            print('['+t.text+']')
    #print(trs[0].contents[1])
    """
    for tr in trs:
        #print(vars(tr))
        print(tr.contents[1].text.strip())
        print(tr.contents[3].text.strip())
        print(tr.contents[5].text.strip())
        print("*"*80)