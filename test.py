import sys
import time
import traceback
from functools import reduce


def calc(**numbers):
   print(numbers.get("core", 1))

def is_odd(n):
    return n % 2 == 1

if __name__ == '__main__':
    try:
        fh = open("testfile1", "r")
        fh.write("这是一个测试文件，用于测试异常!!")
    except IOError :
        print("Error: 没有找到文件或读取文件失败")
        traceback.print_exc()
        info = sys.exc_info()
        for err in info :
            print(err)
    else:
        print("内容写入文件成功")
        fh.close()
