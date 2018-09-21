# -*- coding: utf-8 -*-
"""
Author: Lily
Date: 2018-09-13
QQ: 339600718
中影国际影城 China Film ChinaFilm-s
抓取思路：在首页获取每个城市的code,根据获取到的code做为参数，获取每个城市的具体数据
URL（获取城市的code）:http://m.cfc.com.cn/?code=031GOyP82mrnFE0LmeP82CuyP82GOyPv&state=123
URL(每个城市的数据)http://m.cfc.com.cn/cinema/index.html?cityCode=320100
注意：抓取到的数据有不同的影院，有些不是中影国际影城，可能是院线。
"""
import requests
from bs4 import BeautifulSoup
import re
import datetime
from lxml import etree
from time import sleep
header = {

'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8'
   , 'Cookie':'BIGipServerm.cfc.com.cn-h5=1348774080.20480.0000; JSESSIONID=6B0CFFE09DEC7F2BD4D95FD53F19CEBD; testKey=oEa9M02mmiTZhvlNUTJtQdAVkxBs; _openId_=oEa9M02mmiTZhvlNUTJtQdAVkxBs; _userId_=675331027835308568; _mobile_=; _user_outSystem_key_=97828efb5d20c1c3cec20eda1e5d42e5; Hm_lvt_917df978a7e1880491a42d7fddf13ae8=1536804691; Hm_lpvt_917df978a7e1880491a42d7fddf13ae8=1536828383'  ,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044207 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/WIFI Language/zh_CN'}
url = 'http://m.cfc.com.cn/?code=031GOyP82mrnFE0LmeP82CuyP82GOyPv&state=123'
url_store = 'http://m.cfc.com.cn/cinema/index.html?cityCode='
city_html = requests.get(url).text

soup_city = BeautifulSoup(city_html,'lxml')

citys = soup_city.find_all(name='tt')
filename = "ChinaFilm-s"+re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.csv'
f = open(filename, 'w', encoding='utf-8')
f.write('citycode,city,name,address,phone'+'\n')
for c in citys:
    print(c)
    city = c.div.string
    citycode = c['cityno']
    print(citycode)
    try:
        store_html = requests.post(url_store+str(citycode), headers=header, verify=False).text
        sleep(5)
        # print(store_html)
        store_html = etree.HTML(store_html)
        # print(type(store_html))
        stores = store_html.xpath('//div[@id="city_hide_flag"]/a')
        # print(stores)
        total = len(stores)
        # print(total)
        for i in range(total):
            # print(i)
            # print('//div[@id="ity_hide_flag"]/a['+str(i+1)+']/div[@class="item"]/div/div/text()')
            name = store_html.xpath('//div[contains(@id,"ity_hide_flag")]/a['+str(i+1)+']/div/div/div/text()')
            address = store_html.xpath('//div[contains(@id,"ity_hide_flag")]/a[' + str(i + 1) + ']/div/p[1]/samp/text()')
            phone = store_html.xpath('//div[contains(@id,"ity_hide_flag")]/a[' + str(i + 1) + ']/div/p[2]/samp/text()')
            # print(name,address,phone)
            f.write(citycode+','+city+','+name[0]+','+address[0]+','+phone[0]+','+'\n')
    except:
        print('无数据')
f.close()
