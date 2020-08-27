import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from Log import logger
import time

from Common.common_func import swipe_page
from conf.device_conf import caps2


class BasePage:
    def __init__(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps2)

    # 等待元素可见 - 失败的时候有截图有日志
    def wait_ele_visible(self, locator, wait_times=20, poll_frequency=0.5,model=''):
        '''
        :param locator:类型为元组（By.xxx,定位表达式）
        :return:
        '''
        try:
            #开始时间
            logging.info('等待操作----')
            start_time = time.time()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(
                EC.visibility_of_element_located(locator))
            end_time = time.time()
            logging.info('等待耗时{}'.format(start_time-end_time))
        except:

            # 捕获异常到日志中：
            logging.exception('等待元素可见：')
            # 截图 - 保存到指定的目录，名字要怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

    # 查找元素
    def get_element(self, locator,model=''):
        try:
            return self.driver.find_element(locator[0], locals([1]))
        except:
            # 捕获异常到日志中：
            logging.exception('查找元素失败：')
            # 截图 - 保存到指定的目录，名字要怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

    # 输入操作
    def input_text(self, locator, text,model=''):
        # 找到元素
        ele = self.get_element(locator,model)
        try:
            ele.send_keys(text)
        except:
            # 捕获异常到日志中：
            logging.exception('输入操作失败：')
            # 截图 - 保存到指定的目录，名字要怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

    # 点击操作
    def click_element(self, locator,model=''):
        ele = self.get_element(locator,model)
        try:
            ele.click()
        except:
            # 捕获异常到日志中：
            logging.exception('点击操作失败：')
            # 截图 - 保存到指定的目录，名字要怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

    # 获取元素的属性
    def get_element_attribute(self,locator,attr_name,model=''):
        #找到元素
        ele = self.get_element(locator,model)
        try:
            return ele.get_attribute(attr_name)
        except:
            # 捕获异常到日志中：
            logging.exception('获取元素属性失败：')
            # 截图 - 保存到指定的目录，名字要怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

    # 获取元素的文本
    def get_text(self,locator,model=''):
        #找到元素
        ele = self.get_element(locator,model)
        try:
            return ele.text
        except:
            # 捕获异常到日志中：
            logging.exception('获取文本内容失败：')
            # 截图 - 保存到指定的目录，名字要怎么取？
            self._screenshot(model)
            # 抛出异常
            raise
    def swipe_pages(self,direction,number,model=''):
        #找到元素
        try:
            swipe_page(self.driver,direction,number)
        except:
            # 捕获异常到日志中：
            logging.exception('获取文本内容失败：')
            # 截图 - 保存到指定的目录，名字要怎么取？
            self._screenshot(model)
            # 抛出异常
            raise

    def _screenshot(self,model_name):
        #时间
        basePath = os.path.dirname(os.path.dirname(__file__))
        filePath = os.path.join(basePath,'ScreenShot','{}_{}.png'.format(model_name,time.strftime('%Y%m%d_%H%M%S')))
        self.driver.save_screenshot(filePath)
        logging.info('截图成功，图片路径为：{}'.format(filePath))
