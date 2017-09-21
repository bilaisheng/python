# 面向对象编程：公有属性和私有属性；属性装饰器，描述符；实例方法，静态方法，类方法


# class dog(object):
#
#     nationality = "JP"  # 定义公有属性nationality
#
#     def __init__(self, name):
#         self.name = name
#
#
# d1 = dog("alex")
# d2 = dog("sanjiang")
# print(d1.nationality, d2.nationality)  # 所有的成员变量都可以访问


# class dog(object):
#
#     nationality = "JP"  # 定义公有属性
#
#     def __init__(self, name):
#         self.name = name
#
#
# d1 = dog("alex")
# d2 = dog("sanjiang")
# print(dog.nationality)  # 访问公有属性
# dog.nationality = "US"  # 修改公有属性
# print(dog.nationality)


# class dog(object):
#
#     nationality = "JP"
#
#     def __init__(self, name):
#         self.name = name
#
#
# d1 = dog("alex")
# d2 = dog("sanjiang")
# print("firsthand change...")
# print(d1.nationality, d2.nationality)
# print("brfore change ...")
# d1.nationality = "CN"  # 对象的d1修改公共属性得值
# print(d1.nationality, d2.nationality)
# print("after change ....")
# dog.nationality = "US"  # dog类本省修改公共属性的值
# print(d1.nationality, d2.nationality)   # d1对象的公共属性值没有随着类本身的公共属性值修改而修改


# 私有属性


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

def dec_1(func):
    def wrapper(num1, num2):

        # --- 附加功能 ---
        if num2 == 0:
            print("num2 值不能为0")

        return func(num1, num2)
    return wrapper

# 使用@语法的方式


@dec_1   # (sum = dec(sum))
def sum_1(num1, num2):
    return num1 + num2

print(sum_1(5, 3))  # => 8

# 能接收任何参数的通用装饰器


def dec_2(func):
    def wrapper(*arg, **kwargs):

        # --- 附加功能 ---
        print("loging i ...")

        return func(*arg, **kwargs)
    return wrapper

@dec_2
def average_2(num1, num2):
    return num1 / num2

print(average_2(5, 3))  # => loging i ... => 1.6666666666666667


# 能接收不同参数的装饰器


def auth(auth_type):  # 在外面套一层
    def dec_3(func):
        def wrapper(*arg, **kwargs):
            # --- 附加功能 ---
            if auth_type == "admin":
                print("你是管理员")
            elif auth_type == "user":
                print("你是普通用户")
            else:
                print("你是外星人吗?")

            return func(*arg, **kwargs)
        return wrapper
    return dec_3


# 普通调用方式
@auth(auth_type="admin")
def average_3(*arg):
    return sum(arg) / len(arg)

print(average_3(1, 2, 3, 4, 5))  # => 你是管理员 => 3.0


# 使用多个装饰器
@dec_1
@dec_2
@auth(auth_type="admin")
def average_2(num1, num2):
    return num1 / num2

# 执行顺序dec_1 => dec_2 => auth => average_2
print(average_2(5, 3))  # => loging i ... => 你是管理员 => 1.6666666666666667


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