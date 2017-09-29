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

# 获取当前日期和时间

from datetime import datetime,timedelta,timezone
'''
注意到datetime是模块，datetime模块还包含一个datetime类，
通过from datetime import datetime导入的才是datetime这个类。
'''
# 获取当前datetime
now = datetime.now()
print(now)

# 获取指定日期和时间
dt = datetime(2017, 9, 29, 17, 30)  # 用指定日期时间创建datetime
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
cday = datetime.strptime('2017-9-29 17:30:00', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
print(now.strftime('%a, %b %d %H %M'))

# datetime加减
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=10))

# 本地时间转换为UTC时间

tz_utc_8 = timezone(timedelta(hours=8)) # 创建失去UTC+8:00

dt = datetime(2017, 9, 29, 17, 30)  # 用指定日期时间创建datetime

dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
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
print(q)

'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。
如果希望key不存在时，返回一个默认值，就可以用defaultdict：
'''

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # key1存在
print(dd['key2'])  # key2不存在，返回默认值

'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict：
'''

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)  # d的key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

od = OrderedDict()
od['x'] = 1
od['y'] = 2
od['z'] = 3
print(list(od.keys()))   # 按照插入的Key的顺序返回

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：


# class LastUpdateOrderedDict(OrderedDict):
#
#     def __init__(self, capacity):
#         super(LastUpdateOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey > self._capacity:
#             last = self.popitem(last=False)
#             print('remove:', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)

# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)

# base64
import base64
print(base64.b64encode(b'binary\x00string'))
print( base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
'''
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
'''
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

'''
好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
struct的pack函数把任意数据类型变成bytes：
'''
import struct
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print(struct.pack('>I', 102400999))
# unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

# hashlib
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('UTF-8'))
md5.update('python hashlib ?'.encode('UTF-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use md5 in '.encode('UTF-8'))
sha1.update('python hashlib ?'.encode('UTF-8'))
print(sha1.hexdigest())

# itertools
import itertools
natuals = itertools.count(1)
# 此处无限循环 注释
# for n in natuals:
#     print(n)

# 3 限定重复次数为3次 重复内容为A
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：

for key, group in itertools.groupby('AAABBCCCAAA'):
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
    print("</%s>" % name)

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
#     for line in page:
#         print(line)


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

# HTMLParser
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('<%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s>' % tag)
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
# # urllib
# from urllib import request
#
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))
#
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))



from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


# 图片放在当前文件同级目录下,图片不上传,注释
# from PIL import Image
#
# # 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('test.jpg')
# # 获得图像尺寸:
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# # 缩放到50%:
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# im.save('thumbnail.jpg', 'jpeg')

# 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('test.jpg')
# # 应用模糊滤镜:
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'jpeg')



import random

def generate_verification_code_two():
    '''随机成成6位验证码'''
    code_list = []

    for i in range(1,3):
        # 随机成成0-9之间的数字
        random_num = random.randint(0, 9)
        # 利用random生成65-90之间的随机整数 使得65<=a<=90
        # 对应从'A'到'Z'之家的ASCII码
        a = random.randint(65, 90)
        # 对应从'a'到'z'之家的ASCII码
        b = random.randint(97, 120)

        random_uppercase_letter = chr(a)
        random_lowercase_letter = chr(b)

        code_list.append(str(random_num))
        code_list.append(random_uppercase_letter)
        code_list.append(random_lowercase_letter)
    verification_code = ''.join(code_list)
    return verification_code

print(generate_verification_code_two())





def generate_verification_code(len=6):
    ''' 随机生成6位的验证码 '''
    # 注意： 这里我们生成的是0-9A-Za-z的列表，当然你也可以指定这个list，这里很灵活
    # 比如： code_list = ['P','y','t','h','o','n','T','a','b'] # PythonTab的字母
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91): # 对应从“A”到“Z”的ASCII码
        code_list.append(chr(i))
    for i in range(97, 123): #对应从“a”到“z”的ASCII码
        code_list.append(chr(i))
    myslice = random.sample(code_list, len)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice) # list to string
    return verification_code

print(generate_verification_code())
