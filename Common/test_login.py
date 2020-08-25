import unittest
from appium import webdriver
from ddt import ddt, data, unpack

from conf.device_conf import caps2
from module.login import Login
import logging
from Log import logger


data1 = [
    {'account': '1120103025', 'psd': 'Pafc1502'},
    {'account': '1120101001', 'psd': 'Pafc1502'},
]
data2 = [
    {'scene': 'same'},
    {'scene': 'different'},
]

@ddt
class Test_login(unittest.TestCase):

    def setUp(self):
        self.Login = Login()
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps2)

    @data(*data1)
    @unpack
    def test_account_login(self, account, psd):
        logging.info('开始登录{}账号'.format(account))
        self.Login.account_login(self.driver, account, psd)
        logging.info('{}测试完成'.format(account))

    # @data(*data2)
    # @unpack
    # def test_gesture_login(self,scene):
    #     self.Login.gesture_login(self.driver,scene)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
