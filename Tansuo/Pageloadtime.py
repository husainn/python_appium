# import PyChromeDevTools
# import time
# import os
# os.chdir(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application")
# cmd = "chrome.exe --remote-debugging-port=9222"
# os.popen(cmd)
# chrome = PyChromeDevTools.ChromeInterface()
# chrome.Network.enable()
# chrome.Page.enable()
# chrome.Page.reload(ignoreCache=True)
# start_time =time.time()
# chrome.Page.navigate(url="http://www.baidu.com/")
# chrome.wait_event("Page.loadEventFired",timeout=60)
# end_time = time.time()
# print('Page Loading Time:',end_time-start_time)
# chrome.close()

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
data = driver.execute_script('return window.performance.getEntries();')
print(type(data),data)
dict1 = data[0]
#页面load时间
duration = dict1['duration']

print(dict1['duration'])
driver.close()