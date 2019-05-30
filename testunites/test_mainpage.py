# -*- coding:utf-8 -*-

from framework.browser_engine import BrowserEngine
from pageobject.loginpage import LoginPage
from pageobject.mainpage import MainPage
from pageobject.pldrpage import PldrPage
import unittest
from pywinauto import application

class TestMainPage(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_mainPage(self):
        driver = self.driver
        loginPage = LoginPage(driver)
        mainPage = MainPage(driver)
        pldrPage = PldrPage(driver)

        loginPage.login('admin','admin')
        mainPage.click_daoru()
        mainPage.sleep(3)
        pldrPage.upload_file()
        pldrPage.sleep(3)
        app = application.Application()
        app.connect(class_name='#32770 (对话框)')
        #window = app.window_(class_name="#32770")
        app["Dialog"]["ComboBox"].TypeKeys(r"D:\20190508195129.xls")
        #window["ScrollBar"].Click()
        app["Dialog"]["Button"].Click()
        pldrPage.sleep(10)

if __name__ == '__main__':
    unittest.main()