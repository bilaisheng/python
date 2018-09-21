"""
Author : Lily
Date : 2018-09-20
QQ : 339600718
PULL&BEAR PULL&BEAR PullBear-s
抓取思路：所有数据都在一个主页面上，解析页面上的数据即可。
注意： 所有的数据都在p标签里。
URL:https://mp.weixin.qq.com/s/aj7UPr9l9qnnhB_mDTHUIw

注意
"""
import re
import datetime
import requests
from lxml import etree


filename = "PullBear-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"
f = open(filename, 'w', encoding='utf-8')
f.write('name,address,phone,\n')
url = "https://mp.weixin.qq.com/s/aj7UPr9l9qnnhB_mDTHUIw"
html = requests.get(url).text
html_lxml = etree.HTML(html)
addresss = html_lxml.xpath('//*[@id="js_content"]/section/section/section/section/p//text()')

print(addresss)
print(len(addresss))
for i in range(len(addresss)):

    if "地址" in addresss[i]:
        name = addresss[i-1]
        address = addresss[i].replace('地址：', '')
        if "电话："== addresss[i+1]:
            phone = addresss[i + 2]
            print(addresss[i + 2])
        else:
            phone = addresss[i+1].replace('电话：', '')

        f.write(name + "," + address + "," + phone + "\n")

