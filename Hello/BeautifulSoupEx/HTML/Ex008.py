import urllib.request
from bs4 import BeautifulSoup
class Calendar:
    pass

if __name__ == "__main__":
    url = "http://astro.kasi.re.kr/Life/Knowledge/solar2lunar/convert_monthly.php"
    query = "?sol_year=2017"
    query += "&sol_month=4"

    req = urllib.request.Request(url  + query);
    data = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(data, 'html.parser')

    trs = bs.find_all('tr')
    calendar_list=[]
    for tr in trs:
        tds = tr.select('td')
        list = []
        for td in tds:
            list.append(td.text.strip())
            #print(td.text.strip())
        if len(list)>0:
            print(list)
            c = Calendar()
            c.s = list[0]
            c.l = list[1]
            c.g = list[2]
            calendar_list.append(c)
print(len(calendar_list))
for c in calendar_list:
    print(c.s, c.l, c.g)
    print("_"*80)