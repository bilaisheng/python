"""
author: Lily
date ： 2018-08-29
QQ : 339600718

冰雪皇后 Dairy Queen DairyQueen-s
抓取思路：改变参数（城市，关键字）获取不同城市的数据,各种关键字搜索的结果不一样，最后需要去重复
注意：1.有些城市是没有数据，是空，例如北京没有数据，但北京是有很多店的，官网数据不全
      2.输入的城市和关键字是省份的话也可以抓到数据，但是不全
      3.关键字不通，搜到的数据不一样，city=上海市时，关键字用上海市只搜出来27家，但是用上海搜出来51家。
      4.需要用其他不同的关键字搜索，比如："路"，"号"，"店"，" 区"
"""
import requests
import json
import csv
import datetime
import re


# post 请求一个网页的方法
def download(url, data, headers=None):
    html = requests.post(url=url, data=data, headers=headers, verify=False)
    html = html.text
    return html
# 用Fiddler检测到的headers
header = {
          "Accept-Encoding": "gzip",
          "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x26070237) NetType/WIFI Language/zh_CN"
}
# 用fiddler检测到的url
url = "http://www.dairyqueen.com.cn/store.php?action=search"
# 用于查询的关键字
keyword = ["路", "号", "店", "区"]
# 为了查重，将店名存储于name
name = []
# 为了查重，将地址存储于address
address = []
# sku+时间戳命名文件
filename = "DairyQueen-s"+ re.sub(r'[^0-9]', '', str(datetime.datetime.now()))+'.csv'
# 创建文件，准备写入数据
f = open(filename, 'w', encoding='utf-8')
f.write("name,address,lat,lng"+"\n")
# 打开citys文件，准备读取city list
with open('citys.csv', 'r', encoding='utf-8') as csvfile:
    # 获取citys文件内容
    reader = csv.reader(csvfile)
    # 按行读取citys文件
    for row in reader:
        # 由于每行是一个list,第一列就是list[0],取到citys的第一列的具体值
        city = str(row[0])
        # 关键字里面加上城市的前两个字
        keyword.append(city[:2])
        # 便利每个关键字查询
        for kw in keyword:
            # 提交的参数
            data = {"q": kw, "city_name": city}
            # 加载数据页面
            html = download(url, data, header)
            # 将数据json化
            store = json.loads(html)
            # 为了防止程序异常停止，使用try...except...
            try:
                # 有些城市没有数据，根据lists判断，如果有lists才会继续抓取
                if store["lists"]:
                    # 遍历lists里面的每一条store
                    for s in store["lists"]:
                        # 判断重复，如果店面和地址都已经抓过了，就不再抓取
                        if s["name"] not in name or s["address"] not in address:
                            # 遍历每条数据的每个属性
                            for k, v in s.items():
                                # 写入每个值
                                print(k ,v)
                                f.write(v + ",")
                                # 将写过的name 添加到name 数组里
                                if k == "name":
                                    name.append(v)
                                # 将写过的Address添加到address数组里
                                if k == "address":
                                    address.append(v)
                            # 写完一条数据后换行
                            f.write('\n')
            except:
                # 出现异常时输出“无数据”
                print("无数据")
        # 将用过的city参数清除，待查询下一个城市使用
        keyword.remove(city[:2])
# 关闭文件
f.close()



