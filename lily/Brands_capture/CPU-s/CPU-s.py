"""
Author : Lily
Date : 2018-09-18
QQ : 339600718
C.P.U. C.P.U. CPU-s
抓取思路：在初始页面抓取省份列表，做为参数，请求到具体的stores信息
locator_index : http://www.cpuchina.cn/index.php?controller=site&action=store_search
url(post,json,参数 keyword: 北京市) : http://www.cpuchina.cn/index.php?controller=ajax&mod=site&act=search_store

"""
import requests
import re
import datetime
import json
from lxml import etree

fileanme = "CPU-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"
f = open(fileanme, 'w', encoding='utf-8')
f.write('stor_id, store_name, region, store_address, tel,postcode, latlong, visiblity,\n')
index_url = "http://www.cpuchina.cn/index.php?controller=site&action=store_search"
store_url = 'http://www.cpuchina.cn/index.php?controller=ajax&mod=site&act=search_store'
provinces_html = requests.get(index_url).text
provinces_lxml = etree.HTML(provinces_html)
provinces = provinces_lxml.xpath('//div[@class="shopR_contL_tips"]/ul/li/text()')
for pro in provinces:
    print(pro)
    data = {"keyword":pro}
    stores_html = requests.post(store_url, data=data).text
    stores_json = json.loads(stores_html)
    print(stores_json)
    for store in stores_json["data"]:
        print(store.keys())
        for k, v in store.items():
            v = str(v).replace(',', '，').replace('\n', '')
            f.write(v + ',')
        f.write('\n')
f.close()
