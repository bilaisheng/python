"""
Author : Lily
Date : 2018-09-21
QQ : 339600718
一叶子 One leaf OneLeaf-s
抓取思路：所有数据都在一个页面上，只要解析页面即可。
URL:http://www.oneleafchina.com/find
"""
import re
import requests
import datetime
from lxml import etree


filename = "OneLeaf-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"

url = "http://www.oneleafchina.com/find"
html = requests.get(url).text
html_lxml = etree.HTML(html)
stores = html_lxml.xpath('//div[@class="store_list"]/div')
print(stores)
with open(filename, 'w', encoding='utf-8') as f:
    f.write('name,address,phone,lat,lon,\n')
    for store in stores:
        name = store.xpath('./p[@class="store_info_name"]/text()')[0]
        if len(store.xpath('./p[@class="store_info_de"]/text()'))!=0:
            address = str(store.xpath('./p[@class="store_info_add"]/text()')[0]) + str(store.xpath('./p[@class="store_info_de"]/text()')[0])
        else:
            address = store.xpath('./p[@class="store_info_add"]/text()')[0]
        phone = store.xpath('./p[@class="store_info_tel"]/text()')[0].strip()
        lat = store.xpath('./@lat')[0]
        lon = store.xpath('./@lng')[0]
        print(name,address,phone,lat,lon)
        f.write(name + "," + address + "," + phone +  "," + lat + "," + lon + ",\n")



