# Enum 枚举类  每个常量都是class的一个唯一实例
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)   # value属性则是自动赋给成员的int常量，默认从1开始计数

# 更精确地控制枚举类型，可以从Enum派生出自定义类
from enum import Enum, unique


@unique   # @unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))

'''
总结：
Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
'''


# type
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
def fn(self, name='world'):   # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))

'''
要创建一个class对象，type()函数依次传入3个参数：
    1、class的名称；
    2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
注意;通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
     仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
     正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
     也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言
     运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上
     都是动态编译，会非常复杂
'''

# metaclass   创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”
# 当我们定义了类以后，就可以根据这个类创建出实例，
# 所以：先定义类，然后创建实例.但是如果我们想创建
# 出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    # 它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
    # 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定
    pass

'''
__new__()方法接收到的参数依次是：
    1、当前准备创建的类的对象；
    2、类的名字；
    3、类继承的父类集合；
    4、类的方法集合。
'''
# 测试
L = MyList()
L.add(1)
print(L)

# 对比
# 而普通的list没有add()方法
# L2 = list()
# L2.add(1)   这个会报错

'''
总结：
metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心
'''
# 水仙花
# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。
for i in range(10,1000):
    sum=0   # 各个位数的立方和
    temp=i
    while temp:
        sum=sum+(temp%10)**3   # 累加
        temp//=10   # 地板除
    if sum==i:
        print(i)








