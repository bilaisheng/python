"""
author: Lily
date: 2018-08-30
QQ:339600718
亦谷 yigue YiGue-s
抓取思路：点开附件门店就获取到附近的10家门店，继续向上划就能获取全部的数据
         每页显示10个，需要翻页抓取。

"""
import requests
import re
import json
import datetime


# sku+时间戳命名文件，方便以后再次运行
filename = "YiGue-s" + re.sub(r'[^0-9]', '', str(datetime.datetime.now()))+".csv"
# 创建文件，待将数据写入
f = open(filename, 'w', encoding='utf-8')
# 将title写入
f.write('shop_id,shop_code,avg_score,distance,lng,lat,shop_pic,shop_sign_cnt,shop_name,shop_type,'
        'comtact,address,tel,mobile,is_gift,lngb,latb'+"\n")
# 页面参数，从fiddler得到一共有几页，参数都是哪些
datas = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
# 加载首页的数据，即附近的数据
html_page1 = requests.get('http://h.qizhuyun.com/d729112372/shop/get_new_list?shop_city'
                          '=&lat=22.537135143475&lng=114.03112403466')
# 数据json化
store_page1 = json.loads(html_page1.text)
# 遍历每条数据
for store in store_page1:
    # 遍历每条数据的每个属性
    for k, v in store.items():
        # 将英文逗号替换掉
        v = str(v).replace(',', '')
        # 写入每个值
        f.write(v+',')
    # 写完一条数据后换行
    f.write('\n')
# 遍历每一页的需要提交的参数
for da in datas:
    # 参数构成
    data = {"page": da}
    # 加载页面
    html_more = requests.post("http://h.qizhuyun.com/d729112372/shop/get_list?shop_city=&lat="
                              "22.537135143475&lng=114.03112403466", data)
    # 数据json化
    store_more = json.loads(html_more.text)
    # 遍历每条数据
    for store in store_more:
        # 遍历每条数据的每个属性
        for i, j in store.items():
            # 将英文字符替换掉
            j = str(j).replace(',', '')
            # 写入值
            f.write(j+",")
        # 写完一条数据后换行
        f.write('\n')
# 关闭文件
f.close()
