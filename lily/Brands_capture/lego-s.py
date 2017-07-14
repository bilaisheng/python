#!/usr/bin/python3
# Filename : Houcaller-s.py
# Author by : Lily
"""
locator：http://www.chinalegoland.com/legomap/index.php?openid=o0TWYswA0c3TB-FGTGATBgNT9bKI&key=LEGO_2016ACT001&sign=5b41fd90a6dadb63360f379374126e1a
storeInformation:http://www.chinalegoland.com/legomap/api/getnearby.php?lng=114.02597366&lat=22.54605355&city=%E5%A4%A7%E8%BF%9E
"""
import time
import urllib.request
import re
from bs4 import BeautifulSoup
import json
import codecs

#定义获取打开链接，获取页面内容的方法
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

# 打开主页面
locator = getHtml("http://www.chinalegoland.com/legomap/index.php?openid=o0TWYswA0c3TB-FGTGATBgNT9bKI&key=LEGO_2016ACT001&sign=5b41fd90a6dadb63360f379374126e1a")
#在页面中找到省份的下拉列表，并获取省份
soup = BeautifulSoup(locator,'html.parser')
pro_sel = soup.find('select',attrs={'id':'city_select'})
op = pro_sel.find_all('option')
pro = re.findall('value="(.*?)">',str(op))


tittle = []
n=0
f = codecs.open('legao-s.csv','w','utf-8')
print(pro)
# 根据store id作为参数，打开每个store的具体信息页面，获取具体信息
for st_i in pro:
    url_store = "http://www.chinalegoland.com/legomap/api/getnearby.php?lng=114.02597366&lat=22.54605355&city=" + urllib.request.quote(st_i)
    st_json = getHtml(url_store)
    s_json = json.loads(st_json)

    for k1, v1 in s_json.items():
        if isinstance(v1, list):
            for s in v1:
                print(s)
                for k in s:
                    if k in tittle:
                        tittle.append(k)
                        print(k)
                # if n == 0:
                #     for k1,v1 in s.items():
                #         tittle.append(k1)
                #         for t in tittle:
                #             f.write('%s,'%t)
                #         f.write('\n')
                #         n=n+1
     # 获取键值并写入,方法一
    # for k, v in s_json.items():
    #     f.write('%s,'%str(v).replace(',','，'))
    # f.write('\n')
    # #
    #
    #
    #
# def muti_json(file_name,json_data):
#     # 打开CSV
#     f = open(file_name,'w',encoding='utf-8')
#     #定义tittle
#     tittle = []
#     # 遍历所有的键值对，取到所有不重复的键（做titlle）
#     for l in json_data:
#         for k in l:
#             if k not in tittle:
#                 tittle.append(k)
#                 print(k)
#     # 把 tittle 写入表格
#     for ti in tittle:
#         f.write(ti)
#         f.write(',')
#     f.write('\n')
#
#     # 初始化data(一条json)
#     data = []
#     for i in range(len(tittle)):
#         data.append(' ')
#     # 遍历每一个键值对，将值写入表格
#     for l in json_data:
#         # 按照titlle的顺序把velue存到data
#         for k, v in l.items():
#             data[tittle.index(k)] = v
#         # 将data写 入表格
#         for da in data:
#             f.write(da)
#             f.write(',')
#         f.write('\n')
#
#         json_data = v
#         muti_json('test3.csv', json_data)