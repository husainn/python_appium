import unittest
from appium import webdriver
from ddt import ddt,data,unpack

from conf.device_conf import caps2
from model.login import Login

data1 = [
        {'account':'1120103025','psd':'Pafc1502'},
        {'account':'1120101001','psd':'Pafc1502'},
]

@ddt
class Test_login(unittest.TestCase):

    def setUp(self):
        self.Login = Login()
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps2)

    @data(*data1)
    @unpack
    def test_accountlogin(self, account, psd):
        self.Login.account_login(self.driver, account, psd)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()