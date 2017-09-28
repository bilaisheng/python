#  错误、调试和测试：错误处理、调试、单元测试和文档测试
# 錯誤處理 try 。。except 。。finally
import unittest
import logging

try:
    print('try ...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('end')
# 當我們任務某些代碼可能出錯時，就可以try來運行這段代碼
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')
# python所有的錯誤類型都繼承BaseException，還要注意父子類關係，例如UnicodeError是ValueError的子類
# try。。。except有一個好處就是可以跨越多層調用


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('ERROR', e)
    finally:
        print('finally..')
# 如果錯誤沒有被捕獲，就會一直往上拋，最後被python解釋器捕獲，大約一個錯誤信息然後退出程序。
# 記錄錯誤
# import logging


def foo(s):
    return 10/int(s)


def bar(s):
    return foo(s)*2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
# 拋出錯誤


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value:%s' % s)
    return 10 /n
# 斷言 凡是用print（）來輔助查看的地方，都可以用斷言assert來替代


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n


def main():
    foo('0')

# logging頁可以替代Print，與asset相比logging不會拋出錯誤而且可以輸出到文件


s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# logging 的好處可以允許你指定記錄信息的級別，有debug，info，warning，error
# 等幾個級別，級別從小到大
# pdb 啟動Python的調試器 讓程序以單步執行
# (Pdb) l
# s = '0'
# n = int(s)
# print(10 / n)

# 單元測試


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

# import unittest


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

    def test_KeyError(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_AttrError(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 運行單元測試
if __name__ == '__main__':
    unittest.main()

# setUp与tearDown 调用一个测试方法的前后分别被执行


class TestDict(unittest.TestCase):
    def setUp(self):
        print('setup...')

    def tearDown(self):
        print('tearDown...')