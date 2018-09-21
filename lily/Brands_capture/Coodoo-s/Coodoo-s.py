"""
Author : Lily
Date : 2018-09-21
QQ : 339600718
酷动数码 Coodoo Coodoo-s
抓取思路：数据在页面上，需要翻页，但页面上最大页数，只能从下一页中拿到下一页的页数，再获取下一页的数据
          当没有下一页这个标签时，停止抓取。
URL :http://www.coodoo.com.cn/Stores

"""

import re
import datetime
import requests
from lxml import etree


filename = "Coodoo-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"
f = open(filename, 'w', encoding='utf-8')
f.write('name,address,phone,\n')
n = 1
url = "http://www.coodoo.com.cn/Stores?page="
if n is not None:
    html = requests.get(url+str(n)).text
    html_lxml = etree.HTML(html)
    stores = html_lxml.xpath('//*[@id="main"]/div')
    for store in stores:
        name = store.xpath('./dl/dd/h1/text()')[0]
        address = store.xpath('./dl/dd/text()[1]')[0]
        phone = store.xpath('./dl/dd/text()[2]')[0]
        f.write(name)
