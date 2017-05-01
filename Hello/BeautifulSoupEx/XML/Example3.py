import xml.etree.ElementTree as et

doc = et.parse('test.xml')

# get root node
root = doc.getroot()
# dump 함수는 인자로 넘어온 tag 이하를 print 해준다
et.dump(root)
print("*"*100)
"""
태그 삭제
랭크가 50보다 큰 국가를 삭제해 보자.
"""
# 모든 country에 대해...
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    # rank가 50보다 크면
    if rank > 50:
        # 해당 태그를 삭제한다
        root.remove(country)
et.dump(root)