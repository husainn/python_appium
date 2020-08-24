from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

from Common.common_func import swipe_page


class Login:

    def account_login(self, driver, account, psd):
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

    def gesture_login(self, driver,scene):
        self.account_login(driver, '1120103025', 'Pafc1502')
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((MobileBy.ID, 'com.paic.esale.activity:id/pbt_dialog_cancel')))
        # 取消指纹密码设置
        driver.find_element_by_id('com.paic.esale.activity:id/pbt_dialog_cancel').click()
        # 手势密码设置设置
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        print(x, y)
        point1 = (1 / 5 * x, 1 / 3 * y)
        point2 = (1 / 2 * x, 1 / 3 * y)
        point3 = (4 / 5 * x, 1 / 3 * y)
        point4 = (1 / 2 * x, 1 / 2 * y)
        point5 = (1 / 5 * x, 2 / 3 * y)
        point6 = (1 / 2 * x, 2 / 3 * y)

        if scene == 'same':
            for i in range(2):
                TouchAction(driver).press(x=int(point1[0]), y=int(point1[1])).wait(2000) \
                    .move_to(x=int(point1[0]), y=int(point1[1])).wait(1500) \
                    .move_to(x=int(point2[0]), y=int(point2[1])).wait(1500) \
                    .move_to(x=int(point3[0]), y=int(point3[1])).wait(1500) \
                    .move_to(x=int(point4[0]), y=int(point4[1])).wait(1500) \
                    .move_to(x=int(point5[0]), y=int(point5[1])).wait(1500) \
                    .move_to(x=int(point6[0]), y=int(point6[1])).wait(1500) \
                    .release().perform()
                time.sleep(5)
        elif scene == 'different':
            TouchAction(driver).press(x=int(point1[0]), y=int(point1[1])).wait(2000) \
                .move_to(x=int(point1[0]), y=int(point1[1])).wait(1500) \
                .move_to(x=int(point2[0]), y=int(point2[1])).wait(1500) \
                .move_to(x=int(point3[0]), y=int(point3[1])).wait(1500) \
                .move_to(x=int(point4[0]), y=int(point4[1])).wait(1500) \
                .move_to(x=int(point5[0]), y=int(point5[1])).wait(1500) \
                .move_to(x=int(point6[0]), y=int(point6[1])).wait(1500) \
                .release().perform()
            time.sleep(5)
            TouchAction(driver).press(x=int(point1[0]), y=int(point1[1])).wait(2000) \
                .move_to(x=int(point1[0]), y=int(point1[1])).wait(1500) \
                .move_to(x=int(point2[0]), y=int(point2[1])).wait(1500) \
                .move_to(x=int(point3[0]), y=int(point3[1])).wait(1500) \
                .move_to(x=int(point4[0]), y=int(point4[1])).wait(1500) \
                .move_to(x=int(point5[0]), y=int(point5[1])).wait(1500) \
                .release().perform()
            time.sleep(5)
