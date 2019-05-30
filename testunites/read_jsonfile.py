# -*- coding:utf-8 -*-
import json
import xlwt
filepath =r'D:\BaiduNetdiskDownload\杭州大厦物业管理APP接口.postman_collection.json'
xls_file = r'D:\interface1.xls'
with open(filepath,'r',encoding='utf-8')as f:
    data = f.read()
    data2 = json.loads(data)
    ff = xlwt.Workbook(encoding='utf-8')
    sheet1 = ff.add_sheet('杭州大厦物业管理APP接口')
    row0 = ['id','name','request']
    for i in range(len(row0)):
        sheet1.write(0,i,row0[i])
    #names = data2['item']['name']
    #print(data)
    #print(type(data))
    print(data2)
    #print(type(data2))
    #print(data2['info'])
    #print(type(data2['info']))
    #info = data2['info']
    #name = data2['info']['name']
    #print(name)
    items = data2['item']
    #print(items)
    #print(type(items))
    id = 1
    for item in items:
        row = [id,item['name'],item['request']['body']['raw']]
        for i in range(len(row)):
            sheet1.write(id,i,row[i])
        id = id + 1
        print(item['name'])
        print(item['request']['body']['raw'])

    ff.save(xls_file)