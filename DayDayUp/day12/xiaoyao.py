# 常用内建模块
# datetime
# collections
# base64
# struct
# hashlib
# itertools
# contextlib
# XML
# HTMLParser
# urllib
# 常用第三方模块
# PIL

# datetime
# 获取当前时间

from datetime import datetime,timedelta,timezone

'''
datetime 是模块，datetime模块还包含一个datetime类，
通过from datetime import datetime导入的才是datetime这个类
'''
# 获取当前datetime
now = datetime.now()
print(now)

# 获取指定日期和时间
dt = datetime(2017, 9, 20, 11, 11) # 用指定日期时间创建datetime
print(dt)

# datetime转换为timestamp  如果有小数位，小数位表示毫秒数。
print(dt.timestamp())

# timestamp转换为datetime
'''
timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。
转换是在timestamp和本地时间做转换。
'''
t = 1506677400.0
print(datetime.fromtimestamp(t))

# timestamp也可以直接被转换到UTC标准时区的时间 相差8小时
print(datetime.utcfromtimestamp(t))

# str转换为datetime
cday = datetime.strptime('2017-09-20 11:11:00', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
print(now.strftime('%a, %b %d %H %M'))

# datetime加减
print(now + timedelta(hours=1))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=2))

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8

dt = datetime(2017, 9, 20, 12, 30) # 用指定日期时间创建datetime

dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

# 获取UTC时间，并强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

# astimezone() 将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# astimezone 将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

# collections
p = (1, 2)

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

print(isinstance(p, Point))

# 定义一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
'''
deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
这样就可以非常高效地往头部添加或删除元素。
'''
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q.popleft()
print(q)

'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。
如果希望key不存在时，返回一个默认值，就可以用defaultdict：
'''

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在
print(dd['key2']) # key2不存在，返回默认值

'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict：
'''
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # d的key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序

od = OrderedDict()
od['x'] = 1
od['z'] = 2
od['y'] = 3
print(list(od.keys())) # 按照插入的Key的顺序返回

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key

# Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)

# base64
import base64
print(base64.b64encode(b'binarychaAngstring'))
print(base64.b64decode(b'YmluYXJ5Y2hhbmdzdHJpbmc='))

'''
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
'''

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))

'''
Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
struct的pack函数把任意数据类型变成bytes：
'''
import struct
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print(struct.pack('>I', 102400999))
# unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

# hashlib
import hashlib
md5 = hashlib.md5() # md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
md5.update(bytes('admin',encoding='utf-8')) # 要对哪个字符串进行加密，就放这里
print(md5.hexdigest()) # 拿到加密字符串 

sha1 = hashlib.sha1()
sha1.update('how to use md5 in '.encode('UTF-8'))
sha1.update('python hashlib ?'.encode('UTF-8'))
print(sha1.hexdigest())

# itertools
import itertools
natuals = itertools.count(1)

# 限定重复次数为3次 重复内容为A
ns = itertools.repeat('A', 3)
for n in ns:
	print(n)

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
	print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：

for key, group in itertools.groupby('AAABBBCCCAAAA'):
	print(key, list(group))

# 忽略大小写
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	print(key, list(group))


# contextlib
class Query(object):

	def __init__(self, name):
		self.name = name

	def __enter__(self):
		print('Begin')
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type:
			print('Error')
		else:
			print('End')

	def query(self):
		print('Query info about %s ...' % self.name)

with Query('Bob') as q:
	print(q.query())

#编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，
# 上面的代码可以改写如下：
from contextlib import contextmanager
class Query(object):
	def __init__(self, name):
		self.name = name

	def query(self):
		print('Query info about %s ...' % self.name)

@contextmanager
def create_query(name):
	print('begin')
	q = Query(name)
	yield q
	print('end...')

with create_query('Bob') as q:
    print(q.query())

# 某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例
@contextmanager
def tag(name):
	print("<%s>" % name)
	yield
	print("<%s>" % name)

with tag("h1"):
	print("hello")
	print("world")

'''
如果一个对象没有实现上下文，我们就不能把它用于with语句。
这个时候，可以用closing()来把该对象变为上下文对象。
例如，用with语句使用urlopen()：
'''
from contextlib import closing
from urllib.request import urlopen

# with closing(urlopen('https://www.python.org')) as page:
# 	for line in page:
# 		print(line)


# xm
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

	def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
print(parser.Parse(xml))