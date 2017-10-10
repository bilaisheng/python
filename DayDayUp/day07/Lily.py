"""
Day7:
使用__slots__
使用@property
多重继承

问题：MethodType有问题

"""
import types
from types import MethodType
# python类在进行实例化的时候，会有一个__dict__属性，里边有可用的实例属性名和值。
# 声明__slots__后，实例就只会含有__slots__里有的属性名。
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法.
# 这就是动态语言的灵活性。先定义class：

class Student(object):
    pass

# 然后，尝试给实例绑定一个属性：

s = Student()
s.name = 'Michael'   # 动态给实例绑定一个属性
print(s.name)   # Michael
# 还可以尝试给实例绑定一个方法：


def set_age(self, age):   # 定义一个函数作为实例方法
    self.age = age


# s.set_age = MethodType(set_age, s, Student)   # 给实例绑定一个方法
# s.set_age(25)   # 调用实例方法
# print(s.age)   # 测试结果

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：

s2 = Student()  # 创建新的实例
# s2.set_age(25) # 尝试调用方法

# 为了给所有实例都绑定方法，可以给class绑定方法：

def set_score(self, score):
    self.score = score

# Student.set_score = MethodType(set_score, None, Student)
# 给class绑定方法后，所有实例均可调用：
#
# s.set_score(100)
# print(s.score)
#
# s2.set_score(99)
# print(s2.score)

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
# 使用__slots__
# 但是，如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# s.score = 99  # 绑定属性'score' error

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999

# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。

# 取值和赋值

class Actress():
    def __init__(self):
        self.name = 'TianXin'
        self.age = 5


# 类Actress中有两个成员变量name和age。
# 在外部对类的成员变量的操作，主要包括取值和赋值。
# 简单的取值操作是x = object.var，简单的赋值操作是object.var = value。

actress = Actress()
print(actress.name)  # 取值操作
print(actress.age)  # 取值操作
actress.name = 'NoName'  # 赋值操作
print(actress.name)


# 使用Getter和Setter
# 上述简单的取值和赋值操作，在某些情况下是不能满足要求的。
# 比如，如果要限制Actress的年龄范围，那么只使用上述简单的赋值操作就不能满足要求了。
# getter和setter实现这样的要求。


class Actress():
    def __init__(self):
        self._name = 'TianXin'
        self._age = 20

    def getAge(self):
        return self._age

    def setAge(self, age):
        if age > 30:
            raise ValueError
        self._age = age


# 调用setAge函数可以实现将变量_age的取值范围限制到小于30.

actress = Actress()
actress.setAge(28)
actress.getAge()
# actress.setAge(35)   # ValueError
# 使用property
# property的定义是：
# 其中，fget是取值函数，fset是赋值函数，fdel是删除函数。使用property也实现上述对成员变量的取值限制。


class Actress():
    def __init__(self):
        self._name = 'TianXin'
        self._age = 20

    def getAge(self):
        return self._age

    def setAge(self, age):
        if age > 30:
            raise ValueError
        self._age = age

    age = property(getAge, setAge, None, 'age property')


# 经过上面的定义后，可以像简单取值和赋值操作一样操作age。比如，

actress = Actress()
print(actress.age)
actress.age = 18
# actress.age = 55   # ValueError
# 使用 @ property
# 使用 @ property同样可以实现上述类的定义。


class Actress():
    def __init__(self):
        self._name = 'TianXin'
        self._age = 20

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 30:
            raise ValueError
        self._age = age


# 使用时的示例：

actress = Actress()
print(actress.age)
actress.age = 18
# actress.age = 45   #  ValueError


# 多重继承
# 除了从一个父类继承外，Python允许从多个父类继承，称为多重继承。
# 多重继承的继承链就不是一棵树了，它像这样：

class A(object):
    def __init__(self, a):
        print('init A...')
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print('init B...')

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print('init C...')

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print('init D...')

# 像这样，D 同时继承自 B 和 C，也就是 D 拥有了 A、B、C 的全部功能。多重继承通过 super()调用__init__()方法时，A 虽然被继承了两次，但__init__()只调用一次：

d = D('d')
# init A...
# init C...
# init B...
# init D...
# 多重继承的目的是从两种继承树中分别选择并继承出子类，以便组合功能使用。