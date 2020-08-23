# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10"
caps["deviceName"] = "polaris"
caps["appPackage"] = "com.baidu.searchbox"
caps["appActivity"] = "com.baidu.searchbox.SplashActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# el1 = driver.find_element_by_id("com.baidu.searchbox:id/positive_button")
# el1.click()
# el2 = driver.find_element_by_id("android:id/button1")
# el2.click()
# el3 = driver.find_element_by_id("android:id/button1")
# el3.click()
# el4 = driver.find_element_by_id("android:id/button1")
# el4.click()
# time.sleep(10)
# el5 = driver.find_element_by_id("com.baidu.searchbox:id/half_screen_mask_close")
# el5.click()
#等待元素可见
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.baidu.searchbox:id/positive_button")))
#定位多个元素
# eles1 = driver.find_elements_by_class_name('android.widget.Button')
# print('多个元素：',eles1)
#uiautomator定位表达式中，要用双引号。
# eles2 = driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.Button\").textContains(\"同意并继续\")')
# print('多个元素：',eles2)
#xpath
# eles3 = driver.find_element_by_xpath('//android.widget.Button[@text=\"同意并继续\"]')
# print('多个元素：',eles3)
#id
driver.find_element_by_id('com.baidu.searchbox:id/positive_button').click()
el2 = driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_foreground_only_button")
el2.click()
el3 = driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_foreground_only_button")
el3.click()
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.baidu.searchbox:id/half_screen_mask_close")))
el5 = driver.find_element_by_id("com.baidu.searchbox:id/half_screen_mask_close")
el5.click()

#滑动swipe()
size = driver.get_window_size()
x = size['width']
y = size['height']
#左滑
driver.swipe(0.9*x,0.5*y,0.1*x,0.5*y)
time.sleep(1)
#右滑
driver.swipe(0.1*x,0.5*y,0.9*x,0.5*y)
time.sleep(1)
#上滑
driver.swipe(0.5*x,0.8*y,0.5*x,0.2*y)
time.sleep(1)
#下滑
driver.swipe(0.5*x,0.2*y,0.5*x,0.8*y)
time.sleep(1)







# driver.quit()


