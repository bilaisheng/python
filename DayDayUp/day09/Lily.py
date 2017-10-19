"""
错误、调试和测试：错误处理、调试、单元测试和文档测试
"""

# Python有两种错误很容易辨认：语法错误和异常。

# 语法错误：
# while True print('Hello world')
#
# File "C:/Users/acer w700/Documents/GitHub/python/DayDayUp/day09/Lily.py", line 6
# while True print('Hello world')
#                 ^
# SyntaxError: invalid syntax
# 这个例子中，函数 print() 被检查到有错误，是它前面缺少了一个冒号（:）。
# 语法分析器指出了出错的一行，并且在最先找到的错误的位置标记了一个小小的箭头。

# 即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
# 异常：
# 10 * (1/0)
# Traceback (most recent call last):
#   File "C:/Users/acer w700/Documents/GitHub/python/DayDayUp/day09/Lily.py", line 19, in <module>
#     10 * (1/0)
# ZeroDivisionError: division by zero
# 4 + spam*3
# Traceback (most recent call last):
#   File "C:/Users/acer w700/Documents/GitHub/python/DayDayUp/day09/Lily.py", line 24, in <module>
#     4 + spam*3
# NameError: name 'spam' is not defined
# '2' + 2
# Traceback (most recent call last):
#   File "C:/Users/acer w700/Documents/GitHub/python/DayDayUp/day09/Lily.py", line 29, in <module>
#     '2' + 2
# TypeError: must be str, not int


# try语句按照如下方式工作；
# 首先，执行try子句（在关键字try和关键字except之间的语句）
# 如果没有异常发生，忽略except子句，try子句执行后结束。
# 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
# 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
# 一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
# 处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。

# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
# except(RuntimeError, TypeError, NameError):
#     pass
# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
# try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。
# 这个子句将在try子句没有发生任何异常的时候执行。例如:
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
# 使用 else 子句比把所有的语句都放在
# try 子句里面要好，这样可以避免一些意想不到的、而except又没有捕获的异常。
# 异常处理并不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。
# 例如:
# def this_fails():
#     x = 1 / 0
#
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

# 输出  Handling run-time error: int division or modulo by zero

# Python 使用 raise 语句抛出一个指定的异常。例如:
# raise NameError('HiThere')

# File "C:/Users/acer w700/Documents/GitHub/python/DayDayUp/day09/Lily.py", line 86, in <module>
# Handling run-time error: division by zero
#     raise NameError('HiThere')
# NameError: HiThere

# raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
# 如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise


# 用户自定义异常
# 你可以通过创建一个新的exception类来拥有自己的异常。异常应该继承自 Exception 类，或者直接继承，或者间接继承，例如:
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
# 输出：My exception occurred, value: 4

# 程序能一次写完并正常运行的概率很小，基本不超过1%。
# 总会有各种各样的bug需要修正。有的bug很简单，看看错误信息就知道，有的bug很复杂，
# 我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。
#
# 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()

# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。
# 所以，我们又有第二种方法。
#
# 断言
#
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
# main()

# 程序中如果到处充斥着assert，和print()相比也好不到哪去。
# 不过，启动Python解释器时可以用-O参数来关闭assert：
# python3 -O err.py
# 关闭后，你可以把所有的assert语句当成pass来看。

# logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：

# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
# INFO:root:n = 0
# Traceback (most recent call last):
#   File "C:/Users/acer w700/Documents/GitHub/python/DayDayUp/day09/Lily.py", line 159, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero

# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。


# 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
#
# 比如对函数abs()，我们可以编写出以下几个测试用例：
#
# 输入正数，比如1、1.2、0.99，期待返回值与输入相同；
#
# 输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
#
# 输入0，期待返回0；
#
# 输入非数值类型，比如None、[]、{}，期待抛出TypeError。
#
# 把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。
#
# 如果单元测试通过，说明我们测试的这个函数能够正常工作。如果单元测试不通过，要么函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过。
#
# 单元测试通过后有什么意义呢？如果我们对abs()函数代码做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对abs()函数原有的行为造成影响，如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。
#
# 这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。
# 在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。

# 如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。
# 可以把这些示例代码在Python的交互式环境下输入并执行，结果与文档中的示例代码显示的一致。
#
# 这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘贴出来直接运行，那么，可不可以自动执行写在注释中的这些代码呢？
#
# 答案是肯定的。
#
# 当我们编写注释时，如果写上这样的注释：

def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)
# 无疑更明确地告诉函数的调用者该函数的期望输入和输出。
#
# 并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
#
# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。
# 让我们用doctest来测试上次编写的Dict类：
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()