import xml.etree.ElementTree as et
import datetime

doc = et.parse('test.xml')
"""
파일로 쓰기
지금까지 변경시킨 내용을 이제 파일에 써보도록 하자.
"""
# get root node
root = doc.getroot()
# dump 함수는 인자로 넘어온 tag 이하를 print 해준다
et.dump(root)
print("*"*100)

# 첫번째 인자는 출력할 파일명
# encoding : 출력할 xml 파일의 인코딩 지정
# xml_declaration : True
# encoding 지정이 있고 xml_declaration이 True여야만
# xml 선언 헤더인 <?xml version='1.0' encoding='utf-8'?>이 파일에 써진다
doc.write("output.xml", encoding="utf-8", xml_declaration=True)

