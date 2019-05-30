import psutil
import chardet
import requests
import re
count = psutil.cpu_count(logical=False)
#print(count)
#data = '离离原上草，一岁一枯荣'.encode('gbk')
#print(chardet.detect(data))
#print(data.decode('gbk'))
r = requests.get('https://www.douban.com/')
print(r.status_code)
#print(r.text)
data = r.content.decode('utf-8')
# print(chardet.detect(data))
#print(data)

m=re.findall(r'(https://\w.+\.[a-z]+)', data)
for url in m:
    print(url)
