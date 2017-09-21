"""
面向对象编程：
公有属性和私有属性；属性装饰器，描述符；实例方法，静态方法，类方法

疑惑点：装饰器不懂
"""

# 定义类
# 类声明和函数声明很相似，头一行用class关键字来创建，接下来是一个作为它的定义代码体
class ClassName(object):
    'class documentation string' # '类文档字符串'
    # class_suite  # 类体

# 类属性
# 属性是属于一个对象的数据或者函数元素，可以通过我们熟悉的句点属性标识法来访问。
# 一些python类型，比如复数有数据属性（实部和虚部）
# 而另一些像列表和字典，拥有方法（函数属性）可以访问，这导致了一个属性链
# sys.stdout.write('foo')
# print(myModule.myClass.__doc__)
# myList.extend(map(upper,open('x').readlines()))
#尽量把需要用户传入的属性作为实例属性，而把同类都一样的属性作为类属性。
# 实例属性在每创造一个实例时都会初始化一遍，不同的实例的实例属性可能不同，不同实例的类属性都相同。从而减少内存。

# 公有属性：指的是所属的这个类的所有对象都可以访问的属性
class Person(object):
    nationality = 'CN'  # 定义公有属性

    def __init__(self, name, job, phone, address):
        self.name = name
        self.job = job
        self.phone = phone
        self.address = address

    def sayhi(self):
        print("hell,%s" % self.name)


p1 = Person('Bigberg', 'Doctor', '8833421', 'hz')
p2 = Person('Ashlex', 'Police', '8833232', 'bj')

print(p1.nationality)   # 输出CN
print(p2.nationality)   # 输出CN

# 公有属性的特性：我们不仅可以访问，还能改变公有属性
class Person(object):
    nationality = 'CN'  # 定义公有属性

    def __init__(self, name, job, phone, address):
        self.name = name
        self.job = job
        self.phone = phone
        self.address = address

    def sayhi(self):
        print("hell,%s" % self.name)


p1 = Person('Bigberg', 'Doctor', '8833421', 'hz')
p2 = Person('Ashlex', 'Police', '8833232', 'bj')

print(Person.nationality)  # 调用 公有属性
Person.nationality = 'us'  # 改变 公有属性
print(Person.nationality)  # 输出us
print(p1.nationality)      # 输出us
print(p1.nationality)      # 输出us
p1.nationality = 'jp'
print(Person.nationality)  # 输出us
print(p1.nationality)      # 输出jp

# 成员属性（实例属性）:存在于构造方法中
# Python中要声明私有属性，需要在属性前加上双下划线（但是结尾处不能有双下划线）
#  如：self.__a。然而这样的什么方式并不是真正私有，而是“伪私有”。
# python直接访问私有属性方式:实例化对象名._类名__私有属性名

class Person(object):
    def __init__(self, name, job, phone, address):
        self.name = name  # 成员属性，属于某个实例对象
        self.job = job
        self.phone = phone
        self.__address = address  # 私有属性

    def get_private(self):
        return self.__address

    def sayhi(self):
        print("hell,%s" % self.name)


p1 = Person('Bigberg', 'Doctor', '8833421', 'hz')
p2 = Person('Ashlex', 'Police', '8833232', 'bj')
print(p1.job, p2.job)   # 输出Doctor Police
print(p2._Person__address)  #访问私有属性


# 装饰器：其实就是一个以函数作为参数并返回一个替换函数的可执行函数

def outer(some_func):
    def inner():
        print("before some_func")
        ret = some_func() # 1
        return ret + 1
    return inner


def foo():
    return 1
decorated = outer(foo) # 2
decorated()

# 根据鸭子模型理论，只要具有__get__方法的类就是描述符类。
# 如果一个类中具有__get__和__set__两个方法，那么就是数据描述符，。
# 如果一个类中只有__get__方法，那么是非数据描述符。
#
# __get__：当我们用类或者实例来调用该属性时，Python会返回__get__函数的结果。
# __set__：当我们用实例来设置属性值时，Python会调用该函数。对类没有限制作用。
# __delete__：当我们用实例试图删除该属性时，Python会调用该函数。对类没有限制作用。

# 非数据描述类

class Desc:
    def __init__(self, value=22):
        self.value= value


    def __get__(self, ins, cls):
        return self.value

class A:
    v=Desc()
a=A()
print(a.v) #由于实例中没有v属性，所以找到了类的属性，而类的属性是一个描述符类实例，所以调用其__get__方法的结果。
print(a.__dict__) #实例的__dict__空空如也。
print(A.__dict__)  #类的__dict__中确实存在v属性，且是一个Desc object对象。
a.v=30  #我们通过实例设置v属性
print(a.__dict__ )     #我们发现实例的__dict__中存入了我们刚才设置的属性
print(A.__dict__)  #类的__dict__没有发生任何变化
print(a.v)    #访问到了a.__dict__中的内容。
del a.v         #我们删除实例的属性v后发现居然还是可以调用a.v，返回的是我们设置之前的值。
print(a.v)  # 22
print(A.__dict__)     #和前面一样，没有发生变化。

# 通过上面的测试，我们发现非数据描述类有如下特点：
# 如果实例__dict__没有设置同名属性，那么返回描述类的__get__方法的结果。
# 如果实例__dict__中存在同名属性，那么返回实例__dict__中的内容。
# 对我们设置实例的__dict__中的行为并不做阻止。所以我说这是查看级别的描述类。


# 数据描述类

class Desc:
    def __init__(self, value=22):
        self.value= value


    def __get__(self, ins, cls):
        return self.value


    def __set__(self, ins, value):
        self.value=value
        #raise AttributeError

class A:
    v=Desc()
a=A()


# 实例方法就是类的实例能够使用的方法
class Foo:
    def __init__(self, name):
        self.name = name


    def hi(self):
        print(self.name)
if __name__ == '__main__':
    foo01 = Foo('letian')
    foo01.hi()
    print(type(Foo))
    print(type(foo01))
    print(id(foo01))
    print(id(Foo))

# 静态方法是一种普通函数，就位于类定义的命名空间中，它不会对任何实例类型进行操作。
# 使用装饰器@staticmethod定义静态方法。类对象和实例都可以调用静态方法：
class Foo:
    def __init__(self, name):
        self.name = name


    def hi(self):
        print(self.name)


    @staticmethod
    def add(a, b):
        print(a + b)
if __name__ == '__main__':
    foo01 = Foo('letian')
    foo01.hi()
    foo01.add(1,2)
    Foo.add(1, 2)

# 类方法是将类本身作为对象进行操作的方法。
# 类方法使用@classmethod装饰器定义，其第一个参数是类，约定写为cls。
# 类对象和实例都可以调用类方法：
class Foo:
    name = 'letian '
    @classmethod
    def hi(cls, x):
        print(cls.name * x)
if __name__ == '__main__':
    foo01 = Foo()
    foo01.hi(2)
    Foo.hi(3)