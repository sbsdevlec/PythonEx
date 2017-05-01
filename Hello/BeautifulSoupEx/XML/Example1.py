import xml.etree.ElementTree as et

doc = et.parse('test.xml')

# get root node
root = doc.getroot()
print(root)
print(type(root))
print(dir(root))
print()
"""
다음 과정을 설명하기에 앞서 ElementTree는 xml 태그의 구성을 다음과 같이 표현함을 알아두도록 하자.
tag : 해당 태그의 이름
text : 해당 태그의 값(?) 이걸 뭐라고 해야 하나?
attrib : 해당 노드의 attribute 맵 (key, value)
예를 들어, 리히텐슈타인의 year 태그의 tag는 "year", text는 "2008"이 된다.

그리고, 리히텐슈타인의 neighbor 태그는 다음의 attrib 맵을 가지고 있다.
neighbor { "name" : "Austria",       "Direction" : "E" }
neighbor { "name" : "Switzerland", "Direction" : "W" }
"""
country_tag = root.find("country")
print(country_tag)
print(country_tag.attrib)
print()

year = country_tag.find('year')
print(year)
print(year.text)
print()

# root 하위에 "country"와 일치하는 모든 태그를 리스트로 리턴한다.
country_tags = root.findall("country")
for country_tag in country_tags:
    print(country_tag.attrib)
print()


# root 태그에서도 iter("year")만 모두 순회가 가능하다
for y in root.iter("year"):
    print(y.text)
print()

# root 태그에서도 iter("neighbor")만 모두 순회가 가능하다
for neighbor in root.iter("neighbor"):
    print(neighbor.attrib)
print()

# root 이하 모든 자식의 태그명을 프린트한다.
for child in root.iter():
    print(child.tag)
print()

# root 이하 country 태그들에 대해 태드명을 프린트한다
for country in root.iter("country"):
    print(country.tag)

# 모든 country에 대해
for country in root.iter("country"):
    print("=" * 60)
    # country의 name attribute 출력
    print("Country : ", country.attrib["name"])
    # country의 child "rank" 출력
    print("Rank : ", country.findtext("rank"))
    # country의 child "year" 출력
    print("Year : ", country.findtext("year"))
    # country의 모든 child "neighbor" 출력
    for neighbor in country.iter("neighbor"):
        # neighbor의 attribute map 출력
        print("Neighbor : ", neighbor.attrib)