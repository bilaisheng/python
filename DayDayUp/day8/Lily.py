"""
day8:
1、了解定制类
2、使用枚举类
3、使用元类
"""
# __str__ 可以让输出更简洁


class Student(object):
   def __init__(self, name):
       self.name = name

print(Student('Michael'))   #  <__main__.Student object at 0x109afb190>

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
       return 'Student object (name: %s)' % self.name

print(Student('Michael'))   # Student object (name: Michael)


# __repr__
s = Student('Michael')
# s  # <__main__.Student object at 0x109afb310>
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，
# 两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 解决办法是再定义一个__repr__()。
# 但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

#s # Student object (name: Michael)

# __iter__
#
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 1000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

# 问题未解决：
# for n in a:
#    print(n)

# __getitem__
#
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print(f[0])
print(f[12])
print(list(range(100))[5:10])
# [5, 6, 7, 8, 9]


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0:5])  # [1, 1, 2, 3, 5]


# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
class Student(object):

    def __init__(self):
        self.name = 'Michael'


s = Student()
print(s.name)
# Michael
# print(s.score)  error
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，
# 动态返回一个属性。

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

s = Student()
print(s.name)
# 'Michael'
print(s.score)
# 99

# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
# 好处是简单，缺点是类型是int，并且仍然是变量。
# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。
# Python提供了Enum类来实现这个功能：


from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# Jan = > Month.Jan, 1
# Feb = > Month.Feb, 2
# Mar = > Month.Mar, 3
# Apr = > Month.Apr, 4
# May = > Month.May, 5
# Jun = > Month.Jun, 6
# Jul = > Month.Jul, 7
# Aug = > Month.Aug, 8
# Sep = > Month.Sep, 9
# Oct = > Month.Oct, 10
# Nov = > Month.Nov, 11
# Dec = > Month.Dec, 12
# value属性则是自动赋给成员的int常量，默认从1开始计数。
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# @unique装饰器可以帮助我们检查保证没有重复值。
# 访问这些枚举类型可以有若干种方法：
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)


# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
# 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，
# 动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，
# 必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)



