from appium.webdriver.common.mobileby import MobileBy


class LoginPageLocator:
    #元素定位
    #用户名输入框
    user_input = (MobileBy.ID,'com.paic.esale.activity:id/et_account')
    #密码输入框
    passwd_input = (MobileBy.ID,'com.paic.esale.activity:id/et_password')
    #登录按钮
    login_button = (MobileBy.ID,'com.paic.esale.activity:id/rl_login')