import time

from Common.BasePage import BasePage

import logging
from Common import logger
from PageLocators.login_page_locator import LoginPageLocator
from PageLocators.origin_page_locator import OriginPageLocator


class Login(LoginPageLocator,BasePage,OriginPageLocator):

    def origin_activity(self):
        #权限弹框
        name = '初始化页面'
        self.click_element(self.permission_allow,name)
        #升级弹框
        try:
            self.wait_ele_visible(self.update_cancel,model=name)
            self.click_element(self.update_cancel,name)
        except:
            pass
        #滑动
        time.sleep(1)
        self.swipe_pages('left',3,name)
        # 立即体验
        self.click_element(self.lijitiyan,name)
        #unknow
        # self.wait_ele_visible(self.unknow,model=name)
        # self.click_element(self.unknow,name)
        # 隐私政策
        self.wait_ele_visible(self.yinsizhengce,model=name)
        self.click_element(self.yinsizhengce,name)
        # 同意
        self.click_element(self.allow_btn,name)

    def account_login(self, account, psd):
        # 账号
        name = '登录页面_登录功能'
        self.wait_ele_visible(self.user_input,model=name)
        logging.info('输入账号')
        self.input_text(self.user_input,account)
        # driver.find_element_by_id('com.paic.esale.activity:id/et_account').send_keys(account)
        # 密码
        logging.info('输入密码')
        self.input_text(self.passwd_input,psd)
        # driver.find_element_by_id('com.paic.esale.activity:id/et_password').send_keys(psd)
        # 登录
        logging.info('点击登录')
        self.click_element(self.login_button)
        #指纹弹框
        self.wait_ele_visible(self.finger_cancel,model=name)
        #
        return self.get_text(self.finger_cancel)

        # driver.find_element_by_id('com.paic.esale.activity:id/rl_login').click()

    def gesture_login(self,scene):
        name = '设置手势密码'
        # 取消指纹密码设置
        self.click_element(self.finger_cancel,name)
        time.sleep(1)
        # driver.find_element_by_id('com.paic.esale.activity:id/pbt_dialog_cancel').click()
        # 手势密码设置设置
        self.gesture(scene,name)
