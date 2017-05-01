import xml.etree.ElementTree as et
import datetime

doc = et.parse('test.xml')

# get root node
root = doc.getroot()
# dump 함수는 인자로 넘어온 tag 이하를 print 해준다
et.dump(root)
print("*"*100)
"""
태그 추가
모든 국가에 last_updated 라는 태그를 추가해보자.
"""
# 방법 1 : ElementTree.Element + append
# 모든 county에 대해...
for country in root.iter('country'):
    e = datetime.datetime.now()
    # last_updated 엘리먼트를 만들고
    last_updated = et.Element("last_updated1")
    # last_updated의 text를 지정한다
    last_updated.text = str(e)
    # 그리고 last_updated 엘리먼트를 country 태그에 child로 추가한다
    country.append(last_updated)
et.dump(root)
print("*"*100)

# 방법 2 : ElementTree.SubElement
for country in root.findall('country'):
    e = datetime.datetime.now()
    # country의 서브 엘리먼트 last_updated를 만들고
    last_updated = et.SubElement(country, "last_updated2")
    # text를 지정한다
    last_updated.text = str(e)
et.dump(root)