from bs4 import BeautifulSoup
import requests


if __name__ == "__main__":
    url = "http://astro.kasi.re.kr/Life/Knowledge/solar2lunar/convert_monthly.php"
    # year = input("년도")
    year = '2017'
    query = "?sol_year="+year
    # month = input("년도")
    month='4'
    query += "&sol_month="+month

    html = requests.get(url+query)
    print(html.encoding)
    html.encoding = 'euc-kr'
    print(html.encoding)
    print(html.cookies)
    print(html.url)
    print(html.status_code)
    print(html.history)
    print(html.headers)
    print(html.content)
    print(html.text)