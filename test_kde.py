from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

from device_conf import caps2

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps2)
try:
    el1 = driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_foreground_only_button")
    el1.click()

    size = driver.get_window_size()
    x = size['width']
    y = size['height']

    for i in range(4):
        driver.swipe(0.9 * x, 0.5 * y, 0.1 * x, 0.5 * y)
        time.sleep(1)
except Exception as e:
    print(e)

driver.find_element_by_id('com.paic.esale.activity:id/btn1').click()

