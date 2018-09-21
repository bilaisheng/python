"""
Author : Lily
Date : 2018-09-17
QQ : 339600718
欧珀莱 AUPRES Aupres-s
抓取思路：
Locatore:https://www.aupres.com.cn/index.php?r=toshop/index/#tomap
URL（post,返回json，参数：city=北京）:https://www.aupres.com.cn/index.php?r=toshop/getcitysinfo
有待加强的地方：网页加载很慢，有时候加载不出来，就报错
"""
import requests
import json
import re
import datetime
from lxml import etree

index_url = 'https://www.aupres.com.cn/index.php?r=toshop/index/#tomap'
url = 'https://www.aupres.com.cn/index.php?r=toshop/getcitysinfo'
html = requests.get(index_url).text

html_lxml = etree.HTML(html)
citys = html_lxml.xpath('//select[@id="city_select"]/option[position()!=1]/text()')
filename = "Aupres-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"
f = open(filename, 'w', encoding='utf-8')
f.write('address,shop_name,phone_number,id,shop_code' + '\n')
for ct in citys:
    data = {'city': ct}
    stores_json = requests.post(url, data=data).text
    stores = json.loads(stores_json)
    for store in stores:
        print(store)
        for k, v in store.items():
            v = str(v).replace(',', '')
            f.write(v + ',')
        f.write('\n')
f.close()