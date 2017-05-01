import json
jsonString = '{"name": "한사람", "history": [{"date": "2016-04-22", "item": "ios"}, {"date": "2016-07-31", "item": "window"}]}'
# JSON 디코딩
dict1 = json.loads(jsonString)
print(dict1)
print(type(dict1))
print(dict1['name'])
print("*"*80)

jsonString1 = json.dumps(jsonString)
print(jsonString1)
print(type(jsonString1))
print("*"*80)

jsonString2 = json.dumps(jsonString, ensure_ascii=False)
print(jsonString2)
print(type(jsonString2))
print("*"*80)

import codecs
json_data = codecs.open("json2.json","r","utf-8").read() # UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 30: illegal multibyte sequence
data = json.loads(json_data)
print(data)
print(type(data))
print(data['id'], data['name'])
for h in data['history']:
    print(h['date'], h['item'])
print("-" * 50)



