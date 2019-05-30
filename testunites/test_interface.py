import requests
import json
data = """
{
	"reqPubInfo": {
		"systemNo": "02",
		"method": "appLoginConfirm",
		"transactionID": "012014030000000001",
		"requestTime": "20140306150501",
		"version": "1.0",
		"sign": "f9fe352f8f4d387bfa456ae57c9ec784"
	},
	"busiInfo": {
		"registrationInfo": "141fe1da9e9b37056ca",
		"loginName": "18667020001",
		"password": "123",
		"loginType": "1"
	}
}
"""
json = '{\r\n\t\"reqPubInfo\": {\r\n\t\t\"systemNo\": \"02\",\r\n\t\t\"method\": \"appLoginConfirm\",\r\n\t\t\"transactionID\": \"012014030000000001\",\r\n\t\t\"requestTime\": \"20140306150501\",\r\n\t\t\"version\": \"1.0\",\r\n\t\t\"sign\": \"f9fe352f8f4d387bfa456ae57c9ec784\"\r\n\t},\r\n\t\"busiInfo\": {\r\n\t\t\"registrationInfo\": \"141fe1da9e9b37056ca\",\r\n\t\t\"loginName\": \"18667020001\",\r\n\t\t\"password\": \"123\",\r\n\t\t\"loginType\": \"1\"\r\n\t}\r\n}'
#print(json.dumps(data))
headers = {"Content-Type":"application/json"}
url = "http://183.129.208.90:49697/uip-ccloud-icop/services"

rs = requests.post(url,data=json,headers = headers).json()
#rs = requests.post(url,json=json).json()
token = rs['busiInfo']['token']
staffId = rs['busiInfo']['staffId']
resPubInfo = rs['resPubInfo']
print(f'token:{token},staffId:{staffId}')
print(resPubInfo)
print(rs)