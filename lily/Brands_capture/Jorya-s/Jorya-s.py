"""
author: Lily
date: 2018-08-30
QQ:339600718
JORYA JORYA Jorya-s
抓取思路：在选择城市的页面抓取所有城市的id，
          作为参数获取每个城市的json文件，然后解析，写入文件。
注意:     每一页显示10个,这个牌子刚好没有哪一个城市是超过10的,所以没有翻页.以后数据多了需要翻页.
          可以参照 亦谷 yigue YiGue-s


"""
import requests
from bs4 import BeautifulSoup
import re
import json
import datetime


# sku+时间戳命名文件，方便以后再次运行
filename = "Jorya-s" + re.sub(r'[^0-9]', '', str(datetime.datetime.now()))+".csv"
# 创建文件，待将数据写入
f = open(filename, 'w', encoding='utf-8')
# 将title写入
f.write('shop_id,shop_code,avg_score,distance,lng,lat,shop_pic,shop_sign_cnt,shop_name,shop_type,'
        'comtact,address,tel,mobile,is_gift,lngb,latb'+"\n")
# 加载城市选择页面
html = requests.get("http://h.qizhuyun.com/c81141/shop/otherCity")
print(html.text)
# 初始化BautifulSoup
soup = BeautifulSoup(html.text, 'lxml')
# 在页面中找到所有城市的id,即所有a标签且属性class=city_css
for a in soup.find_all(name = "a",attrs = {'class': 'city_css'}):
    # 用正则表达式提取城市的id
    s = re.search('city=(.*)&city', a.attrs["href"])
    # 获取城市id
    cityid = s.group(1)
    # 拼接请求每个城市信息的URL
    url = "http://h.qizhuyun.com/c81141/shop/get_new_list?shop_city=" + cityid
    # 加载每个城市的文件
    store_json = requests.get(url)
    # 将文件json化
    stores = json.loads(store_json.text)
    # 遍历每条数据
    for s in stores:
        # 遍历每条数据的每个属性
        for k, v in s.items():
            # 去英文逗号，如果有英文逗号会错列
            v = str(v).replace(',', '')
            # 写入文件
            f.write(v+",")
        # 写文一条数据后换行
        f.write('\n')
# 关闭文件
f.close()

