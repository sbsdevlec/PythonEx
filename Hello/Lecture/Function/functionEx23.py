# 딕셔너리를 넘기고 받을때는 **를 사용합니다.
def makeQuery(url, **queryString):
    print(type(queryString))
    url += "?"
    for k,v in queryString.items():
        url += k + "=" + v + "&"
    return url[0:-1]

dict = {'name':'kimc','age':'33','gender':'true'}
print(makeQuery('http://192.168.11.100',**dict))