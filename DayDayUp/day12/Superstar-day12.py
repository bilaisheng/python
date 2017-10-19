# 正則表達式
# \d 匹配數字，\w匹配一個字母或者數字 .可以匹配任意字符  * 表示任意個字符  ？表示0個或者1個字符，
# {n,m}表示n-m個字符 特殊字符需要轉義 例如\-表示-
r = '\d{3}\s+\d{3,8}' # \d{3} 匹配3個數字 \s 表示匹配一個空格 \{3-8}三到八個數字
# 進階 [] 表示範圍
r1 = '[0-9a-z\_]'  # 可以匹配一個數字、字母或者下劃線
r2 = '[0-9a-zA-Z\_]+'  # 可以匹配至少一個字母，數字或者下劃線組成的字符串
r3 = '[a-zA-Z\_][0-9a-zA-Z\_]{0,19}' # 限制了變量的長度時1-20個字符
# A\B 可以匹配A或B
# ^ 表示行開頭 ^\d表示必須以數字開頭
# $ 表示行結束
# re模塊
import  re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
test = '用戶輸入的字符串'
if re.match(r'正則表達式', test):
    print('ok')
else:
    print('failed')

# 常用内建模块
# datetime
# 獲取當前時間
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))
# 獲取指定時間
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
print(dt.timestamp())
# timestamp 轉換為datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))
# UTC 標準時區
print(datetime.utcfromtimestamp(t))
# str轉換為datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# datetime 加減
from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now + timedelta(hours=10))
print(now + timedelta(days=2, hours=12))
# 時區轉換
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# collections
# namedtuple 是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
# Point 對象是tuple的一種子類
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
# deque deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from  collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
# defaultdict key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda :'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
# OrderedDict 使用dict时，Key是无序的。在对dict做迭代时，
# 我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
# OrederedDict是一個先進先出的dict，當容量超出時，會刪除最早添加的key
class LastUpdateOrderDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self)- containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add：',(key, value))
        OrderedDict.__setitem__(self, key, value)
# Counter 一個簡單的計數器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch]=c[ch]+1
print(c)

# base64 是一種用64個字符表示二進制數據的方法
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
# print(base64.b64decode(b'i\xb7\x1d\xfb\xef\xff'))

# struct
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = (n & 0xff)
bs = bytes([b1, b2, b3, b4])
print(bs)
import struct
print(struct.pack('>I', 10240099))  # >I表示4字節無符號數
# hashlib
# 摘要算法也是哈希算法，散列算法。他通過一個函數，把任意長度的數據轉換為一個固定長度的數據串
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest()) # 可多次調用update（）
# itertools
# python內建模塊itertools提供了非常有用的用於操作迭代對象的函數
import itertools
natuals = itertools.count(1)   # count會創建一個無線的迭代器，只能按ctrl+C退出
for n in natuals:
    print(n)
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)
# takewhile()等函数根据条件判断来截取出一个有限的序列
# ns1 = itertools.takewhile(lambda x: x<=10, natuals)
# print(list(ns1))
# chain() 把一組對象串聯起來，形成一個更大的迭代器
# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)
# groupby() 把重複放入元素挑出來
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))
# contextlib
# 在python中讀寫文件，必須在使用完畢之後正確關閉他們一般使用try。。。finally
# 為了簡化
with open('/path/to/file','r') as f:
    f.read()
# 任何對象只要實現了上下文管理，就可以使用with語句，通過__enter__和__exit__


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('begin')
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type:
           print('Error')
        else:
            print('end')

    def query(self):
        print('Query info about %s...' % self.name)
with Query('Bob') as q:
    q.query()
# @contextmanager

# XML
# HTMLParser
# urllib
# 常用第三方模块
# PIL
# contextlib
# 在python中讀寫文件，必須在使用完畢之後正確關閉他們一般使用try。。。finally
# 為了簡化
# with open('/path/to/file', 'r') as f:
#     f.read()


# 任何對象只要實現了上下文管理，就可以使用with語句，通過__enter__和__exit__


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):  # 進來
        print('begin')
        return self

    def __exit__(self, exc_type, exc_val, traceback):  # 檢查和出去
        if exc_type:
            print('Error')
        else:
            print('end')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('Bob') as q:
    q.query()

# @contextmanager 標籤實現了進入和出來的兩個方法
from contextlib import contextmanager


class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query2 info about %s..' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q2= Query2(name)
    yield q2
    print('End')

with create_query('sum') as q2:
    q2.query()


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)
with tag('h1'):
    print('hello')
    print('hi')
# with 語句首先執行的yield之前的語句，yield會執行with語句內部的所有語句
# 最後執行yield之後的語句

# closing方法吧對象變為上下文對象
from contextlib import closing
from  urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)

# XML
# 三個事件start_element、char_date和end_element
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs:%s'% (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element:%s' % name)

    def char_data(self, text):
        print('sax:char_data:%s' % text)
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
# HTMLParser
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s:' % name)

    def handle_charref(self, name):
        print('&#%s:' % name)
parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
# urllib 一系列的用於操作URL的功能
# Get
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
# Post
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
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
    # 常用第三方模块
# PIL
from PIL import Image, ImageFilter
im = Image.open('D:532282682075721553.png')
w, h =im.size
print('原始尺寸：%sx%s'% (w,h))
im.thumbnail((w//2, h//2))
print('變化后：%sx%s'% (w//2, h//2))
im.save('thumbnail.png','png')
# 切片、旋转、滤镜、输出文字、调色板功能都有
# 模糊效果
im = Image.open('D:532282682075721553.png')
im2 =im.filter(ImageFilter.BLUR)
im2.save('blur.png','png')

from PIL import  Image, ImageDraw,ImageFont, ImageFilter
import random
# 隨機字母


def rndChar():
    return chr(random.randint(65, 90))
# 隨機顏色


def rndColor():
    return (random.readint(64,255),random.readint(64,255),random.readint(64,255))
# 隨機顏色2


def rndColor2():
    return (random.readint(32,127),random.readint(32,127),random.readint(32,127))

width = 60 *4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 創建font對象
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
# 創建Draw對象
draw = ImageDraw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

