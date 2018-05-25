from urllib import parse
urls1 = ['province=上海&city=上海市&district=南汇区&all=Y&page=0&_=1509106871111',
'province=上海&city=上海市&district=卢湾区&all=Y&page=0&_=1509106871111',
'province=上海&city=上海市&district=嘉定区&all=Y&page=0&_=1509106871111',
'province=上海&city=上海市&district=奉贤区&all=Y&page=0&_=1509106871111',
'province=上海&city=上海市&district=宝山区&all=Y&page=0&_=1509106871111'
]
#中文转URL编码
# with open('url.txt','a') as f:
#     for url in urls1:
#         new = parse.quote(url)
#         f.write(new)
#         f.write('\n')

#URL编码转中文
urls2 = ['province=%E4%B8%8A%E6%B5%B7&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&district=%E5%8D%97%E6%B1%87%E5%8C%BA&all=Y&page=0&_=1509106871111',
'province=%E4%B8%8A%E6%B5%B7&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&district=%E5%8D%97%E6%B1%87%E5%8C%BA&all=Y&page=0&_=1509106871111',
'province=%E4%B8%8A%E6%B5%B7&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&district=%E5%8D%A2%E6%B9%BE%E5%8C%BA&all=Y&page=0&_=1509106871111',
'province=%E4%B8%8A%E6%B5%B7&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&district=%E5%98%89%E5%AE%9A%E5%8C%BA&all=Y&page=0&_=1509106871111',
'province=%E4%B8%8A%E6%B5%B7&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&district=%E5%98%89%E5%AE%9A%E5%8C%BA&all=Y&page=0&_=1509106871111'

]
with open('url.txt','a') as f:
    for url in urls2:
        new = parse.unquote(url)
        f.write(new)
        f.write('\n')
