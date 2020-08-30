import os

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from Common import logger

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
            logging.exception('等待{}元素可见'.format(locator[1]))
            # 截图 - 保存到指定的目录
            self._screenshot(model)
            # 抛出异常
            raise

    # 查找元素
    def get_element(self, locator,model=''):
        try:
            return self.driver.find_element(locator[0], locator[1])
        except:
            # 捕获异常到日志中：
            logging.exception('查找元素失败：')
            # 截图 - 保存到指定的目录
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
            # 截图 - 保存到指定的目录
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
            # 截图 - 保存到指定的目录
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
            # 截图 - 保存到指定的目录
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
            # 截图 - 保存到指定的目录
            self._screenshot(model)
            # 抛出异常
            raise

    def swipe_pages(self,direction,number,model=''):
        try:
            swipe_page(self.driver,direction,number)
        except:
            # 捕获异常到日志中：
            logging.exception('获取文本内容失败：')
            # 截图 - 保存到指定的目录
            self._screenshot(model)
            # 抛出异常
            raise

    def _screenshot(self,model_name):
        #时间
        basePath = os.path.dirname(os.path.dirname(__file__))
        filePath = os.path.join(basePath,'ScreenShot','{}_{}.png'.format(model_name,time.strftime('%Y%m%d_%H%M%S')))
        self.driver.save_screenshot(filePath)
        logging.info('截图成功，图片路径为：{}'.format(filePath))

    def gesture(self,scene,model=''):
        try:
            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            point1 = (1 / 5 * x, 1 / 3 * y)
            point2 = (1 / 2 * x, 1 / 3 * y)
            point3 = (4 / 5 * x, 1 / 3 * y)
            point4 = (1 / 2 * x, 1 / 2 * y)
            point5 = (1 / 5 * x, 2 / 3 * y)
            point6 = (1 / 2 * x, 2 / 3 * y)

            if scene == 'same':
                for i in range(2):
                    TouchAction(self.driver).press(x=int(point1[0]), y=int(point1[1])).wait(2000) \
                        .move_to(x=int(point1[0]), y=int(point1[1])).wait(1500) \
                        .move_to(x=int(point2[0]), y=int(point2[1])).wait(1500) \
                        .move_to(x=int(point3[0]), y=int(point3[1])).wait(1500) \
                        .move_to(x=int(point4[0]), y=int(point4[1])).wait(1500) \
                        .move_to(x=int(point5[0]), y=int(point5[1])).wait(1500) \
                        .move_to(x=int(point6[0]), y=int(point6[1])).wait(1500) \
                        .release().perform()
                    time.sleep(1)
            elif scene == 'different':
                TouchAction(self.driver).press(x=int(point1[0]), y=int(point1[1])).wait(2000) \
                    .move_to(x=int(point1[0]), y=int(point1[1])).wait(1500) \
                    .move_to(x=int(point2[0]), y=int(point2[1])).wait(1500) \
                    .move_to(x=int(point3[0]), y=int(point3[1])).wait(1500) \
                    .move_to(x=int(point4[0]), y=int(point4[1])).wait(1500) \
                    .move_to(x=int(point5[0]), y=int(point5[1])).wait(1500) \
                    .move_to(x=int(point6[0]), y=int(point6[1])).wait(1500) \
                    .release().perform()
                time.sleep(1)
                TouchAction(self.driver).press(x=int(point1[0]), y=int(point1[1])).wait(2000) \
                    .move_to(x=int(point1[0]), y=int(point1[1])).wait(1500) \
                    .move_to(x=int(point2[0]), y=int(point2[1])).wait(1500) \
                    .move_to(x=int(point3[0]), y=int(point3[1])).wait(1500) \
                    .move_to(x=int(point4[0]), y=int(point4[1])).wait(1500) \
                    .move_to(x=int(point5[0]), y=int(point5[1])).wait(1500) \
                    .release().perform()
        except:
            logging.exception('手势失败')
            self._screenshot(model)
            raise
