
'''
#get请求
import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode("utf-8"))
'''

'''
#post请求
import urllib.request
import urllib.parse
data = bytes(urllib.parse.urlencode({"name":"solar"}),encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read())
print(response.read().decode("utf-8"))
'''

'''
#异常处理
import urllib.request
import urllib
try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
except urllib.error.URLError as result:
    print(result)
'''


'''
#post请求 修改header信息，模拟浏览器发送请求
import urllib.request
import urllib.parse
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({"name":"solar"}),encoding="utf-8")
req = urllib.request.Request(url,method="POST",data=data,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''

'''
import urllib.request
import urllib.parse
url = "https://www.douban.com/"
data = bytes(urllib.parse.urlencode({"name":"solar"}),encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
req = urllib.request.Request(url,method="POST",data=data,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''

import urllib.request
import urllib.parse
url = "https://www.baidu.com/"
data = bytes(urllib.parse.urlencode({"name":"solar"}),encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
req = urllib.request.Request(url,method="POST",data=data,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
