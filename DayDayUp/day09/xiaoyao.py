# 错误处理
# try
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
# try...
# except: division by zero
# finally...
# END

# 从输出可以看到，当错误发生时，后续语句print('result:', r)不会被执行，
# except由于捕获到ZeroDivisionError，因此被执行。
# 最后，finally语句被执行。然后，程序继续按照流程往下走。
'''
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
'''
# 将除数变为2即可正常运行
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 输出try...
# result: 5
# finally...
# END
'''
由于没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）
'''
# 如果发生了不同类型的错误，应该由不同的except语句块处理。可以有多个except来捕获不同类型的错误：
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:  # 用except捕获ValueError
    print('ValueError:', e)
except ZeroDivisionError as e: # 用except捕获ZeroDivisionError
    print('ZeroDivisionError:', e)
else:
    print('no error!') # 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
finally:
    print('finally...')
print('END')


# 调试
# 第一种 print 用print()最大的坏处是将来还得删掉它
# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n
#
#
# def main():
#     foo('0')
#
# main()


# 第二种 断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'  # assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    return 10 / n


def main():
    foo('0')

# 第3种logging logging不会抛出错误，而且可以输出到文件
# import logging
# logging.basicConfig(level=logging.INFO)
#
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

'''
logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别
当我们指定level=INFO时，logging.debug就不起作用了
这样一来，可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件
'''

# 第4种 启动Python的调试器pdb 让程序以单步方式运行
# err.py
s = '0'
n = int(s)
print(10 / n)

# $ python3 -m pdb err.py
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
# 输入命令n可以单步执行代码：
# 输入命令p 变量名来查看变量
# 输入命令q结束调试，退出程序

# 单元测试
# mydict.py代码如下：


# class Dict(dict):
#
#     def __init__(self, **kw):
#         super().__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value

# 需要引入Python自带的unittest模块
# import unittest
#
# from mydict import Dict
#
# class TestDict(unittest.TestCase):
#
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))
#
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key, 'value')
#
#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty

# 文档测试
import re
m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))

# Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
# 只有测试异常的时候，可以用...表示中间一大段烦人的输出。
