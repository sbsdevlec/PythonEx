from urllib.request import Request, urlopen
from urllib.parse import urlencode
import copy
import re

URL = "http://astro.kasi.re.kr/Life/Knowledge/solar2lunar/convert_monthly.php"

DATA = {"sol_year": None, "sol_month": None}

headers = {"Content-Type": "application/x-www-form-urlencoded","Accept":"text/html"}

data = copy.copy(DATA)
data["sol_year"] = 2015
data["sol_month"] = 1

req = Request(URL, method="POST",
data=urlencode(data).encode('utf-8'))
res = urlopen(req)
a = res.read().decode('cp949')
print(a)

