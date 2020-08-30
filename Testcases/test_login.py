import pytest
from PageLocators.login_page_locator import LoginPageLocator
from PageObjects.login_page import Login
import logging
from Common import logger

data1 = [
    {'account': '1120103025', 'psd': 'Pafc1502'},
    {'account': '1120101001', 'psd': 'Pafc1502'},
]


@pytest.mark.demo
def test_demo():
    print('我是测试用例')
    logging.info('test run')
    assert False


@pytest.mark.login
@pytest.mark.usefixtures('class_demo')
@pytest.mark.usefixtures('init_loginEnv')
class Test_login:

    @pytest.mark.smoke
    # init_loginEnv接收 fixture运行的返回值 login
    def test_origin(self, init_loginEnv):
        logging.info('开始初始化app')
        init_loginEnv.origin_activity()

    @pytest.mark.parametrize('data',data1)
    def test_account_login(self ,init_loginEnv, data):
        logging.info('开始登录{}账号'.format(data['account']))
        init_loginEnv.origin_activity()
        button_name = init_loginEnv.account_login(data['account'], data['psd'])
        print(button_name)
        assert button_name == '取消'
        logging.info('{}测试完成'.format(data['account']))

    def test_gesture_login_true(self, init_loginEnv):
        init_loginEnv.origin_activity()
        init_loginEnv.account_login('1120103025', 'Pafc1502')
        init_loginEnv.gesture_login('same')

    def test_gesture_login_false(self, init_loginEnv):
        init_loginEnv.origin_activity()
        init_loginEnv.account_login('1120103025', 'Pafc1502')
        init_loginEnv.gesture_login('different')
