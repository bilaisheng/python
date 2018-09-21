"""
Author: Lily
Date: 2018-09-17
QQ: 339600718
DHC DHC DHC-s
页面布局：通过省份，城市搜索得到结果。
          不选城市，只选省份可得到全省数据。
          上面是两个下拉下表，左边是数据列表，后边是地图显示。
          搜索的结果的数量会显示在数据list上面
抓取思路：在首页抓取省份的id，通过id作为参数提交get请求得到具体数据页面，
          通过解析页面得到具体数据。
URL: http://www.dhc.net.cn/info/storelist_map.jsp?province_id=JS
"""
import requests
import re
import datetime
from lxml import etree


filename = "DHC-s" + re.sub('[^0-9]', '',str(datetime.datetime.now())) + ".csv"
f = open(filename, 'w', encoding='utf-8')
f.write('store_num,store_id,name,address,phone,lat,lon'+ '\n')
provice_url = 'http://www.dhc.net.cn/info/storelist_map.jsp?province_id=JS'
Province_html = requests.get(provice_url).text
province_lxml = etree.HTML(Province_html)
provinces = province_lxml.xpath('//*[@id="provinceSelect"]/option[position()!=1]/@value')
print(provinces)
for pro in provinces:
    store_url ='http://www.dhc.net.cn/info/storelist_map.jsp?province_id='+pro
    store_html = requests.get(store_url).text
    stores_lxml = etree.HTML(store_html)
    stores_num = stores_lxml.xpath('//div[contains(text(),"店铺")]/text()')[0]
    stores_num = stores_num.strip()
    print(stores_num)
    stores = stores_lxml.xpath('//div[contains(@id,"divps")]/div[@class="shop-div1"]')
    print(len(stores))
    for s in stores:
        print(s)
        name = str(s.xpath('./div[1]/text()')[0])
        name = name.strip()
        address = s.xpath('./table[1]/tr/td[3]/text()')[0]
        address = address.strip()

        phone = s.xpath('./table[2]/tr/td[3]/text()')[0]
        phone = phone.strip()

        onclick = s.xpath('./@onclick')
        store_info = re.findall("goToMap2\('(.*)','(.*)','(.*)'\)", onclick[0])
        store_id = str(store_info[0][0])
        lat = str(store_info[0][1])
        lon = str(store_info[0][2])
        f.write(stores_num + "," + store_id + "," + name + "," + address + "," + phone + "," + lat + "," + lon + "\n")
f.close()

