"""
Author : Lily
Date : 2018-09-18
QQ : 339600718
鸥美药妆 OMEY Omey-s
抓取思路：抓取后台json数据，先抓取城市列表，用城市列表做为参数，请求区列表，再用区做为参数，请求具体的store数据
citylist_url(json): http://omeyweixin.jemy.com/addon/Scratch/Store/get_Citys?jsonp=jQuery111109317909866618594_1537254590861&_=1537254590863
district_url(json): http://omeyweixin.jemy.com/addon/Scratch/Store/get_dict?jsonp=jQuery111109317909866618594_1537254590861&city=上海&_=1537254590864
stores_url(json): http://omeyweixin.jemy.com/addon/Scratch/Store/get_store?jsonp=jQuery111109317909866618594_1537254590861&dict=黄浦区&_=1537254590865
注意：得到的json有头：jQuery111109317909866618594_1537254590861(）需要去掉，不知道下次还是不是一样的头。
      抓取了几次，官网就就崩溃了。
"""
import requests
import re
import datetime
import json


filenam = "Omey-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"
f = open(filenam, 'w', encoding='utf-8')
f.write("shop_business_starttime,shop_business_endtime,org_code,city,lon,lat,org_id,fullname,shortname,address,telephone,\n")

city_url = 'http://omeyweixin.jemy.com/addon/Scratch/Store/get_Citys?jsonp=jQuery111109317909866618594_1537254590861&_=1537254590863'
district_url = 'http://omeyweixin.jemy.com/addon/Scratch/Store/get_dict?jsonp=jQuery111109317909866618594_1537254590861&_=1537254590864&city='
store_url = 'http://omeyweixin.jemy.com/addon/Scratch/Store/get_store?jsonp=jQuery111109317909866618594_1537254590861&_=1537254590865&dict='
citylist = requests.get(city_url).text
citys_json = citylist.replace('jQuery111109317909866618594_1537254590861(', '')
citys_json = citys_json.replace(')', '')
citys = json.loads(citys_json)
print(citys)
for ci in citys['data']:
    for c_k, c_v in ci.items():
        districtlist = requests.get(district_url + c_v).text
        districts_json = districtlist.replace('jQuery111109317909866618594_1537254590861(','')
        districts_json = districts_json.replace(')', '')
        districts = json.loads(districts_json)
        for district in districts['dictdata']:
            for d_k, d_v in district.items():
                storelist = requests.get(store_url+d_v).text
                store_json = storelist.replace('jQuery111109317909866618594_1537254590861(', '')
                store_json = store_json.replace(')', '')
                stores = json.loads(store_json)
                for store in stores['storedata']:
                    for s_k, s_v in store.items():
                        s_v = str(s_v).replace(',', '，').replace('\n', ' ')
                        f.write(s_v + ',')
                    f.write('\n')
f.close()