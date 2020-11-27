#关于beaustfulSoup的使用
from bs4 import BeautifulSoup
import re

'''
file = open("./baidu.html","rb")
html = file.read()
bs =BeautifulSoup(html,"html.parser")
#print(bs.title) #<title>页面不存在_百度搜索</title>
#print(bs.a) #<a href="//www.baidu.com/" id="result_logo"><img alt="到百度首页" src="//www.baidu.com/img/baidu_jgylogo3.gif" title="到百度首页"/></a>
#print(bs.head)  #获取<head>标签的东西
#print(type(bs.head))    #此数据类型为标签tag <class 'bs4.element.Tag'>

#print(bs.title.string)  #页面不存在_百度搜索
#print(type(bs.title.string))    #<class 'bs4.element.NavigableString'>

#print(bs.a.attrs)   #列举a标签内的属性 {'href': '//www.baidu.com/', 'id': 'result_logo'}
# print(type(bs.a.attrs)) #<class 'dict'>
#
# print(type(bs)) #<class 'bs4.BeautifulSoup'>

print(bs.div)
'''

'''
#文件遍历
file = open("./baidu.html","rb")
html = file.read()
bs =BeautifulSoup(html,"html.parser")
#print(bs.head.contents)
#print(bs.body.contents)
#print(bs.body.contents[0])
print(bs.head.parents)

'''


def name_is_exist(tag):
    return tag.has_attr("name")

#文件搜索
file = open("./baidu.html","rb")
html = file.read()
bs =BeautifulSoup(html,"html.parser")
#t_list= bs.find_all("a")    #查找与字符串完全相同的内容
#t_list = bs.find_all(re.compile("a"))   #通过正则表达搜索内容
#t_list = bs.find_all(re.compile("^<a>.*$"))
#t_list = bs.find_all(name_is_exist)      #根据函数内容来搜索

#t_list = bs.find_all(id="form")
#t_list = bs.find_all(class_ = True)
#t_list = bs.find_all(href = "http://qingting.baidu.com/index")

#t_list = bs.find_all(text= "反馈给我们")
#t_list = bs.find_all(text=["反馈给我们","到百度首页"])

#t_list = bs.find_all(text=re.compile("\d"))

t_list = bs.select(".s_form_wrapper")   #通过类名查找
t_list = bs.select("title")     #通过标签查找
t_list = bs.select("#kw")       #通过id查找
t_list = bs.select("a[wdfield = 'word']")   #通过a标签内的属性值查找
t_list = bs.select("head > title")      #通过标签层级查找


print(t_list)



