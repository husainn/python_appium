import unittest
from appium import webdriver
from ddt import ddt, data, unpack

from BasePage import BasePage
from PageLocators.login_page_locator import LoginPageLocator
from PageLocators.origin_page_locator import OriginPageLocator
from conf.device_conf import caps2
from PageObjects.login_page import Login
import logging

data1 = [
    {'account': '1120103025', 'psd': 'Pafc1502'},
    {'account': '1120101001', 'psd': 'Pafc1502'},
]
data2 = [
    {'scene': 'same'},
    {'scene': 'different'},
]

def test_demo():
    print('我是测试用例')

@ddt
class Test_login(unittest.TestCase,LoginPageLocator):

    def setUp(self):
        self.Login = Login()

    @data(*data1)
    @unpack
    def test_account_login(self, account, psd):
        logging.info('开始登录{}账号'.format(account))
        self.Login.origin_activity()
        button_name =  self.Login.account_login(account, psd)
        print(button_name)
        self.assertEqual(button_name,'取消')
        logging.info('{}测试完成'.format(account))

    # @data(*data2)
    # @unpack
    # def test_gesture_login(self,scene):
    #     self.Login.gesture_login(self.driver,scene)

    def tearDown(self):
        pass
        # self.driver.quit()


if __name__ == '__main__':
    unittest.main()
