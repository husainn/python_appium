import pytest
from PageObjects.login_page import Login

#登录用例的前置和后置
#setup和teardown
@pytest.fixture
def init_loginEnv():
    #前置
    print('--------用例级别开始---------')
    login = Login()
    #后置
    yield login
    login.driver.quit()
    print('--------用例级别结束---------')

#setupClass，teardownClass
@pytest.fixture(scope='class')
def class_demo():
    print('---------------我是class级别的fixture----------')