
"""
Author :Lily
Date : 2018-09-11
QQ : 339600718

安踏  ANTA  AnTa-s
抓取思路：1.由于没有locator,需要抓取tencent地图，用CG抓的到几百条就要验证码，CG没法抓取。
          高德API有经纬度和电话，所以从API抓取。
          2.tencentAPI教程：http://lbs.qq.com/webservice_v1/guide-search.html#boundary_detail
          3.url:https://apis.map.qq.com/ws/place/v1/search?boundary=region(北京,0)&keyword=安踏&page_size=20&page_index=1&orderby=_distance&key=QODBZ-KAXC6-T7OSI-MD5VG-2M6KQ-4VB75
          4.根据总数判断翻几页

"""

import requests
import json
import re
import datetime
import csv
from time import sleep
# URL 的第一部分
url = 'https://apis.map.qq.com/ws/place/v1/search?keyword=安踏&page_size=20&orderby=_distance&key=QODBZ-KAXC6-T7OSI-MD5VG-2M6KQ-4VB75&boundary=region('
# URL第二部分
url_page = '&page_index='
# 文件名按照sku+时间命名
url_end = ',0)'
filename = "Anta-s-FromTencet" + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.csv'
# 新建文件
f = open(filename, 'w', encoding='utf-8')
# 写入title
f.write('id,title,address,tel,category,type,location,ad_info' + '\n')
# 打开citylist 遍历每个城市
with open('citys.csv', 'r', encoding='utf-8') as csvfile:
    # 读取city文件
    reader = csv.reader(csvfile)
    # 遍历每个城市
    for row in reader:
        # 获取城市
        city = str(row[0])
        print(city)
        # 先进入初始网址，拿到最大的数量
        html = requests.get(url+city+url_end).text
        # json化 数据
        html = json.loads(html)
        print(html)
        # 获取最大的数量
        pages = int(html['count']) // 20 + 1

        # 翻页
        for p in range(pages):
            print(p+1)
            # 根据城市和页数拼接新的url,下载数据
            html_s = requests.get(url+city+url_end+url_page+str(p+1)).text
            sleep(5)
            # json 化数据
            html_s = json.loads(html_s)
            # 获取 store的数据，遍历每条store数据
            for store in html_s['data']:
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









