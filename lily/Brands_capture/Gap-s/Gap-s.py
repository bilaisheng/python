"""
Author : Lily
Date : 2018-09-18
QQ : 339600718
Gap Gap Gap-s
抓取思路：获取city id ,用city id 作为参数请求store具体数据。
city_url(get,json) : https://www.gap.cn/storelocator/index/ajaxgetCity?storecode=CN
store_url(get,json) : https://www.gap.cn/storelocator/index/ajax?id=3
"""

import re
import requests
import datetime
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/53'}
city_url = "https://www.gap.cn/storelocator/index/ajaxgetCity?storecode=CN"
store_url = "https://www.gap.cn/storelocator/index/ajax?id="
citys_json = requests.get(city_url, headers=headers).text
citys_json = json.loads(citys_json)
for city in citys_json:
    citycode = city["id"]
    city_name = city["namech"]
    stores_json = requests.get(store_url+str(citycode), headers=headers).text
    stores_json = json.loads(stores_json)
    for store in stores_json[""]
