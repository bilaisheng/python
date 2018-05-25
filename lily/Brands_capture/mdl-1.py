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

latlon = []
name = []
address = []
csv_file = csv.reader(open('mdl-latlonlist.csv', 'r', encoding='utf-8'))
for stu in csv_file:
    latlon.append(stu)
f = open('mdl171124.csv', "w", encoding="utf-8")
try:
    for lg in range(len(latlon)):
        sleep(5)
        response = requests.post(url, data={'point': latlon[lg]}, verify=False)
        sleep(5)
        print(response.text)
        data = json.loads(response.text)
        print(data)
        s = data['datas']
        print(s)
        print(type(s))
        print(len(s))

        if s != 0:
            for i in s:
                f.write('sellatlon')
                f.write(',')
                for k, v in i.items():
                    f.write(k)
                    f.write(',')
                    print(k)
                    print(v)
                f.write('\n')
                break

            for i in s:
                sellatlon = str(latlon[lg]).replace(',', '，')
                f.write(sellatlon)
                f.write(',')
                for k, v in i.items():

                    v = str(v).replace(',', '，')
                    f.write(v)
                    f.write(',')

                f.write('\n')
    f.close()
except:
    print('error')

