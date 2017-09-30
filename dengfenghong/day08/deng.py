# 1、了解定制类
# 类似__slots__这种的变量或者函数名，这是用来限制函数绑定参数的
# __str__


class Person(object):
    def __init__(self, name):
        self.name = name
print(Person('super'))  # 打印出暴露内部重要数据
# 直接显示调用的是__repr__() 返回程序开发者看到的字符，是为调试服务的
# __str__()返回用户看到的字符串


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
print(Student('super'))

# __iter__
# 如果一个类想被用于for   in 循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# python的for循环会不断调试改迭代对象的__next__(）方法拿到下一个值，直到遇到StopIteration错误退出


class Fib(object):
    def __init__(self):
        self.a,self.b = 0, 1

    def __iter__(self):
        return  self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a
# for n in Fib():
#     print(n)

# 虽然Fib实例循环，看起来和list像，但是不能去某个元素，要按照下标一样取元素，需要实现__getitem__()


class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
print(f[0])

print(list(range(100))[5: 100])
# print(f[0: 5])


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

f2 = Fib()
print(f2[0: 5])
# 一般情况下，当我们调用类的方法时或属性，若不存在就会报错
s = Student()
print(s.name)
print(s.score)  # 报错


class Student1(object):
    def __init__(self):
        self.name = 'super'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

# 只有没有找到属性的情况下，才会调用__getattr__
s2 = Student()
print(s.name)
print(s.score)
# 2、使用枚举类
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# 若需要更精确的枚举类型 @unique 保证没有重复值
from enum import  Enum,unique
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(day1 == Weekday.Mon)
print(Weekday(1))
# 3、使用元类
# type() 函数可以查看一个类型或变量的类型

# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# from hello import Hello
# h = Hello()
# h.hello()
print(type(Hello))

# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class Mylist(list, metaclass= ListMetaclass):
    pass
L = Mylist()
L.add(1)
print(L)


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):

    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
