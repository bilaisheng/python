# 1、了解定制类
# 2、使用枚举类
# 3、使用元类

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
# print(Student('Michael'))
#
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name %s)' % self.name
# print(Student('Michael'))
#
# s = Student('Godiness')
# print(s)
#
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name %s)' % self.name
#     __repr__ = __str__
#
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return  self  # 实例本身就是一个迭代对象 , 故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b  # 计算下一个值
#         if self.a > 10000:
#             raise  StopIteration()
#         return self.a  # 返回下一个值
#
# for n in Fib():
#     print(n)
#
# # print(Fib()[5])   # 此处报错.不支持这种写法 ,需转换实现__getitem__
#
# class Fib(object):
#     def __getitem__(self, item):
#         a, b = 1, 1
#         for x in range(item):
#             a, b = b, a + b
#         return a
#
# f = Fib()
# print(f[10])
#
# class Fib(object):
#
#     def __getitem__(self, item):
#         if isinstance(item, int): # item是索引
#             a, b = 1, 1
#             for x in range(item):
#                 a, b = b, a + b
#             return a
#
#         if isinstance(item, slice):  # item 是切片
#             start = item.start
#             stop = item.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#
# f = Fib()
# print(f[0:5])
# print(f[:10])
# print(f[:10:2])
#
#
# class Student(object):
#     def __init__(self):
#         self.name = 'Godliness'
#
#     def __getattr__(self, item):
#         if item == 'score':
#             return 99
#         if item == 'age':
#             return lambda : 25
#
# s = Student()
# print(s.name)
# print(s.score)
# print(s.age)
# print(s.age())

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s ' % self.name)

s = Student('godliness')
s()
# 判断对象是否可以被调用 : callable
print(callable(Student('ss')))


# 枚举类

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# @unique装饰器可以帮助我们检查保证没有重复值。

day1 = Weekday.Mon
print(day1)

print(Weekday['Tue'])

print(Weekday.Thu.value)

print(day1 == Weekday.Tue)


# print(Weekday(7))

for name, member in Weekday.__members__.items():
    print(name, '=>', member, '=>', member.value)


# 元类

class Hello(object):
    def hello(self, name='world'):
        print('Hello %s' % name)

'''
创建一个class对象，type()函数依次传入3个参数：
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''
def fn(self, name='world'):
    print('Hello %s' % name)


Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello.class

h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# metaclass 是类的模板, 所以必须从type类派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value : self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

'''
__new__()方法接收到的参数依次是：
当前准备创建的类的对象；
类的名字；
类继承的父类集合；
类的方法集合。
'''
L = MyList()
L.add(1)
L.add(2)
print(L)

