# 了解定制类
# __str__


class Student(object):
    def __init__(self,name):
        self.name = name
print(Student('jack'))  # <<<<__main__.Student object at 0x0000000000A3B5F8>


# 定义好__str__()方法，返回一个好看的字符串就可以了
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student('jack'))  # <<<< Student object (name: jack)

'''
__str__()，__repr__()，两者的区别是__str__()返回用户看到的字符串，
而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，
所以，有个偷懒的写法：
'''


class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__


# __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值
for n in Fib():
    print(n)


# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f =Fib()
# 可以按下标访问数列的任意一项  需要注意，list的切片方法在这里不能使用，__getitem__()传入的参数可能是一个int，
# 也可能是一个切片对象slice，所以要做判断print(f[0])
print(f[0])

# 使用枚举类
# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
JAN = 1
FEB = 2
MAR = 3  # 好处是简单，缺点是类型是int，并且仍然是变量

# 为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例：Enum
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique


@unique  # @unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon
print(day1)  # >>>> Weekday.Mon
print(day1.value)  # >>>> 1

for name, member in Weekday.__members__.items():
     print(name, '=>', member)


# 使用元类
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


def fn(self, name='world'):  # 先定义函数
      print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
h.hello
print(type(Hello))


# metaclass，直译为元类 先定义metaclass，就可以创建类，最后创建实例
# metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass

'''
当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，
然后，返回修改后的定义。
__new__()方法接收到的参数依次是：
1.当前准备创建的类的对象；
2.类的名字；
3.类继承的父类集合；
4.类的方法集合。
'''
L = MyList()
L.add(1)
print(L)
# 而普通的list没有add()方法：
