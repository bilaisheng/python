import requests
import json
import csv
from time import sleep
url = "https://innisfree.e.verystar.cn/Member/Store/storelist"

headers = {
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 micromessage/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN',
    'Accept-Encoding': 'gzip, deflate,br',
    'Content-type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, data={'prov': '%E5%B9%BF%E4%B8%9C%E7%9C%81', 'city': '%E6%B7%B1%E5%9C%B3%E5%B8%82', 'lat': 22.53783323682006, 'lng': 114.03229582109043}, verify=False)

print(response.text)