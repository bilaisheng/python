# 面向对象编程：
# 公有属性和私有属性；属性装饰器，描述符；实例方法，静态方法，类方法


# 方法：
class Dog(object):
    country = 'JP'  # 全局变量，通过类修改后，所有对象全改，通过对象修改只是单个对象改了

    def __init__(self,name): #构造函数
        self.NAME = name #成员属性
        # * 私有属性外部不能直接访问,两个下划线定义，属于该对象内部私有。
        self.__heart = "Normal"

    def sayhi(self): # 方法
        print('hello, I am a dog',self.NAME)

# 复制代码
# self表示对象本身，NAME为类的成员属性

d1 = Dog("a") # Dog(d,"a")
d2 = Dog("b")
print(d1.country, d2.country)  # 所有的成员变量都可以访问


class dog(object):

    nationality = "AM"  # 定义公有属性

    def __init__(self, name):
        self.name = name


d1 = dog("hello")
d2 = dog("beijing")
print(dog.nationality)  # 访问公有属性
dog.nationality = "US"  # 修改公有属性
print(dog.nationality)

class dog(object):

    nationality = "AU"

    def __init__(self, name):
        self.name = name


d1 = dog("black")
d2 = dog("white")
print("firsthand change...")
print(d1.nationality, d2.nationality)
print("brfore change ...")
d1.nationality = "CN"  # 对象d1修改公共属性得值
d2.nationality = "CN11"  # 对象d1修改公共属性得值
print(d1.nationality, d2.nationality)
print("after change ....")
dog.nationality = "US"  # dog类本省修改公共属性的值
print(d1.nationality, d2.nationality)   # d1对象的公共属性值没有随着类本身的公共属性值修改而修改


# # 私有属性
class Students():
    #  只允许拥有私有的name和score属性
    __slots__ = ('__name', '__score')

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    # @Property就是将成员函数的调用变成属性赋值。
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name


    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,score):
        self.__score = score

    def __str__(self):
        return '姓名 ' + self.__name + ' \n分数' + str(self.__score)
# if __name__ == 'main': 下的代码只有在文件作为脚本直接执行
if __name__ == '__main__':
    cj=Students('王五',100)
    print(cj.name)
    print(cj.score)
    cj.score=98
    cj.name ='一一'
    print(cj.score)
    print(cj)


# 装饰器
def dec_1(func):
    def wrapper(num1, num2):

        # --- 附加功能 ---
        if num2 == 0:
            print("num2 值不能为0")

        return func(num1, num2)
    return wrapper


def now():
    print('2017-09-20')
f = now
f()
# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)


@dec_1   # (sum = dec(sum))
def sum_1(num1, num2):
    return num1 + num2

print(sum_1(5, 3))  # => 8

# 类方法
# @classmethod
# def classget(cls):
# print(cls.x)
# 只能调用类属性 ,类对象和实例都可以调用静态方法
#
# 静态方法
# @staticmethod
# def add(a, b):
#      print (a + b)
# 类对象和实例都可以调用静态方法


class Foo:

    def func(self):
        print("object method")

    @classmethod
    def cfunc(cls):
        print("class method")

    @staticmethod
    def sfunc(a, b):
        print("static method:", a, " + ", b, "=", a + b)


if __name__ == '__main__':
    foo = Foo()

    # instance method can be called by object and class name
    foo.func()
    Foo.func(foo)

    # both instance and class can call class method
    foo.cfunc()
    Foo.cfunc()

    # both instance and class can call static method
    Foo.sfunc(10, 20)
    foo.sfunc(50, 100)

