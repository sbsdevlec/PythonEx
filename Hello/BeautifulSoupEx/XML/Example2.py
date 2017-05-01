import xml.etree.ElementTree as et

doc = et.parse('test.xml')

# get root node
root = doc.getroot()
# dump 함수는 인자로 넘어온 tag 이하를 print 해준다
et.dump(root)
print("*"*100)
"""
태그 변경

모든 국가의 랭크를 1단계를 낮춰보도록 하자.
그리고, rank 태그에 "updated"라는 attribute를 추가해 보자.
"""
# root 이하 모든 rank 태그에 대해...
for rank in root.iter("rank"):
    # 기존의 rank값을 정수형으로 변환한 뒤 1 더해서 변수에 대입하고
    new_rank = int(rank.text) + 1
    # 이를 rank 태그의 text로 갱신
    rank.text = str(new_rank)
    # 그리고, rank 태그에 {"updated":"yes"} attribute를 추가한다
    rank.attrib["updated"] = "yes"
    # 위 attribute 추가는 아래과 같이 할 수도 있다.
    # rank.set("updated", "yes")

# dump 함수는 인자로 넘어온 tag 이하를 print 해준다
et.dump(root)