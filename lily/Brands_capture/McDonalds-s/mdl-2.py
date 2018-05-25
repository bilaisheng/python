import requests
import json
import csv
from time import sleep

url = "https://www.mcdonalds.com.cn/ajaxs/search_by_point"

headers = {
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate,br'
}

lat_lon = []
name = []
address = []
csv_file = csv.reader(open('mdl-latlonlist.csv', 'r', encoding='utf-8'))
for stu in csv_file:
    lat_lon.append(stu)
print(len(lat_lon))
f = open('McDonalds-s180321-2.csv', "w", encoding="utf-8")
try:
    for lg in range(len(lat_lon)):
        response = requests.post(url, data={'point': lat_lon[lg]}, verify=False)
        sleep(2)
        data = json.loads(response.text)
        print(data)
        s = data['datas']
        print(s)
        print(type(s))
        print(len(s))

        if len(s) != 0:
            for i in s:
                f.write('sellatlon')
                f.write(',')
                for k in i.keys():
                    f.write(k)
                    f.write(',')
                f.write('\n')
                break

            for i in s:
                # if (i['_name'] not in name) or (i['_address'] not in address):
                sellatlon = str(lat_lon[lg]).replace(',', '，')
                f.write(sellatlon)
                f.write(',')
                # name.append(i['_name'])
                # address.append(i['_address'])
                for k, v in i.items():
                    v = str(v).replace(',', '，')
                    f.write(v)
                    f.write(',')
                f.write('\n')

    f.close()

except:
    print('error')
