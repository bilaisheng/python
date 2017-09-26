# 使用__slots__
# 使用@property
# 多重继承
# leetcode:Longest Common Prefix
# java环境搭建 工具 Myeclipse 2017 CI 8 , java9  tomcat 9

# 偏函数
# python的functool模块提供了很多有用的功能。
# int函数提供了额外的base参数，可以转化成相应的进制
import functools
import sys
from types import  MethodType


def int2(x, base=2):
    return int(x, base)
print(int2('10010'))

kw = {'base':2}
print(int('10010', **kw))


int2 = functools.partial(int, base=2)
print(int2('10010'))

max2 = functools.partial(max, 10)   # 相當於
args = (10, 5, 6, 7)
max(*args)
# 模块
__author__ = 'Super Deng'


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('Too many arguments!')
if __name__ == '__main__':
    test()
# 安装第三方模块
# 在python中，安装第三方模块是通过包管理工具pip完成的。
# from PIL import Image
# im = Image.open('test.png')
# print(im.format, im.size, im.mode)
# im.thumbnail(200, 100)

# 模塊搜索路徑
# import  mymodule
print(sys.path)
import sys
sys.path.append('/Users/michael/my_py_scripts')
# 使用__slots__


class Student(object):
    pass
s = Student()
s.name = 'super' # 动态的给实例绑定一个属性
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
print(s.set_age(25))


def set_score(self, score):
    self.score = score

# 为所有实例绑定方法
Student.set_score = set_score
print(s.set_score(100))
# 特殊的__slots__变量。来限制class实例能添加的属性
class Student2(object):
    __slots__ = ('name', 'age')

s1 = Student2()
s.name = 'super'  # 绑定属性name
s.age = 25  # 绑定属性age
s.score = 99  # 绑定属性score
#  由于score没有放到__slots__中，所以不能绑定score属性，__slots__属性
#  仅对当前类的实例起作用，对继承的子类不起作用

# 使用@property   当绑定属性时如果直接把属性暴露出来，会导致没法检查参数，可以对值随便修改


# class Student(object):
#     def get_score(self):
#         return self.get_score
#
#     def set_score(self,value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer')
#         if value < 0 or value >100:
#             raise ValueError('score must betwwen 0~100')
#         self._score = value
#
#
# s = Student()
# s.set_score(60)
# print(s.get_score())
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 多层继承


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal):
    pass


class Bat(Mammal):
         pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')

# 多重继承是一个子类同时获取父类的多个功能
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass


# 在设计类的继承关系时，通常，主线都是单一继承下来的，
# 例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
# 通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，
# 再同时继承Runnable。这种设计通常称之为MixIn。

# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass




