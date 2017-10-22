"""
常用内建模块
datetime
collections
base64
struct
hashlib
itertools
contextlib
XML
HTMLParser
urllib
常用第三方模块
PIL
"""

from datetime import datetime

# 获取当前日期和时间
now = datetime.now() # 获取当前datetime
print(now)  # 2017-10-22 22:22:04.677899
print(type(now))  # <class 'datetime.datetime'>

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)   # 2015-04-19 12:20:00

# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
t = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
t.timestamp() # 把datetime转换为timestamp
print(t.timestamp()) # 1429417200.0

# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
t = 1429417200.0
print(datetime.fromtimestamp(t))
# 2015-04-19 12:20:00

# timestamp也可以直接被转换到UTC标准时区的时间：
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
# 2015-04-19 12:20:00
print(datetime.utcfromtimestamp(t)) # UTC时间
# 2015-04-19 04:20:00

# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。
# 转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# 2015-06-01 18:19:59

# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，
# 转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
# Sun, Oct 22 22:31

# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
# 加减可以直接用+和-运算符，不过需要导入timedelta这个类：
from datetime import datetime, timedelta
now = datetime.now()

# datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
now + timedelta(hours=10)
# datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
now - timedelta(days=1)
# datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
now + timedelta(days=2, hours=12)
# datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)

# collections是Python内建的一个集合模块，提供了许多有用的集合类。
# namedtuple
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
#
# p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
# 定义一个class又小题大做了，这时，namedtuple就派上了用场：
#
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x)
# # 1
# print(p.y)
# # 2
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
# 可以验证创建的Point对象是tuple的一种子类：
#
# isinstance(p, Point)
# # True
# isinstance(p, tuple)
# # True
# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
# # namedtuple('名称', [属性list]):
# Circle = namedtuple('Circle', ['x', 'y', 'r'])
# deque
#
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# from collections import deque
# q  = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
#
# deque(['y', 'a', 'b', 'c', 'x'])
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
#
# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
#
# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# dd['key1'] # key1存在
# #n'abc'
# dd['key2'] # key2不存在，返回默认值
# # 'N/A'
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
# OrderedDict
#
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
#
# from collections import OrderedDict
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# d # dict的Key是无序的
# {'a': 1, 'c': 3, 'b': 2}
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# od # OrderedDict的Key是有序的
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
#
# od = OrderedDict()
# od['z'] = 1
# od['y'] = 2
# od['x'] = 3
# list(od.keys()) # 按照插入的Key的顺序返回
# ['z', 'y', 'x']
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
#
# from collections import OrderedDict
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
# Counter
#
# Counter是一个简单的计数器，例如，统计字符出现的个数：
#
# from collections import Counter
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
#
# c
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})


# Base64是一种用64个字符来表示任意二进制数据的方法。

# 用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，
# 所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。
# Base64是一种最常见的二进制编码方法。
#
# 准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，
# 所以，字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：
#
# n = 10240099
# b1 = (n & 0xff000000) >> 24
# b2 = (n & 0xff0000) >> 16
# b3 = (n & 0xff00) >> 8
# b4 = n & 0xff
# bs = bytes([b1, b2, b3, b4])
# bs
# b'\x00\x9c@c'
# 非常麻烦。如果换成浮点数就无能为力了。
# 好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
# struct的pack函数把任意数据类型变成bytes：
#
# import struct
# struct.pack('>I', 10240099)
# b'\x00\x9c@c'

# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。
#
# 假设第一步已经完成了，第二步应该如何解析HTML呢？
#
# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
#
# 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：
#
# from html.parser import HTMLParser
# from html.entities import name2codepoint
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