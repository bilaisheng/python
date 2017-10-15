# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

# 像上面的类中，将他的变量变成私有变量之后，下面的方法就不能成功调用了
bart = Student('Bart Simpson', 98)
print(bart)   # 能够成功，但是像下面那样要给他重新赋值或者取值就不可以了
# bart.score() = 5

# 如果外部想要获得Student类里面的值就得在类中增加get方法，可以进行如下的改造
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

bart = Student('Bart Simpson', 98)
print(bart.get_name())   # 能够成功打印出名字

# 如果希望外部可以修改类中的属性，可以增加set方法
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name
bart = Student('Bart Simpson', 98)
print('赋值前： ', bart.get_name())
bart.set_name('wofoaiwe')
print('赋值后： ', bart.get_name())
print('强烈建议不要这样取值因为不同版本的Python解释器可能会把__name改成不同的变量名：',bart._Student__name)
'''
    1、需要注意的是，在Python中，变量名类似__xxx__的，
       也就是以双下划线开头，并且以双下划线结尾的，是
       特殊变量，特殊变量是可以直接访问的，不是private变量，
       所以，不能用__name__、__score__这样的变量名。
    2、像上面的例子 bart = Student('Bart Simpson', 98),千万不可用bart.__name = 'New Name' 来设置__name变量！
       表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
       内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量
'''
bart.__name = '测试'
print(bart.__name)
print('但是通过get方法输出值还是没有被改变', bart.get_name())

# 获取对象信息
# 可以使用type() 函数来确认一个对象是什么类型
print(type(None))   # 注意None的类型是NoneType

# 如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types


def fu():
    pass
print(type(fu) == types.FunctionType)   # Types中还要很多类型可以判断

# 判断class的类型，可以使用isinstance()函数 ，用法就是isinstance(别名， 函数名)，
# 如别名是属于函数的话返回True，其中函数写他的父类也可以判断成功，但是父类用子类来判断就不行
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print('判断是否是list或者tuple: ', isinstance([1, 2, 3], (list, tuple)))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
# 比如，获得一个str对象的所有属性和方法
print(dir('ABC'))

# 测试对象拥有哪些属性
hasattr(Student, 'x')  # 有属性'x'吗？

# 获取属性的两种方法
getattr(Student, 'name')  # 获取属性'y'
Student.get_name()

'''
装饰器
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）本质上，decorator就是一个返回函数的高阶函数
'''
# 定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log   # 借助Python的@语法，把decorator置于函数的定义处,这样在调用new的时候会一起调用log()
def new():
    print('2017-09-21')
new()

# 对比下面的两个代码理解装饰器
'''
经过decorator装饰之后的函数，它们的__name__已经从原来的变成装饰器
返回的函数的名称，为了避免有些依赖函数签名的代码执行会出错，需要把
原始函数的__name__等属性复制到装饰器返回的函数中，这个时候可以在装
饰器中使用Python内置的 functools.wraps 来解决这个问题
'''
def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

import functools   # 导入functools模块
def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper