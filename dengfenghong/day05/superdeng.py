

s = ['ahdaG', 'sdU', 'HEFU']

#  按照標準格式輸出單詞
# 字符串相關操作方法
# join()方法把字符合成字符串
# capwords(str)：只保留str首字母大写 是先将字符串切成字符，进行首字母大写，其余小写，再用jion方法合并
# capitalize()：只保留str中首字母大写 把字符串整体操作，不进行分割
# split()函数 默认以空格为分隔符
# isupper()，islower()，istitle()方法用来判断字符串的大小写

import string


def numalSize(nums):
    l = []
    for i in nums:
        s = string.capwords(i)
        print(s)
        l.append(s)
    return l
numalSize(s)

# map 函数 分别取list的值跟函数作用


def f(x):
    return x*x
l = map(f,[1, 2, 3, 4, 5, 6])
print(list(l))

# reduce函数 把一个函数作用在一个序列[x1,x2,x3,x4....]这个函数接收两个参数，reduce把结果继续和序列的下一个元素做积累
# reduce（f,[x1,x2,x3,x4]）= f(f((x1,x2),x3),x4)
from functools import reduce


def fn(x, y):
    return x * 10 + y
n = reduce(fn, [1, 3, 5, 7, 9])
print(n)
# 可以结合字符串使用 map 和reduce结合 实现字符串直接变成数字


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

a = map(char2num, '13579')
print(list(a))

b = reduce(fn,map(char2num, '13579'))
print(b)
# 两个函数可以整合成一个函数str2int


def str2(s):

    def fn(x, y):
        return x * 10 + y


    def charm2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
# 利用匿名函数


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
# filter 函数用于过滤序列
#  和map类似，filter（）也接收一个函数和一个序列。和map不同的是，
#  filter把传入的函数依次作用每个元素，然后根据返回值True或者False决定是否保留还是丢弃

# 只保留列表里的奇数


def is_add(n):
    return n % 2 == 1
l = list(filter(is_add, [1, 2, 4, 5, 6, 10, 15]))
print(l)
# 删除序列中的空字符串


def not_empty(s):
    return s and s.strip()

l = list(filter(not_empty,['A', '', '', 'c', None, 'D']))
print(l)

# 排序算法 sorted
print(sorted([36, 5, -12, -21, 9]))
# sorted是一个高阶函数，可以接受key函数来实现自定义排序
print(sorted([36, 5, -12, -21, 9], key = abs))
# 默认情况下，对字符串排序是按照ASCII大小比较的 注意大写字母排小写前面
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 反向排序 传入第三个参数reverse = True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 返回函数
# 函数作为返回值


def lazy_sum(*args):

    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 3, 4, 5)
print(f)  # 调用的是对象
print(f())  # 调用的是函数

#  面向对象编程：公有属性和私有属性；属性装饰器，描述符；实例方法，静态方法，类方法


# class person(object):
#
#     city = "JP"  # 定义公有属性nationality
#
#     def __init__(self, name):
#         self.name = name
#
#
# d1 = person("alex")
# d2 = person("sanjiang")
# print(d1.nationality, d2.nationality)  # 所有的成员变量都可以访问
# d1.city = "US"  # 修改公有属性

# 私有屬性
# 如果要讓內部屬性不被外部訪問，可以在屬性名稱前面加上__，就變成了私有屬性
# 只能內部訪問，外部不能訪問
# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
# # 要獲取則採用 get_xxx
#
#     def get_name(self, name):
#         return name
# # 若要允許外部修改 可以給類加set_XXX方法
#
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')
# bart = Student('Bart Simpson', 98)
# print(bart.get_name())

# class Person():
#     # 只允许拥有私有的name和age属性
#     __slots__ = ('__name', '__age')
#
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,name):
#         self.__name=name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     def __str__(self):
#         return '姓名 '+self.__name+' \n年龄'+str(self.__age)
#
# if __name__ == '__main__':
#     zhangsan=Person('张三',20)
#     print(zhangsan)
#     print(zhangsan.name)
#     print(zhangsan.age)
#     zhangsan.age=30
#     zhangsan.name='张三三'
#     print(zhangsan)

# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以通过变量也能调用改函数


def now():
    print('2017-09-20')
f = now
f()
# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)

# decorator


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return  func(*args, **kw)
    return wrapper


@log
def now():
    print('2017-09-09')
now()

# decoratoe本身需要參數


def log(text):
    def decorator(func):
        def wrapper(*args, **hw):
         print('%s %s():' % (text, func.__name__))
         return func(*args, **hw)
        return wrapper
    return  decorator


@log('execute')
def now():
    print('2017899')

now()
now = log('execute')(now)
# 裝飾器也可以多個疊加

# 獲取對象信息 昨天已經寫了 此處複習
# type()函數判斷對象類型
# 若要判斷繼承關係 isinstance()函數哥合適
# dir()可以獲得一個對象的所有屬性和方法

# 實例屬性和類屬性
# 給實例綁定屬性


# class student(object):
#     def __init__(self, name):
#         self.name = name
# s = student('bob')
# s.score = 90
# 當我們定義一個類屬性這個屬性龜類所有
class Student(object):
    name = 'studet'
    __class = 11
print(Student.name)
# print(Student.__class)  # 訪問不了
s = Student()
# print(s.__class)  # 訪問不了
print(s.name)

del s.name  # 刪除實例name屬性
print(s.name)  # 无值
print(Student.name) # 报错 AttributeError



