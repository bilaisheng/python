
"""
Author :Lily
Date : 2018-09-07
QQ : 339600718

安踏  ANTA  AnTa-s
抓取思路：1.由于没有locator,需要抓取百度地图，用CG也可以抓，但是没有经纬度和电话，抓取的数据不全。
          百度API有经纬度和电话，所以从API抓取。
          2.百度API教程：http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
          3.url:http://api.map.baidu.com/place/v2/search?query=安踏&region=北京市&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_num=1&page_size=20
          query  :  安踏（只能填一个）所以需要抓多次（因为要用3个关键字搜：安踏；anta;Anta）
          region :需要遍历所有的城市
          ak :需要注册后申请
          page_size: 每页的最大数据量,最大为50。（offset=50即每页显示50条数据）
          scope：信息的详细程度
          page_num : 翻页
          4.根据总数判断翻几页
          5.抓到一半就会受限，需要睡眠一段时间再抓一次

"""

import requests
import json
import re
import datetime
import csv
from time import sleep

url =['http://api.map.baidu.com/place/v2/search?query=anta$Anta$安踏&bounds=39.531759, 115.739015,40.636086, 117.021333&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20'
,'http://api.map.baidu.com/place/v2/search?query=anta$Anta$安踏&bounds=37.390175, 113.518890,38.985030, 115.870231&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20'
,'http://api.map.baidu.com/place/v2/search?query=anta$Anta$安踏&bounds=36.426340, 116.522993,37.147208, 117.533562&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20'
,'http://api.map.baidu.com/place/v2/search?query=anta$Anta$安踏&bounds=35.793708, 119.441444,37.126415, 121.321338&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20'
,'http://api.map.baidu.com/place/v2/search?query=anta$Anta$安踏&bounds=30.745855, 120.717305,31.882268, 121.718979&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20'
,'http://api.map.baidu.com/place/v2/search?query=anta$Anta$安踏&bounds=30.069471, 113.730134,31.262087, 114.971265&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20'
,'http://api.map.baidu.com/place/v2/search?query=anta$Anta$安踏&bounds=28.960060, 106.338580,30.184953, 107.502572&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20'
,'http://api.map.baidu.com/place/v2/search?query=anta$Anta$安踏&bounds=22.354956, 112.949903,23.662326, 114.837248&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20'
,'http://api.map.baidu.com/place/v2/search?query=anta$Anta$安踏&bounds=29.627369, 102.932519,31.427493, 105.522617&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20'
,'http://api.map.baidu.com/place/v2/search?query=anta$Anta$安踏&bounds=31.570596, 116.850783,32.948990, 119.741461&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20'
]


filename = "Anta-s-frombaidu-jingweidu" + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.csv'
# 新建文件
f = open(filename, 'w', encoding='utf-8')
# 写入title
f.write('name,location,address,province,address,city,area,telephone,detail,uid,detail_info' + '\n')
# 打开citylist 遍历每个城市
for u in url:
    html = requests.get(u).text
    # json化 数据
    html = json.loads(html)
    print(html)
    # 获取最大的数量
    if html['total'] != 0:
        pages = int(html['total']) // 60 + 1
        print(html['total'])
        # 翻页
        for p in range(pages):
            print(p)
            # 根据城市和页数拼接新的url,下载数据
            sleep(8)
            html_s = requests.get(u+"&page_num="+str(p)).text
            # json 化数据
            html_s = json.loads(html_s)
            # 获取 store的数据，遍历每条store数据
            for store in html_s['results']:
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









