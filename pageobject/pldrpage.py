# -*- coding:utf-8 -*-
from framework.base_page import BasePage
from pywinauto import application
class PldrPage(BasePage):
    btn_systemName = "id=>ddl-btn-systemName"
    zyyhy = "xpath=>//*[@id='systemName-ul-li-ul']/li[2]/a"
    btn_upload = "id=>btn-upload"


    def upload_file(self):
        self.click(self.btn_systemName)
        self.click(self.zyyhy)
        self.click(self.btn_upload)
