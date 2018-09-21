"""
author: Lily
date ： 2018-08-28
QQ : 339600718

雅莹 EP ElegantPro-s
抓取思路：现在city的页面把city list 抓下来，再用city为参数，请求store的具体数据
注意：1.抓取的时候需要传递cookies,每次抓取都需要获取新的cookies 替换旧的cookies,否则报错
      2.地址中有空格，需要替换掉，否则会错列
"""
import json
import requests
from bs4 import BeautifulSoup
import datetime
import re


# header 一定要有cookie,没有的话报错404
header = {"Accept-Language": "zh-CN,en-US;q=0.8",
          "Cookie": "ASP.NET_SessionId=kyq2vbv5jm05z1dp3oxdz5ph;Hm_lpvt_10d048cdc0c87908b7ddf69b78c3e284=1535600227;"
                    "Hm_lpvt_10d048cdc0c87908b7ddf69b78c3e284=1535600227",
          "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN"}
# 获取每个store具体信息的链接
url_store = 'http://o2o.elegant-prosper.com/EPWXSiteNew/ShopInfo/GetCityByLatLonJSON?sid=cfe404ea-fe5b-4a85-87f0-b2701929462c&oid=oBf_qJei0dv_nfb8qvrF0f7x-xGw'
# 获取所有城市的链接
url_city = "http://o2o.elegant-prosper.com/EPWXSiteNew/ShopInfo/GetProvinceCity"
# 获取store具体信息时所提交的参数
data_store = {"strLatitude": 30.7509120000,
              "strLongitude": 120.7620450000}
# 获取所有城市时所提交的参数
data_city = {"sid": "cfe404ea-fe5b-4a85-87f0-b2701929462c",
             "oid": "oBf_qJei0dv_nfb8qvrF0f7x-xGw",
             "strLatitude": "30.750912",
             "strLongitude": "120.762045",
             "strCity": "%E5%98%89%E5%85%B4%E5%B8%82"}
# 创建城市list,接下来把城市列表存储到其中
citys = []


# post 请求一个页面的方法
def download(url, data, headers):
    html = requests.post(url=url, data=data, headers=headers)
    html = html.text
    print(html)
    return html


# 获取城市列表
def get_citys():
    # 下载城市页面
    html = download(url_city, data_city, header)
    # 使用BeautifulSoup解析页面
    soup = BeautifulSoup(html, 'lxml')
    # 遍历 子节点
    for i, child in enumerate(soup.div.children):
        # 找到所要的第三个子节点  备注：其实只有2个子节点，但是不知道为什么0和2是空的，可能是换行也算一个子
        if i == 3:
            # 遍历所有子节点，拿到城市列表
            for j, c in enumerate(child.children):
                # 换行可能也是一个子，排除掉换行
                if c != "\n":
                    # 收集城市
                    citys.append(c.string)


# 写入文件
def write_store():
    # sku+时间戳命名文件
    filename = "ElegantPro-s" + re.sub(r'[^0-9]', '', str(datetime.datetime.now()))+'.csv'
    # 创建文件
    f = open(filename, 'w', encoding='utf-8')
    # 写title
    f.write("j_depotid,j_name,g_address,m_shoptel,Distance,latitude,longitude"+"\n")
    # 获取具体store信息
    for ci in citys:
        # 将city的值添加到参数中
        data_store["strCity"] = ci
        # 下载改城市的数据页面
        store = download(url_store, data_store, header)
        # 将数据json化
        print(store)
        print(type(store))

        print(store[0])
        store = json.loads(store)

        print(store[0])
        print(store)
        print(type(store))
        # 将数据转成list
        store = eval(store)
        print(store)
        print(type(store))
        # 遍历每条数据
        for s in store:
            # 遍历每条数据的键值对
            for k, v in s.items():
                # 将值写入到文件中
                v = str(v).replace(",", "")
                f.write(v+",")
            # 写完一条数据后换行
            f.write('\n')
    # 关闭文件
    f.close()


# 获取城市列表
get_citys()
# 将数据写入CSV
write_store()

