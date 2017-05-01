import json

# 테스트용 Python Dictionary
customer = {
    'id': 1,
    'name': 'kimc',
    'history': [
        {'date': '2015-03-11', 'item': 'ios'},
        {'date': '2016-02-23', 'item': 'window'},
        {'date': '2017-02-23', 'item': 'android'}
    ]
}

print(customer)
print(type(customer))
print("-"*50)

'''
# JSON 인코딩
Python Object (Dictionary, List, Tuple 등) 를 JSON 문자열로 변경하는 것을 JSON Encoding 이라 부른다. 
JSON 인코딩을 위해서는 우선 json 라이브러리를 import 한 후, json.dumps() 메서드를 써서 Python Object를 문자열로 변환하면 된다.
'''
jsonString = json.dumps(customer)

# 문자열 출력
print(jsonString)
print(type(jsonString))  # class str
print("-"*50)
'''
JSON 문자열을 읽기 편하게 할 필요가 있을 경우에는, 아래와 같이 "indent" 옵션을 json.dumps() 메서드 안에 지정하면 된다.
'''
jsonString = json.dumps(customer, indent=4)
print(jsonString)
print(type(jsonString))  # class str
print("-"*50)

"""
JSON 디코딩

JSON 문자열을 Python 타입 (Dictionary, List, Tuple 등) 으로 변경하는 것을 JSON Decoding 이라 부른다. 
JSON 디코딩은 json.loads() 메서드를 사용하여 문자열을 Python 타입으로 변경하게 된다.
"""
jsonString = '{"id": 1, "name": "kimc", "history": [{"date": "2015-03-11", "item": "ios"}, {"date": "2016-02-23", "item": "window"}, {"date": "2017-02-23", "item": "android"}]}'

# JSON 디코딩
dict = json.loads(jsonString)

# Dictionary 데이타 체크
print(dict['id'], dict['name'])
for h in dict['history']:
    print(h['date'], h['item'])
print("-" * 50)

"""
파일에서 읽기
"""
json_data=open("json.json").read() # UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 30: illegal multibyte sequence
data = json.loads(json_data)
print(data)
print(type(data))
print(data['id'], data['name'])
for h in data['history']:
    print(h['date'], h['item'])
print("-" * 50)