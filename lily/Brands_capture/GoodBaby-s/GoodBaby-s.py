"""
Author :Lily
Date : 2018-08-31
QQ : 339600718

好孩子 GoodBaby GoodBaby-s
抓取思路:先获取省份id,再获取城市id,最后获取地区id,根据地区id获取最终的数据
         由于一页只显示10个,获取总数后,修改url参数,获取全部数据

"""
import requests
import json
import datetime
import re


# post 请求一个网页的方法
def download(url, data, headers=None):
    html = requests.post(url=url, data=data, headers=headers,verify=False)
    html = html.text
    return html
headers = {"Accept-Encoding": "gzip",
           "User-Agent": "vivo X7,1080x1920,Android 5.1.1,MamHao V5.2.0 74"}
pro_url = 'https://api.mamahao.com/V1/basic/queryArea.htm'
pro_data = {"type": 1}
store_url = 'https://api.mamahao.com/V3/member/shop/queryMemberShopIndex.htm'
province = download(pro_url, pro_data, headers)
province = json.loads(province)
filename = "GoodBaby-s" + re.sub(r'[^0-9]','', str(datetime.datetime.now())) + ".csv"
f = open(filename, 'w', encoding='utf-8')
for pv in province["data"]:
    for k_p, v_p in pv.items():
        if k_p == "id":
            city_data = {"type": 2, "id": v_p}
            city = download(pro_url, city_data, headers)
            city = json.loads(city)
            print("province" + str(v_p))
            for ct in city["data"]:
                for k_c, v_c in ct.items():
                    if k_c == "id":
                        district_data = {"type": 3, "id": v_c}
                        district = download(pro_url, district_data, headers)
                        district = json.loads(district)
                        print(district["data"])
                        for di in district["data"]:
                            for k_d, v_d in di.items():
                                if k_d == "id":
                                    print("district" + str(v_d))
                                    store_data = {"areaId": v_d, "lng": "116.416357", "lat": 39.928353, "page": 1, "count": 10}
                                    print(store_data)
                                    store = download(store_url, store_data, headers)
                                    store = json.loads(store)
                                    if store["totalRow"] != 0:
                                        count = (store["totalRow"]//10+1)*10
                                        print(store["totalRow"])
                                        n_store_data = {"areaId": v_d, "lng": "116.416357", "lat": 39.928353, "page": 1, "count": count}
                                        stores = download(store_url, n_store_data, headers)
                                        stores = json.loads(stores)
                                        for s in stores["shopList"]:
                                            print(s)
                                            for k_s, v_s in s.items():
                                                v_s = str(v_s).replace(',', '')
                                                f.write(v_s + ',')
                                            f.write('\n')
f.close()





