from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

from common.common_func import swipe_page
from conf.device_conf import caps2

class Login:

    def account_login(self,driver,account,psd):
        time.sleep(1)
        try:
            el1 = driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_foreground_only_button")
            el1.click()
        except Exception as e:
            print('ele1', e)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((MobileBy.ID, 'com.paic.esale.activity:id/btn1')))
        try:
            driver.find_element_by_id('com.paic.esale.activity:id/btn1').click()
        except Exception as e:
            print(e)
        time.sleep(1)
        swipe_page(driver, 'left', 3)
        time.sleep(1)
        # 立即体验
        driver.find_element_by_id('com.paic.esale.activity:id/btnStart').click()
        time.sleep(0.5)
        # driver.find_element_by_id('com.paic.esale.activity:id/btn1').click()
        # 隐私政策
        driver.find_element_by_id('com.paic.esale.activity:id/cb_privacypolicy').click()
        # 同意
        driver.find_element_by_id('com.paic.esale.activity:id/pbt_dialog_sure').click()
        # 账号
        driver.find_element_by_id('com.paic.esale.activity:id/et_account').send_keys(account)
        # 密码
        driver.find_element_by_id('com.paic.esale.activity:id/et_password').send_keys(psd)
        # 登录
        driver.find_element_by_id('com.paic.esale.activity:id/rl_login').click()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((MobileBy.ID, 'com.paic.esale.activity:id/pbt_dialog_cancel')))
        # 取消指纹密码设置
        driver.find_element_by_id('com.paic.esale.activity:id/pbt_dialog_cancel').click()
        #取消手势密码
        driver.find_element_by_android_uiautomator('new UiSelector().text("跳过")').click()