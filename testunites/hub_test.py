# -*- coding: utf-8 -*-
from selenium import webdriver
import os,time

chrome_driver = os.path.abspath(r'D:\py-workspace\autotest_framework\tools\chromedriver.exe')
os.environ["webdriver.chrome.driver"] = chrome_driver
chrome_capabilities = {
    "browserName": "chrome",
    "version": "",
    "plateform": "windows",
    "javascriptEnabled": True,
    "webdriver.chrome.driver": chrome_driver
}
driver = webdriver.Remote(command_executor="http://localhost:4455/wd/hub",desired_capabilities=chrome_capabilities)
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(5)
driver.quit()