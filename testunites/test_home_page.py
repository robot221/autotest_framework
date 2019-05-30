# -*- coding:utf-8 -*-

from framework.browser_engine import BrowserEngine
from pageobject.baidu_homepage import HomePage
import unittest,csv,os.path,xlrd
from ddt import ddt,data,unpack

def get_data(file_name,fileType='csv'):
    rows = []
    if fileType == 'csv':

        with open(file_name,'r',encoding='utf-8') as data_file:
            reader = csv.reader(data_file)
            next(reader,None)
            for row in reader:
                rows.append(row)
    elif fileType == 'excel':
        book =xlrd.open_workbook(file_name)
        sheet = book.sheet_by_index(0)
        for row in range(1,sheet.nrows):
            rows.append(sheet.row_values(row,0,sheet.ncols))
    print(rows)
    return rows


@ddt
class TestHomePage(unittest.TestCase):
    dir = os.path.dirname(os.path.abspath('.')) + '/testData/'
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*get_data(dir + 'test.xlsx',fileType='excel'))
    @unpack
    def test_search(self,text,value):
        """测试"""
        homepage = HomePage(self.driver)
        homepage.type_search(text)
        homepage.send_submit_button()
        homepage.sleep(2)
        homepage.get_windows_img()
        #print(value)
        self.assertIn(text, homepage.get_page_title())

    # def test_news_page(self):
    #     homepage = HomePage(self.driver)
    #     homepage.click_news()
    #     homepage.sleep(1)
    #     self.assertIn("百度新闻" , homepage.get_page_title())