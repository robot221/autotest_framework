# -*- coding:utf-8 -*-

from framework.base_page import BasePage


class HomePage(BasePage):
    search_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"

    def type_search(self,text):
        self.type(self.search_box,text)

    def send_submit_button(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)
