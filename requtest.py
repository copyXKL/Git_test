import requests
JXurl = 'http://222.128.104.222:55504/api/stationCard/callbackDoorCmd'
JXdata = \
{
  "CN" : "3123",
  "ExeRtn" : "2",
  "doorCmdId" : "872442177746849792",
  "isSuccessful" : "0",
  "stationId" : "852477107247992832"
}

response = requests.post(JXurl, json=JXdata)
if response.status_code == 200:
    data = response.json()
    headers = response.headers
    print(data)
else:
    print(f"失败，状态码：{response.status_code}")