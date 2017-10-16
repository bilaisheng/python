# try...except...finally...的错误处理机制
try:   # 需用于异常处理的模块
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:   # 捕抓异常并返回提示
    print('except:', e)
finally:   # 无论如何都要执行的
    print('finally...')
print('END')

# 可以添加更多的except模块去捕抓可能出现的具体的异常
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:   # 参数类型错误
    print('ValueError:', e)
except ZeroDivisionError as e:   # 被除为0异常
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

'''
说明：
第二个except永远也捕获不到UnicodeError，因为UnicodeError
是ValueError的子类，如果有，也被第一个except给捕获了

Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
'''


# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()
# 调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，
# 就可以处理不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
# 这样一来，就大大减少了写try...except...finally的麻烦
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

# 可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，
# 然后分析错误原因，同时，让程序继续执行下去。Python内置的logging模块可以非常容易地记录错误信息
import logging


def A(s):
    return 10 / int(s)


def B(s):
    return foo(s) * 2


def C():
    try:
        B('0')
    except Exception as e:
        logging.exception(e)

C()
print('code continue。。。。')   # 上面的代码执行出错但是程序可以继续运行

'''
因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，
而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
'''


class FooError(ValueError):
    pass


def DD(s):
    n = int(s)
    if n==0:
        raise FooError('被除数是: %s' % s)   # 用raise语句跑出一个错误的实例
    return 10 / n

DD('0')

'''
例子：
捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，
让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，
最终会抛给CEO去处理
'''


def SS(s):
    n = int(s)
    if n==0:
        raise ValueError('这里的错误是: %s' % s)
    return 10 / n


def QQ():
    try:
        SS('0')
    except ValueError as e:
        print('最终错误!')
        raise

QQ()

# raise语句如果不带参数，就会把当前错误原样抛出。此外，
# 在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')

