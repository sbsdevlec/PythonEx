html_doc = """ 
<!doctype html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <meta name="Generator" content="EditPlus®">
  <title>Document</title>
 </head>
 <body>
  <h1>제목1</h1>
	<p class="story1">내용1</p>
	<p>내용2</p>
	<p class="story2">내용3</p>
	<p>내용4</p>
  <h1>제목2</h1>
    <a class="sister" href="http://example.com/elsie" id="link1">링크1</a>
    <a class="sister" href="http://example.com/elsie" id="link2">링크2</a>
    <a class="sister" href="http://example.com/elsie" id="link3">링크3</a>
    <a class="sister" href="http://example.com/elsie" id="link4">링크4</a>
    <a class="sister" href="http://example.com/elsie" id="link5">링크5</a>
 </body>
</html>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
# BeautifulSoup 생성자에서 html_doc를 파싱하고
# 그 결과를 BeautifulSoup 객체로 반환한다.

# 모든 내용 출력
# print(soup.prettify())

# soup 객체의 데이터 탐색 
print(soup.title) # title 태그
# <title>Document</title>
print(soup.title.name) # 태그명
#  title
print(soup.title.string) # 태그 내용
#  Document
print(soup.title.parent.name) # 위의 태그
# meta

print(soup.p)
# <p class="story1">내용1</p>
print(soup.p['class'])
# ['story1']

print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">링크1</a>
print(soup.find_all('a'))
"""
[
<a class="sister" href="http://example.com/elsie" id="link1">링크1</a>, 
<a class="sister" href="http://example.com/elsie" id="link2">링크2</a>, 
<a class="sister" href="http://example.com/elsie" id="link3">링크3</a>, 
<a class="sister" href="http://example.com/elsie" id="link4">링크4</a>, 
<a class="sister" href="http://example.com/elsie" id="link5">링크5</a>
]
"""
print(soup.find(id="link3"))
# <a class="sister" href="http://example.com/elsie" id="link3">링크3</a>

for link in soup.find_all('a'):
    print(link.get('href'))
"""
http://example.com/elsie
http://example.com/elsie
http://example.com/elsie
http://example.com/elsie
http://example.com/elsie
"""

print(soup.get_text())
"""






Document


제목1
내용1
내용2
내용3
내용4
제목2
링크1
링크2
링크3
링크4
링크5




"""
