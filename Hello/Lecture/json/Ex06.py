# URL로부터 html text string을 얻는다.
# Python3은  uses urllib.request.urlopen()을 사용
# Python2는 urllib.urlopen() 또는 urllib2.urlopen()
import urllib.request
fp = urllib.request.urlopen("http://www.naver.com")
mybytes = fp.read()
print(mybytes)
mybytes.decode('utf-8')
print(mybytes)
fp.close()
