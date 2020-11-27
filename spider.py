import re   #正则表达式
from urllib.request import urlretrieve
import random
import os
import requests

#定义主函数
def main():
    getData()

#获取图片正则表达式
patternImg = re.compile(r',{"ObjURL":"(.*?)",')

#获取图片url，并且读取图片保存到本地
def getData():
    #获取图片url
    dataList = urlBatch("口罩人脸",50)
    #将图片保存到本地路径
    saveData(dataList,'./images')
    return dataList

#根据图片路径获取图片并保存图片到本地路径
def saveData(urlList,savePath):
    # 本地路径不存在则重新创建路径
    if not os.path.exists(savePath):
        os.mkdir(savePath)

    #下载图片
    index = 1
    for url in urlList:
        try:
            urlretrieve(url,os.path.join(savePath, 'img%s'%(random.randint(1,999999999999999999999999999999999999999))+'.jpg'),callBackFunction)
            index += 1
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(index), str(url)))
            print(e)
            pass

#百度图片搜索url批处理操作 保存图片地址
def urlBatch(keyWord,page):
    #请求参数
    params = []
    #假设每页显示60条记录
    for i in range(0, 30*page+30, 30):
        params.append({
            "tn": "resultjson_com",
            "logid": "12164922078002664171",
            "ipn": "rj",
            "ct": "201326592",
            "is": "",
            "fp": "result",
            "queryWord": keyWord.encode("utf-8"),
            "cl": "2",
            "lm": "-1",
            "ie": "utf-8",
            "oe": "utf-8",
            "adpicid": "",
            "st": "-1",
            "z": "",
            "ic": "",
            "hd": "",
            "latest": "",
            "copyright": "",
            "word": keyWord.encode("utf-8"),
            "s": "",
            "se": "",
            "tab": "",
            "width": "",
            "height": "",
            "face": "0",
            "istype": "2",
            "qc": "",
            "nc": "1",
            "fr": "",
            "expermode": "",
            "force": "",
            "pn": i,
            "rn": "30",
            "gsm": "78",
            "1605687277043": ""
            })
    url = 'https://image.baidu.com/search/acjson'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    contents = []
    for i in params:
        response = requests.get(url,params=i,headers=headers,allow_redirects=False)
        contents.append(response.content)

    #保存图片地址
    urls = []
    finalUrls = []
    for item in contents:
        u = re.findall(patternImg,str(item))
        urls.extend(u)
    for item in urls:
        item = eval(repr(item).replace('\\\\', ''))
        finalUrls.append(item)
    #print(finalUrls)
    return finalUrls

#用于提示下载进度 回调函数
def callBackFunction(downloadSize,blockSize,fileSize):
    '''''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*downloadSize*blockSize/fileSize
    if per>100:
        per=100
    print('%.2f%%' % per)

if __name__ == "__main__":
    main()