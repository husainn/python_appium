import logging
import os

'''
设置为debug级别则包含下面所有的级别日志
DEBUG：详细信息，用于诊断问题。Value=10。
INFO：确认代码运行正常。Value=20。
WARNING：意想不到的事情发生了，或预示着某个问题。但软件仍按预期运行。Value=30。
ERROR：出现更严重的问题，软件无法执行某些功能。Value=40。
CRITICAL：严重错误，程序本身可能无法继续运行。Value=50。
'''
path =os.path.join(os.path.dirname(os.path.dirname(__file__)),'Log','log.txt')

print(path)
fh = logging.FileHandler(path,encoding='utf-8')
sh = logging.StreamHandler()#输出到控制台
format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'

logging.basicConfig(level=logging.INFO,handlers=[fh,sh],format=format)
