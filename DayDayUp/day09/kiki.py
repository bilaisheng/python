#1、错误处理（为了避免因发生错误而中断整个程序，用try....except...finally...的错误处理机制抛出错误，
# 并按照我们的规定作出提示(finally  可以省略)
# try
try:#当产生错误时，try 模块不会被执行
    print('try...')
    r = 10 / 0
    print('result:',r)
except ZeroDivisionError as e: #产生错误时，执行except 语句块
    print('except',e)
finally:#无论是否发生错误，都finally块都会被执行
    print('finallt...')
print('END')
# 计算10 / 0 时会产生除法运算错误：
# try....
# except：division by zero
# finally...
# END

#错误会有很多种类，当发生不同类型的错误，应由不同的except语句块处理。
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:  #由多个except来捕获不同类型的错误
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:  #没有错误发生时，可以自动执行else语句
    print('no error!')
finally:
    print('finally...')
print('END')

#2、调试
#第一种调试方法，用print（）把可能有问题的变量打印出来
#坏处是将来还得回过头全部删掉
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')
main()

#第二种方法——断言..... 用断言（assert）来替代print（）
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' #n != 0应该是TRUE，否则，后面代码会出错，所以抛出错误提示
    return 10 / n

def main():
    foo('0')

#第三种方法....把print（）替换为logging，logging不会抛出错误，而是输出文本
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# logging好在允许制定记录的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。
# 指定level=WARNING后，debug和info就不起作用。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，
# 最后统一控制输出哪个级别的信息。
#logging还可以通过简单的配置，只用一条语句就可以同时输出到不同的地方，比如console和文件。

#第四种方法：启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
# err.py
s = '0'
n = int(s)
print(10 / n)

# $ python3 -m pdb err.py
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。
# 输入命令 l 可以查看代码
# 输入命令 n 进行单步执行代码
# 输入命令 p 变量名来查看变量
# 输入命令 q 结束调试，退出程序
#一步步调试是万能的，但是代码很多行时调试就很不方便了

#第五种方法：pdb.set.trace()
#这种方法也是使用pdb调试器，但可以对我们需要进行调试的区域进行断点debug
#import pdb，在可能出错的地方放个pdb.set_trace()，就可以设置一个断点：

# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

#在暂停的时候会进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：

#第六种：单元测试

#代码
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

import unittest

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

#文档测试
# Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确
# 只有测试异常的时候，可以用...表示中间一大段的输出

# def abs(n):
#     '''
#     Function to get absolute value of number.
#
#     Example:
#
#     >>> abs(1)
#     1
#     >>> abs(-1)
#     1
#     >>> abs(0)
#     0
#     '''
#     return n if n >= 0 else (-n)
