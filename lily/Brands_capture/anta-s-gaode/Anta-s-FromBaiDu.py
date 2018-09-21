
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
# header = {
#
#     "Cookies":"BAIDUID=C5A274FB331F281CE852C09D57F43A3B:FG=1; BIDUPSID=C5A274FB331F281CE852C09D57F43A3B; PSTM=1512100937; BDUSS=5CYlhSeWVaR1p3b1VuWDY4bkJBZzllU0p1dmpsRVNRc1Z4RTdUTEU1THJlMjFhQVFBQUFBJCQAAAAAAAAAAAEAAAD6zIeSAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOvuRVrr7kVaM2; __cfduid=d367b743d8f76522f157a9d1f4985dc631534383860; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[08EbrmKd5E_]=aeXf-1x8UdYcs; H_PS_PSSID=1469_21090; PSINO=7; MCITY=-131%3A340%3A"
#     ,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
# }
# URL 的第一部分
url = 'http://api.map.baidu.com/place/v2/search?query=Anta&output=json&ak=aRsmdt7rLKFwSaOf6lI6iHGBVyyRvZyd&scope=2&page_size=20&region='
# URL第二部分
url_page = '&page_num='
# 文件名按照sku+时间命名
filename = "Anta-s-frombaidu" + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.csv'
# 新建文件
f = open(filename, 'w', encoding='utf-8')
# 写入title
f.write('name,location,address,province,city,distict,area,telephone,detail,uid,detail_info' + '\n')
# 打开citylist 遍历每个城市
with open('citys.csv', 'r', encoding='utf-8') as csvfile:
    # 读取city文件
    reader = csv.reader(csvfile)
    # 遍历每个城市
    for row in reader:
        # 获取城市
        city = str(row[0])
        # 先进入初始网址，拿到最大的数量
        html = requests.get(url+city+url_page+str(0), ).text
        # json化 数据
        html = json.loads(html)

        # 获取最大的数量
        if html['total'] != 0:
            pages = int(html['total']) // 20 + 1
            print(html['total'])
            # 翻页
            for p in range(pages):
                print(p)
                # 根据城市和页数拼接新的url,下载数据
                sleep(8)
                html_s = requests.get(url+city+url_page+str(p)).text
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









