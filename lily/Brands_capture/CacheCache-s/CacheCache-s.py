"""
Author : Lily
Data : 2018-09-19
QQ : 339600718
Cache Cache Cache Cache CacheCache-s
抓取思路： 在主页上抓取每个省份的id,作为参数提交请求，获取城市信息的cityPK,用cityPK做为参数请求具体的数据信息
index_url : http://www.cache-cache.cn/store-finder
city_url(get,json) : http://www.cache-cache.cn/store-finder/getCitiesStoresByRegion?isocode=CN-31
stores_url (get,json): http://www.cache-cache.cn/store-finder/getStoresByCity?cityId=8796095424073

"""
import re
import requests
import datetime
import json
from lxml import etree


filename = "CacheCache-s" + re.sub('[^0-9]', '', str(datetime.datetime.now())) + ".csv"
f = open(filename, 'w', encoding='utf-8')
f.write('lastNamprovince, country, city, companyName, postalCode, '
        'cityData, title, titleCode, formattedAddress, visibleInAddressBook, cellphone, cityDistrictData, id, line2, line1, email, town, landlinePhonePart1, cityDistrict, firstName, phone, landlinePhonePart2, shippingAddress, landlinePhonePart3, billingAddress, region, remarks, defaultAddress,\n')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
index_url = "http://www.cache-cache.cn/store-finder"
city_url = 'http://www.cache-cache.cn/store-finder/getCitiesStoresByRegion?isocode='
store_url = "http://www.cache-cache.cn/store-finder/getStoresByCity?cityId="
index_html = requests.get(index_url, headers=headers).text
index_lxml = etree.HTML(index_html)
provinces = index_lxml.xpath('//*[@id="storeFinder"]/div[1]/div/div/div/div[1]/ul/li')
print(len(provinces))
for pro in provinces:

    pro_id = pro.xpath('./@id')[0]
    pro_count = pro.xpath('./@storecount')
    pro_name = pro.xpath('./a/text()')
    print(pro_name)
    citys_json = requests.get(city_url+pro_id, headers=headers).text
    citys_json = json.loads(citys_json)

    for city in citys_json:
        print(city)
        city_id = city["cityPK"]
        city_name = city["cityName"]
        city_count = city["storeCount"]
        store_json = requests.get(store_url+str(city_id), headers=headers).text
        store_json = json.loads(store_json)

        for store in store_json:
            for k, v in store["address"].items():
                v = str(v).replace(',', '，').replace('\n', '')
                f.write(v + ',')
            f.write('\n')
f.close()


