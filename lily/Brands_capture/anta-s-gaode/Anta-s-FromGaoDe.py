
"""
Author :Lily
Date : 2018-09-06
QQ : 339600718

安踏  ANTA  AnTa-s
抓取思路：1.由于没有locator,需要抓取高德地图，用CG也可以抓，但是没有经纬度和电话。
          高德API有经纬度和电话，所以从API抓取。
          2.高德API教程：https://lbs.amap.com/api/webservice/guide/api/search
          3.url:https://restapi.amap.com/v3/place/text?keywords=%E5%AE%89%E8%B8%8F&city=beijing&key=ea09814ea8f79b7ba56bc241cd23223b&offset=50&page=1
          keywords  :  安踏
          city :需要遍历所有的城市
          key :需要注册后申请
          offset: 每页的最大数据量,最大为50。（offset=50即每页显示50条数据）
          page : 翻页
          4.根据总数判断翻几页

"""

import requests
import json
import re
import datetime
import csv
# URL 的第一部分
url = 'https://restapi.amap.com/v3/place/text?keywords=安踏|anta|Anta&key=ea09814ea8f79b7ba56bc241cd23223b&offset=50&city='
# URL第二部分
url_page = '&page='
# 文件名按照sku+时间命名
filename = "Anta-s" + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.csv'
# 新建文件
f = open(filename, 'w', encoding='utf-8')
# 写入title
f.write('id,name,type,typecode,biz_type,address,location,tel,distance,biz_ext,pname,cityname,adname,importance,shopid,shopinfo,poiweight,photos' + '\n')
# 打开citylist 遍历每个城市
with open('citys.csv', 'r', encoding='utf-8') as csvfile:
    # 读取city文件
    reader = csv.reader(csvfile)
    # 遍历每个城市
    for row in reader:
        # 获取城市
        city = str(row[0])
        # 先进入初始网址，拿到最大的数量
        html = requests.get(url+city+url_page+str(1)).text
        # json化 数据
        html = json.loads(html)
        # 获取最大的数量
        pages = int(html['count']) // 50 + 1
        # 翻页
        for p in range(pages):
            # 根据城市和页数拼接新的url,下载数据
            html_s = requests.get(url+city+url_page+str(p+1)).text
            # json 化数据
            html_s = json.loads(html_s)
            # 获取 store的数据，遍历每条store数据
            for store in html_s['pois']:
                # 遍历store的每一个属性
                for k, v in store.items():
                    # 将英文逗号换成中文逗号，以防错列
                    v = str(v).replace(',', '，')
                    # 写入数据
                    f.write(v+',')
                # 写完一条数据后换行
                f.write('\n')
# 关闭文件
f.close()









