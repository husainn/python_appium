import logging
'''
DEBUG：详细信息，用于诊断问题。Value=10。
INFO：确认代码运行正常。Value=20。
WARNING：意想不到的事情发生了，或预示着某个问题。但软件仍按预期运行。Value=30。
ERROR：出现更严重的问题，软件无法执行某些功能。Value=40。
CRITICAL：严重错误，程序本身可能无法继续运行。Value=50。
'''

logging.basicConfig(level=logging.ERROR,filename='D:\workspace\python_appium\Common\log.log',format='%(asctime)s :: %(levelname)s :: %(message)s')
