import json
import urllib.request
import urllib.parse
from urllib.parse import quote
url = 'http://guerlainwechat.h5po.com/Front/Counter/List.aspx'

citys = ['上海',
'大连',
'广州',
'乌鲁木齐',
'天津',
'太原',
'无锡',
'长沙',
'长春',
'东营',
'兰州',
'包头',
'北京',
'宁波',
'石家庄',
'合肥',
'吉林',
'成都',
'西宁',
'西安',
'沈阳',
'苏州',
'呼和浩特',
'宜昌',
'昆明',
'杭州',
'武汉',
'郑州',
'青岛',
'保定',
'南宁',
'南京',
'南昌',
'南通',
'哈尔滨',
'洛阳',
'济宁',
'济南',
'贵阳',
'重庆',
'唐山',
'徐州',
'株洲',
'烟台',
'常州',
'淄博',
'淮安',
'深圳',
'银川',
'厦门',
'温州',
'福州',
'鞍山']


f = open('Guerlain-s180619.csv', "w+", encoding="utf-8")
# f.write("id,brand,store_id,sn,store_name,description,hours,province,city,district,address,lng,lat,tel,status,ext,create_time,update_time\n")

for city in citys:
    city = quote(city)
    parameter = '{"action":"getList","city":"'+city+'"}'

    print(parameter)
    p_to_request = urllib.parse.urlencode(json.loads(parameter)).encode('utf-8')
    request = urllib.request.Request(url, p_to_request)
    html = urllib.request.urlopen(request).read()
    stores = json.loads(html)

    print(type(html))

#     if stores['list']:
#         for store in stores['list']:
#             for k, v in store.items():
#                 print(k, v)
#                 v = str(v).replace(',', '，')
#                 f.write(str(v))
#                 f.write(',')
#             f.write('\n')
# f.close()
