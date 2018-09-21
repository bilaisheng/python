"""
Author ： Lily
Date : 2018-09-21
QQ : 339600718
赫妍 HERA Hera-s
抓取思路：所有页面在同一个页面上，直接解析页面即可
Url: http://www.hera.com/cn/zh/misc/store.html
"""
import requests
import re
import datetime
from lxml import etree
filename = "Hera-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"
url = "http://www.hera.com/cn/zh/misc/store.html"
html = requests.get(url).text
html_lxml = etree.HTML(html)
stores  = html_lxml.xpath('//*[@id="main"]/div/div/div/div')
with open(filename, 'w', encoding='utf-8') as f:
    f.write('name,address,lat,lon,\n')
    for store in stores:
        name = store.xpath('./ul/li[1]//text()')[0]
        address = store.xpath('./ul/li[2]//text()')[0]
        lat = store.xpath('./div/div/div/@data-lat')[0]
        lon = store.xpath('./div/div/div/@data-lng')[0]
        f.write(name + "," + address + "," + lat + "," + lon + ",\n")
f.close()