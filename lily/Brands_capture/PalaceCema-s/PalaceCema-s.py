"""
Author : Lily
Date : 2018-09-18
QQ : 339600718
百丽宫影城 PALACE cinema PalaceCema-s
抓取思路：在主页面获取每个影院的链接，再进入链接获取影院的具体信息
index_url: http://www.b-cinema.cn/home.jsp
注意：网页时而能加载，时而不能，只要多请求几次,需要改善。
"""
from time import sleep
import requests
import re
import datetime
from lxml import etree
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
filename = "PalaceCema-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"
f = open(filename, 'w', encoding='utf-8')
f.write('name,address,goup_phone,news_phone,\n')
index_url = 'http://www.b-cinema.cn/home.jsp'
index_html = requests.get(index_url, headers=headers).text

index_lxml = etree.HTML(index_html)

sum = len(index_lxml.xpath('//table[@class="box"]/tbody/tr/td/table/tbody/tr/td[2]/a/@href'))
address = ''
goup_phone = ''
news_phone = ''
for i in range(sum):
    name = index_lxml.xpath('//table[@class="box"]/tbody/tr/td/table/tbody/tr[' + str(i+1) + ']/td[2]/a/text()')[0]
    store_link = index_lxml.xpath('//table[@class="box"]/tbody/tr/td/table/tbody/tr[' + str(i+1) + ']/td[2]/a/@href')
    sleep(3)
    print(store_link[0])
    if "http://www.b-cinema.cn/" in store_link[0]:
        store_link = store_link[0]
    else:
        store_link = 'http://www.b-cinema.cn/'+store_link[0]
    print(store_link)
    store_html = requests.get(store_link).text
    store_lxml = etree.HTML(store_html)
    store_info = store_lxml.xpath('//*[@id="toubiao"]/table[4]/tbody/tr[2]/td/table[3]/tbody/tr/td[1]/table/tbody/tr/td[strong]//text()')
    sum1 = len(store_info)
    print(sum1)
    for j in range(sum1):
        print(store_info[j])
        if "团体票" in store_info[j]:
            goup_phone = store_info[j+1].replace('：', '')
            print(goup_phone)
        if "影讯" in store_info[j]:
            news_phone = store_info[j+1].replace('：', '')
            print(news_phone)
        if "地址" in store_info[j]:
            address = store_info[j+1].replace('：', '').replace(',','，')
            print(address)
    f.write(name + "," + address + "," + goup_phone + "," + news_phone + "\n")

