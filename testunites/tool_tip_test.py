# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import unittest
class ToolTipTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://jqueryui.com/tooltip/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()
    def test_tool_tip(self):
        driver = self.driver
        frame_ele = driver.find_element_by_class_name('demo-frame')
        driver.switch_to.frame(frame_ele)

        age_field = driver.find_element_by_id('age')
        ActionChains(self.driver).move_to_element(age_field).perform()

        tool_tip_elm = WebDriverWait(self.driver,10)\
        .until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"ui-tooltip-content")))

        self.assertEqual('We ask for your age only for statistical purposes.',tool_tip_elm.text)

if __name__ == '__main__':
    unittest.main()