import urllib.request
import json
from urllib import parse


def download5(url, free_proxy=None, user_agent='test', num_retries=2, data=None):
    # print("download5...", url)
    # 设置headers 中的用户代理，默认值是test
    headers = {"User_agent": "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255"}
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
    return html5
html = download5("http://wx.sephora.cn/index.php?m=Nearby&a=index&provinceid=6&cityid=76")
print(html)
# province =['http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=北京市&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=天津市&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=河北省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=山西省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=内蒙古自治区&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=辽宁省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=吉林省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=黑龙江省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=上海市&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=江苏省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=浙江省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=安徽省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=福建省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=江西省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=山东省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=河南省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=湖北省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=湖南省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=广东省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=广西壮族自治区&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=海南省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=重庆市&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=四川省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=贵州省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=云南省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=西藏自治区&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=陕西省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=甘肃省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=青海省&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=宁夏回族自治区&city=&_=1516174273975',
# 'http://location.chcedo.com/interface/index.php?c=api&m=get_store_list&callback=jQuery110109367562047222278_1516174273973&province=新疆维吾尔自治区&city=&_=1516174273975'
# ]
# f = open('Chando-s180117.csv', "w+", encoding="utf-8")
# try:
#     for url in province:
#         url = parse.quote(url, safe='/:?=&_.')
#         html = download5(url)
#         html=str(html).replace('jQuery110109367562047222278_1516174273973(','')
#         html =str(html).replace(')', '')
#         data = json.loads(html)
#         re = data["data"]["store_list"]
#         print(html)
#
#         for store in re:
#             for k, v in store.items():
#                 f.write(v)
#                 f.write(',')
#             f.write('\n')
#     f.close()
# except:
#     print('erro')
