"""
Author : Lily
Date : 2018-09-21
QQ : 339600718
新亚 Xinya XinYaStore-s
抓取思路：所有数据都在一个页面上，只要解析页面即可。
URL: http://www.ixinya.com/store

"""

import re
import datetime
import requests
from lxml import etree


filename = "XinYaStore-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"

url = "http://www.ixinya.com/store"
html = requests.get(url).text
html_lxml = etree.HTML(html)
stores = html_lxml.xpath('//div[@class="content"]/div/div')
with open(filename, 'w', encoding='utf-8') as f:
    f.write('name,address,phone,\n')
    for store in stores:
        name = store.xpath('./div[1]//text()')[0].strip()
        address = store.xpath('./div[2]/text()')[0].replace('地址：', '').strip()
        phone = store.xpath('./div[3]/text()')[0].replace('电话：', '')
        print(name,"kai"+ address,phone)
        f.write(name + "," + address + "," + phone + ",\n")