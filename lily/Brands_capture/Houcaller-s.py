#!/usr/bin/python3
# Filename : Houcaller-s.py
# Author by : Lily
"""
locator：http://www.houcaller.com/hklhome/crm/searchorg.jspx
storeID:http://www.houcaller.com/hklhome/crm/getOrgs.jspx?province=%E7%A6%8F%E5%BB%BA
storeInformation:http://www.houcaller.com/hklhome/crm/getOrg.jspx?orgCode=0106
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
locator = getHtml("http://www.houcaller.com/hklhome/crm/searchorg.jspx")
#在页面中找到省份的下拉列表，并获取省份
soup = BeautifulSoup(locator,'html.parser')
pro_sel = soup.find('select',attrs={'name':'province'})
op = pro_sel.find_all('option')
pro = re.findall('value="(.*?)">',str(op))

store_ids = []
tittle = []
n=0
f = codecs.open('haokelai.csv','w','utf-8')
# 根据获取的省份作为get参数，打开省份页面，获取store id的信息
for s_id in pro:
    url_pro ="http://www.houcaller.com/hklhome/crm/getOrgs.jspx?province="+ urllib.request.quote(s_id)
    pro_content = getHtml(url_pro)
    store_id = re.findall('value="(.*?)"',str(pro_content))
    store_ids += store_id

# 根据store id作为参数，打开每个store的具体信息页面，获取具体信息
for st_i in store_ids:
    url_store = "http://www.houcaller.com/hklhome/crm/getOrg.jspx?orgCode="+st_i
    store_content = getHtml(url_store)
    st_json = json.loads(store_content)
    # 获取tittle并写入
    if n == 0:
        for k,v in st_json.items():
            print(k)
            tittle.append(k)
        for t in tittle:
            f.write('%s,'%t)
        f.write('\n')
        n=n+1
    address=st_json['address']
    f.csv.writer(f,dialect = ('excel').writerow(['address']))

#
# """
#     #获取键值并写入,方法一
#     for k, v in st_json.items():
#         f.write('%s,'%str(v).replace(',','，'))
#     f.write('\n')
# """



