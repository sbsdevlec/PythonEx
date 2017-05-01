import json
import codecs
json_data = codecs.open("data.json","r","utf-8").read() # UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 30: illegal multibyte sequence
data = json.loads(json_data)
print(data)
print(type(data))

for d in data:
    print(d['h'], d['k'], d["t"])
print("-" * 50)



