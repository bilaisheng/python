# 使用__slots__
# 正常情况下，当我们定义了一个类，我们可以给该class绑定任何的属性和方法，这相当的灵活


class Student(object):
    pass

s = Student();
s.name = 'Test'
print(s.name)


# 可以尝试绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType   # 给class绑定方法需要导入MethodType
s.set_age = MethodType(set_age, s)   # 给实例绑定一个方法
s.set_age(25)   # 调用实例方法
print(s.age)


# 为了给所有的实例绑定方法。可以给class绑定方法
def set_score(self, score):   # 定义一个分数的方法
    self.score = score
Student.set_score = set_score   # 给Student这个class绑定上面的分数的方法
s = Student()
s.set_score(100)
print(s.score)

# 上面的方法在静态语言中容易实现，但是动态绑定允许我们在程序运行的过程中动态给class加上功能在静态语言中时不容易实现的
'''
__slots__
假如要限制实例的属性，比如，只允许对Student实例添加name和age属性
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
'''


class student(object):
    __slots__ = ('name', 'age')   # 用tuple定义允许绑定的属性名称

# 测试
s = student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# s.score = 99 # 绑定属性'score'
print(s.name)
print(s.age)
# print(s.score)   # 这个会报错因我们已经限制不能定义除name 和 age以外的东西了


# 测试对对继承的子类的作用
class GraduateStudent(student):
    pass
g = GraduateStudent()
g.score = 99   # 父的限制没有继承到子类中
print(g.score)


class Test1(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):   # isinstance用于对参数类型进行限制
            raise ValueError('TestError')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
a = Test1()
a.set_score(88)
print(a.get_score())

'''
用Python内置的@property装饰器把一个方法变成属性调用的
这样做可以既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
'''


class Test2(object):
    @property
    def score(self):   # 定义属性
        return self._score

    # 把一个getter方法变成属性，只需要加上@property就可以了，此时，
    # @property本身又创建了另一个装饰器@score.setter，负责把一个
    # setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    @score.setter   # 定义属性的setter方法
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('TestError')
        if value < 0 or value > 100:
            raise ValueError('测试范围')
        self._score = value

b = Test2()
b.score = 22
print(b.score)

'''
多重继承是为了解决类的设计层次增加而导致类的数量会呈指数增长
操作方法就是子类在继承了一个父类的前提下载继承多一个父类，这样
一个子类就拥有多个父类的功能了
'''


class Animal(object):
    def pris(self):
        print('这是一只鸟')


class flying(object):
    def pri(self):
        print('会飞')


class hawk(Animal, flying):   # bird 继承了Animal 和 running，所以可以使用它们的方法
    def __init__(self):
        print('那是一只老鹰')

d = hawk()
d.pris()
d.pri()