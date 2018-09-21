"""
Author : Lily
Data : 2018-09-18
QQ : 339600718
科颜氏 Kiehl's Kiehls-s
抓取思路：微信公众号，拿到province的id,做为参数，请求city的id,根据cityid请求stores的数据
getProvince（post,json）:http://wx.kiehls.com.cn/KStart/GetProvince
getCity（post,json,参数：proId）:http://wx.kiehls.com.cn/KStart/GetCity
getStore（post,json，参数：city_id: 37,longitude: ,latitude: ）:http://wx.kiehls.com.cn/Shoppe/GetShopList
注意：在浏览器打不开，会提示---Server Error in '/' Application.


"""

import requests
import re
import datetime
import json


filename = "Kiehls-s" + re.sub('[^0-9]','',str(datetime.datetime.now())) + ".csv"
f = open(filename, 'w', encoding='utf-8')
f.write('StoreId,WebChatId,Content,Name,Country,Code,state,BusinessTime,Map,thumb,Address,Phone,City,Dist,Province,Lng,Number,Lat,Price,Recommended,Characteristic,Introduction,BranchName,category,product1,product2,product3,url,PanoramaUrl,ComplexDefualts,PassWord,CounterMobile,TrailId,FailedPasswordCount,LastLoginTime,\n')
pro_url = 'http://wx.kiehls.com.cn/KStart/GetProvince'
city_url = 'http://wx.kiehls.com.cn/KStart/GetCity'
store_url = 'http://wx.kiehls.com.cn/Shoppe/GetShopList'
provinces = requests.post(pro_url).text
provinces_json = json.loads(provinces)
for pro in provinces_json:
    print(pro)
    data = {"proId":pro["AreaId"]}
    citys = requests.post(city_url, data=data).text
    print(citys)
    citys_json = json.loads(citys)
    for ct in citys_json:
        print(ct)
        cityname = ct['AreaName']
        cityid = ct["AreaId"]
        store_data = {"city_id": cityid, "longitude": "", "latitude": ""}
        stores = requests.post(store_url, data=store_data).text
        stores_json = json.loads(stores)
        for store in stores_json["shopperList"]:
            print(store)
            for s_k, s_v in store.items():
                v = str(s_v).replace(',', '，').replace('\n', '').replace('\r','')
                f.write(v + ",")
            f.write('\n')
f.close()
