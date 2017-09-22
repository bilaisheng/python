# 迭代器与生成器
from collections import Iterator
isinstance((x for x in range(10)), Iterator)
# iter()函数获得一个Iterator对象。
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

# 一边循环一边计算的机制，称为生成器


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done'
fib(6)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g', x)
    except StopIteration as e:
        print('Generator return value', e.value)
        break
# 输入和输出
# File(文件) 方法
# file

# 读文件
f = open('hello.txt','w')
# 写文件
f.write('hello\n')
f.write('world\n')
# lose()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
f.close()
t = open('hello.txt')
# 读文件
text = t.read()
t.close()
print(text)
st = text.split()
print(st)
detail = dir(f)
print(detail)
he = help(f.seek)
print(he)
# 简便写法
#   try：
#      f = open('hello.txt','r')
#      print(f)
#   finally:
#      if f:
#       f.close()
with open('hello.txt', 'r') as f:
    print(f.read())
# 推荐这种

with open('hello.txt', 'r') as f:
    for line in f.readlines():
       print(line.strip())

# 二进制文件
f = open('test.jpg', 'rb')
f.read()
# 字符编码
f = open('gbk.txt', 'r', encoding='gbk', errors='ignore')
f.read()
# 写文件
f = open('text.txt', 'w')
f.write('hhahah,super')
f.close()

# 简便写法
with open('text.txt', 'w') as f:
    f.write('hello world')

# OS 文件/目录方法
# StringIO
# getvaule方法获得写入后的str

from io import  StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f = StringIO('hello!\nhi!\ngoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
# BytesIO
# 操作二进制数据
from io import BytesIO
f = BytesIO
f.write('中文'.encode('utf-8'))
print(f.getvalue())
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
# 操作文件和目录
# os 模块的某些函数是跟操作系统相关的
import os
print(os.name)
# 如果需要获取详细的系统信息，可以调用uname（）
print(os.uname())
# 环境变量
# 在操作系统中定义环境变量全部保存在os.environ变量中
print(os.environ)
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))
# 操作文件和目录
# 查看当前目录的绝对路径
os.path.abspath('.')
# 在某个目录下创建一个新目录
os.path.join('/user/michael','testdir')   # 把新目录的完整路径表示出来
os.mkdir('/user/michael/testdir')  # 创建一个目录
os.rmdir('/user/michael/testdir')  # 删除一个目录
# 列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]
# 列出特定后缀名的文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# 正则表达式
# []表示匹配這些字符之一，$匹配字符串的結尾 re.sub()函數執行基於正則表達式的字符串的替換
# ^ 除了


import re


# def plural(noun):
#     if re.search('[sxz]$', noun):
#         return re.sub('$', 'es', noun)
#     elif re.search('[^aeioudgkprt]h$',noun):
#         return re.sub('$', 'es', noun)
#     elif re.search('[aeiou]y$', noun):
#         return re.sub('y$', 'ies', noun)
#     else:
#         return noun + 's'
#
# print(plural('vacancy'))


def match_sxz(noun):
    return re.search('[sxz]$', noun)


def apply_sxz(noun):
    return re.sub('$', 'es', noun)


def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)


def apply_h(noun):
    return re.sub('$', 'es', noun)


def match_y(noun):
    return re.search('[^aeiou]y$', noun)


def apply_y(noun):
    return re.sub('y$', 'ies', noun)


def match_default(noun):
    return True


def apply_default(noun):
    return noun + 's'

rules = (
    (match_sxz, apply_sxz),
    (match_h, apply_h),
    (match_y, match_y),
    (match_default, match_default())
         )

# 每一條匹配規則都有自己的函數，返回對re.search()函數


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


