# -*- coding:utf-8 -*-

from framework.base_page import BasePage

class LoginPage(BasePage):
    username = "id=>username"
    password = "id=>password"
    submit_btn = "id=>submit-btn"

    def login(self,uname,passwd):
        self.type(self.username,uname)
        self.type(self.password,passwd)
        self.click(self.submit_btn)