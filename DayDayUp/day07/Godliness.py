'''
使用__slots__
使用@property
多重继承

leetcode:Longest Common Prefix

java环境搭建 工具 Myeclipse 2017 CI 8 , java9  tomcat 9

'''


class Student(object):
    pass

# 绑定属性
s = Student()
s.name = 'Nichael'  # 动态给实例绑定一个属性
print(s.name)

# 给实例绑定一个方法
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)   # 测试结果

# 给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()  # 创建新的实例
# s2.set_age(25)  # 尝试调用方法，此处报错

# 给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
s2.set_score(90)
print(s.score)
print(s2.score)

# 想要限制实例的属性怎么办？
# 比如，只允许对Student实例添加name和age属性。
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性

# class Student(object):
#     __slots__ = ('name', 'age') # 用tuple 定义允许绑定的属性名称
#
# s = Student() # 差个内奸新的实例
# s.name = 'godliness' # 绑定属性 name
# s.age = 35  # 绑定属性 age
# # s.score = 90  # 绑定属性 score 此处报错
# '''
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
# '''
#
# class GraduateStudent(Student):
#     pass
#
# g = GraduateStudent()
# g.score = 9999
# print(g.score)
#
# # 使用@property
# class Student(object):
#
#     def get_score(self):
#         return  self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score  must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must be betweeen 0~100!')
#         self._score = value
# # 对任意的Student实例进行操作，就不能随心所欲地设置score了：
# s = Student()
# s.set_score(60)
# print(s.get_score())

# s.set_score(9999)
# print(s.get_score())


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score  must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must be betweeen 0~100!')
        self._score = value



s = Student()
s.score = 60  # OK，实际转化为s.set_score(60)
print(s.score)  # OK，实际转化为s.get_score()

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 只读属性
    @property
    def age(self):
        return 2017 - self._birth


# 多重继承
class Animal(object):
    pass

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass

# 动物再加上Runnable和Flyable的功能


class Runnable(object):
    def run(self):
        print('Running ....')


class Flyable(object):
    print('Flying ....')


class Dog(Mammal, Runnable):
    pass


class Bat(Bird, Flyable):
    pass


