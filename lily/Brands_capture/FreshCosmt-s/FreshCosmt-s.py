"""
Author : Lily
Date : 2018-09-21
QQ : 339600718
fresh fresh FreshCosmt-s
抓取思路：所有数据都后台json文件里，查看页面源代码是看不到数据的。
URL :https://cn.fresh.com/on/demandware.store/Sites-fresh-cn-Site/zh_CN/Stores-GetNearestStores?lat=32.057236&lng=118.778074
"""

import re
import requests
import datetime
import json


filename = "FreshCosmt-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"

url = "https://cn.fresh.com/on/demandware.store/Sites-fresh-cn-Site/zh_CN/Stores-GetNearestStores?lat=32.057236&lng=118.778074"
html = requests.get(url).text
html_json = json.loads(html)
n = 1
print(html_json['stores'])
with open(filename, 'w', encoding='utf-8') as f:
    for index_k, index_v in html_json['stores'].items():
        if n==1:
            for title in index_v.keys():
                f.write(title + ',')
            f.write('\n')
            n = n+1
        for s_k, s_v in index_v.items():
            s_v = str(s_v).replace(',', '，').replace('\n', '')
            f.write(s_v+",")
        f.write('\n')
f.close()
