import urllib.request
import json

def download5(url, free_proxy=None, user_agent='test', num_retries=2, data=None):
    # print("download5...", url)
    # 设置headers 中的用户代理，默认值是test
    headers = {"User_agent": user_agent}
    # 将用户代理添加到请求中
    request = urllib.request.Request(url, data, headers=headers)
    # 创建句柄
    opener = urllib.request.build_opener()
    # 判断如果proxy是否有值
    if free_proxy:
        # 获取ip代理协议和IP代理
        proxy_params = {urllib.request.urlparse(url).scheme: free_proxy}
        # 将IP代理设置添加到句柄中
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        # 使用句柄的open()打开网页，read()读取内容
        html5 = opener.open(request).read()
    # 异常处理，捕获异常
    except urllib.request.URLError as e:
        # 打印异常原因
        print("download error", e.reason)
        html5 = None
        # 判断重新加载次数是否大于0
        if num_retries > 0:
            # 判断 页面code是否在500和600之间
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 调用自身
                html5 = download5(url, free_proxy, user_agent, num_retries - 1)
    return html5.decode('utf-8')
urls =['https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=116.391532&latitude=39.907641&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=117.191066&latitude=39.118407&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=115.459253&latitude=38.873365&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=112.54089&latitude=37.870445&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=119.737339&latitude=49.212554&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=123.427379&latitude=41.801623&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=125.3111&latitude=43.884061&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=126.637209&latitude=45.755032&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=121.469022&latitude=31.232232&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=120.596908&latitude=31.311158&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=120.159269&latitude=30.266643&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=117.278801&latitude=31.860845&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=119.308358&latitude=26.073192&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=115.886836&latitude=28.675227&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=117.023644&latitude=36.659707&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=113.619357&latitude=34.748301&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=114.295535&latitude=30.598321&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=113.007656&latitude=28.184007&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=113.259021&latitude=23.13177&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=108.361811&latitude=22.819923&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=110.344328&latitude=20.021178&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=106.546877&latitude=29.567788&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=104.063968&latitude=30.574667&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=106.626633&latitude=26.651248&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=102.831592&latitude=24.882091&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=91.170532&latitude=29.655196&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=108.940344&latitude=34.262324&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=103.831716&latitude=36.061316&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=101.776087&latitude=36.617233&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=106.226243&latitude=38.486785&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=',
'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=87.613857&latitude=43.824446&count=10000&brandCode=RE&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser=']

f = open("Replay-s171121.csv", "w+", encoding="utf-8")

# url = 'https://wx.qxclub.cn/wcap/nearby_shop_controller/queryNearestShop.do?1=1&longitude=113.670492&latitude=34.648754&count=1000&brandCode=BL&openID=oZi76jt-fusXm4BOSA23D1BenlhI&currentUser= '


t = 0
tittle = []
sid = []
for url in urls:
    html = download5(url)
    html = json.loads(html)
    for i in html:

        print(i['shop'])
        if t == 0:
            for k, v in i['shop'].items():
                tittle.append(k)
                f.write(k)
                f.write(',')
                t = t + 1
            f.write('\n')
        if i['shop']['shopStoreId'] not in sid:
            print(sid)
            print(i['shop']['shopStoreId'])
            sid.append(i['shop']['shopStoreId'])
            for j in range(len(tittle)):
                if tittle[j] in i['shop'].keys():
                    v = i['shop'][tittle[j]]
                    v = str(v).replace(',', '，')
                    v = str(v).replace('\n', ' ')
                    f.write(v)
                    f.write(',')
                else:
                    f.write(' ')
                    f.write(',')
            f.write('\n')
f.close()



