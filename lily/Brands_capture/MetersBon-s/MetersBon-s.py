import urllib.parse
import json
import urllib.request

url = 'https://member.mbgo.com/api/members/nearby'
velues = ['{"lon":"116.386444","lat":"39.912218","brand":"MB"}',
]

f = open('MetersBon-s1.csv', "w+", encoding="utf-8")
for p in velues:
    print(p)
    p1 = json.loads(p)
    store = urllib.parse.urlencode(json.loads(p)).encode('utf-8')
    request1 = urllib.request.Request(url, store)
    html1 = urllib.request.urlopen(request1).read().decode('utf-8')
    stores = json.loads(html1)
    print(stores)
    if stores['message']:
        print(stores)
        for store in stores['message']:
            for k, v in store.items():
                print(k, v)
                v = str(v).replace(',', '，')
                f.write(str(v))
                f.write(',')
            f.write('\n')
f.close()
