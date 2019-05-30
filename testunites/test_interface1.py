# -*- coding:utf-8 -*-

import unittest,os.path,xlrd,csv,requests
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
            rows.append(sheet.row_values(row,1,sheet.ncols))
    print(rows)
    return rows

@ddt
class TestInterface(unittest.TestCase):
    dir = os.path.dirname(os.path.abspath('.')) + '/testData/'
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*get_data(dir + 'interface1.xls',fileType='excel'))
    @unpack
    def test_interface(self,name,params):
        headers = {"Content-Type": "application/json"}
        url = "http://183.129.208.90:49697/uip-ccloud-icop/services"
        print(f'接口名称为:{name}')
        params = params.encode('utf-8')
        rs = requests.post(url,data=params,headers=headers).json()
        print(rs)

if __name__ == "__main__":
    unittest.main()