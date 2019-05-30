# -*- coding:utf-8 -*-

from selenium import webdriver
from configparser import ConfigParser
from framework.logger import Logger
import os.path

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):
    def __init__(self,driver):
       self.driver = driver

    def open_browser(self,driver):
        config = ConfigParser()
        conf_file = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(conf_file)
        browserName = config.get('browserType', 'browserName')
        logger.info(f"你选择的浏览器是：{browserName}")
        testUrl = config.get('testServer', 'URL')
        logger.info(f'待测试系统ULR是：{testUrl}')
        dir_path = os.path.dirname(os.path.abspath('.')) + '/tools/'
        if browserName == 'Chrome':
            chrome_path = dir_path + 'chromedriver.exe'
            driver = webdriver.Chrome(chrome_path)
            logger.info('开始启动chrome浏览器')
        elif browserName == 'Firefox':
            driver = webdriver.Firefox()
            logger.info('开始启动Firefox浏览器')
        elif browserName == 'IE':
            ie_path = dir_path + 'IEDriverServer.exe'
            driver = webdriver.Ie(ie_path)
            logger.info('开始启动Ie浏览器')
        driver.get(testUrl)
        driver.maximize_window()
        logger.info('最大化当前窗口')
        driver.implicitly_wait(10)
        logger.info('设置隐式等待时间为10秒')
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info('退出并关闭浏览器')
