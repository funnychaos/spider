#正则表达式demo
import re

pat = re.compile("aa")
r = pat.search("aabbbcaa")
r = re.search("aa","ccdaaadd")
r = re.findall("a","AAddjiafijida") #前面字符串时规则，后面字符串是被校验的字符串
r = re.findall("[a-z]","ddajlfdija112AAA")
r = re.findall("[a-z]+","ddajlfdija112AdjjjAA")
r = re.sub("a","A","dfaijifaae")    #用A替换a
print(r)
a = r"\aad\-'"      #使得转义字符不要被转换
print(a)

