# '''
# \d     可以匹配一个数字
# \w     可以匹配一个字母
# .      可以匹配任何字符
# *      表示任意个字符
# +      表示至少一个字符
# ？     表示1个或者0个字符
# {n}    表示n个字符
# {n,m}  表示n-m个字符
# \s     表示一个空格
# 如果出现特殊字符需要用 \ 进行转义
# 如-  在正则表达式中表示为\-
# '''
# '''
# 例子：
# \d{3}\s+\d{3,8}
# \d{3}表示匹配3个数字，例如'010'；
# \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
# \d{3,8}表示3-8个数字，例如'1234567'
# '''
#
# '''
# 要做更精确地匹配，可以用[]表示范围,比如：
#     [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
#     [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
#     [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
#     [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
# '''
# import re
# test = '65465sa645fd'
# if re.match(r'\d{3}\s+\d{3,8}', test):   # match()方法判断是否匹配
#     print('ok')
# else:
#     print('failed')
#
# # 切分字符串
# a = re.split(r'\s+', 'a b   c')
# b = 'a b   c'.split(' ')   # 无法识别连续的空格
# print(a, b)
#
# # 用()表示的就是要提取的分组（Group）
# # ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# # 正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来
# print(m, '\n', m.group(0), '\n', m.group(1), '\n', m.group(2))
#
# # 可以用re.compile()去编译正则表达式，那么接下来我们就可以重复使用时就不需要编译这个步骤了
#
#
# # datetime
# # 是python处理时间的标准库
# from datetime import datetime
# # 获取系统时间
# now = datetime.now()   # 返回的类型是datetime
#
# # 获取指定日期和时间
# dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
#
# # datetime转换为timestamp
# dt.timestamp() # 把datetime转换为timestamp
# # Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数
#
# # timestamp 转换为 datetime
# t = 1429417200.0
# datetime.fromtimestamp(t)   # 在timestamp和本地时间做转换
# datetime.utcfromtimestamp(t)   # UTC时间
#
# # str转换为datetime
# # '%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# # datetime是没有时区信息的
#
# # datetime转换为str
# now.strftime('%a, %b %d %H:%M')
#
# # datetime加减
# # 加减可以直接用+和-运算符，不过需要导入timedelta这个类
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now, now + timedelta(hours=10), now - timedelta(days=1), now + timedelta(days=2, hours=12))
#
# # 本地时间转换为UTC时间
# # 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
# from datetime import datetime, timedelta, timezone
# tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
# print(datetime.now())
# print(datetime.now().replace(tzinfo=tz_utc_8))   # 强制设置为UTC+8:00
#
# # 时区转换
# # 先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print('当前的UTC时间', utc_dt)
# # astimezone()将转换时区为北京时间:
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print('北京时间：', bj_dt)
#
# '''
# 总结
# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
#
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
# '''
#
# # collections
# # collections是Python内建的一个集合模块，提供了许多有用的集合类
# # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# # 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1,2)
# print(p, p.x, p.y)
#
# '''
# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
# '''
# from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')   # 尾部进行插入
# q.appendleft('y')   # 头部进行插入
# print(q)
#
# # defaultdict
# # 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])   # 不存在key2所以返回一个默认值
#
# # OrderedDict
# # 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# # 如果要保持Key的顺序，可以用OrderedDict
# from collections import OrderedDict
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print('d这个时候时无序的: ', d)
# d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print('d这个时候是有序的： ', d)   # 可以用d.get('a')来获取值
#
# # OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
# from collections import OrderedDict
#
#
# class LastUpdatedOrderedDict(OrderedDict):
#
#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)
#
# # Counter
# # Counter是一个简单的计数器，例如，统计字符出现的个数
# from collections import Counter
# c = Counter()
# for ch in 'hfeikfhae':
#     c[ch] = c[ch] + 1
#
# print(c)
#
# # struct模块来解决bytes和其他二进制数据类型的转换
# # struct的pack函数把任意数据类型变成bytes
# import struct
# print(struct.pack('>I', 1024009999))   # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
#
#
#
#
# import hashlib
#
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print('MD5: ', md5.hexdigest())
#
# sha1 = hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print('shal: ', sha1.hexdigest())
#
#
# '''
# itertools:
#     count()会创建一个无限的迭代器
#     cycle()会把传入的一个序列无限重复下去
#     repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
#     takewhile()等函数根据条件判断来截取出一个有限的序列
#     chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
#     groupby()把迭代器中相邻的重复元素挑出来放在一起
#
# 总结：itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
# '''
#
#
# class Query(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
# with Query('Bob') as q:
#     q.query()
#
#
# # 在某段代码执行前后自动执行特定代码
# # 例子：
# from contextlib import contextmanager
#
#
# @contextmanager    # 简化上下文管理
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)
#
# with tag("h1"):
#     print("hello")
#     print("world")
#
#
# # 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象
# # closing()的实现原理如下：
# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()
#
#
# # 解析XML
# from xml.parsers.expat import ParserCreate
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)
#
# # 解析HTML
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')
#
# # 使用request对一个url抓取其返回的http响应
# from urllib import request
#
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))
#
# # 模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
# from urllib import request
# req = request.Request('http://www.sina.com.cn/')
# # 添加HTTP头
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('status', f.status, f.reason)
#     for k, v in f.getheaders:
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnails.png', 'png')








