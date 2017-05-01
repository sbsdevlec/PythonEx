import urllib.request
web = urllib.request.urlopen('http://www.python.org')
print(web.headers)                                    # 리턴된 헤더 출력
print(web.read())                                     # 실제로 가져온 html 파일 출력

