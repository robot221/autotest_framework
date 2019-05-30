# -*- coding:utf-8 -*-

from framework.base_page import BasePage

class MainPage(BasePage):
    fee_menu = "id=>accordion-item-272"
    daoru = "id=>accordion-item-237"

    def click_daoru(self):
        self.mouse_to_element(self.fee_menu)
        self.click(self.daoru)
