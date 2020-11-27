#用于查看中文编码

import sys

def main():
    enCode("戴口罩人脸")
    deCode(b'\xe6\x88\xb4\xe5\x8f\xa3\xe7\xbd\xa9\xe4\xba\xba\xe8\x84\xb8')

#编码
def enCode(keyWord):
    code = keyWord.encode("utf-8")
    print(code)

#解码
def deCode(code):
    keyWord = code.decode("utf-8")
    print(keyWord)




if __name__ == "__main__":
    main()



