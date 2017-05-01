html_doc = """ 
<!doctype html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <meta name="Generator" content="EditPlus®">
  <meta name="Author" content="">
  <meta name="Keywords" content="">
  <meta name="Description" content="">
  <title>Document</title>
 </head>
 <body>
  <h1>제목</h1>
	<p>내용</p>
 </body>
</html>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
# BeautifulSoup 생성자에서 html_doc를 파싱하고
# 그 결과를 BeautifulSoup 객체로 반환한다.
print(soup.prettify())

