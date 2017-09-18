# 函数参数
# 函数定义
# 函数调用
# python中的函数定义，使用和传参


note = '''
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

'''
def_str = '''\
    python中的函数以如下形式声明:
    def 函数名称([参数1，参数2，参数3......]):
        执行语句
    如：
    
    def helloWorld():
        print('hello')
    # 类似java中的main函数
    # 为了防止每次停止,后面不用该方法
    if __name__ == '_main__':
        helloWorld()

    输出：hello
    '''
print(def_str)


def helloworld():
    print('输出：hello')


print(helloworld())

print('''\
    ################################################

    函数可以带参数和返回值，参数将按从左到右的匹配，
    参数可设置默认值，当使用函数时没给相应的参数时，
    会按照默认值进行赋值

    ################################################
    ''')


def my_abs(x):
    if x <= 0:
        return -x
    else:
        return x

print(my_abs(-1))
print(my_abs(-1))

'''

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。
'''


'''
默认参数：

一是必选参数在前，默认参数在后，否则Python的解释器会报错；

二是设置默认参数。

把年龄和城市设为默认参数：
'''


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

# 可变参数：


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(100))


# 内置函数
# 绝对值或复数的模>>>>6
print(abs(-6))

# 接受一个迭代器，如果迭代器的所有元素都为真，那么返回True，否则返回False>>>>False
print(all([1, 0, 3, 6]))

# any()　　接受一个迭代器，如果迭代器里有一个元素为真，那么返回True,否则返回False
print(any([0, 0, 0, []]))  # >>>>False

# ascii()　　调用对象的__repr__()方法，获得该方法的返回值.
print(ascii([1,2,3,1,22,123]))  # >>>>>[1, 2, 3, 1, 22, 123]

# bin(), 将十进制转换为二进制
print(bin(10))  # >>>>>0b1010

# oct(),将十进制转换为八进制
print(oct(7))  # >>>>>>0o7

# hex(),将十进制转换为十六进制
print(hex(15))  # >>>>>>0xf

# bool()　　测试一个对象是True还是False.
print(bool([]))  # >>>>>False

# bytes()　　将一个字符串转换成字节类型

s = "apple"
v = bytes(s,encoding="utf-8")
print(v)  # >>>>>>b'apple'

# str()　　将字符类型/数值类型等转换为字符串类型
s = 100
print(type(s))  # >>>><class 'int'>
s = str(s)
print(type(s))  # >>>><class 'str'>

# challable()　　判断对象是否可以被调用，能被调用的对象就是一个callables对象，比如函数
print(callable(str))  # >>>>>True

'''
complie()　将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译。

compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

将source编译为代码或者AST对象。代码对象能过通过exec语句来执行或者eval()进行求值。

参数source：字符串或者AST（abstract syntax trees）对象。

参数filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。

参数model：指定编译代码的种类。可以指定'exec', 'eval', 'single'。

参数flag和dont_inherit：这两个参数为可选参数。
'''

s = "print('helloworld')"
r = compile(s, "<string>", "exec")
print(r)  # >>>>>>><code object <module> at 0x0000000000B426F0, file "<string>", line 1>

# complex()，创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。如果第一个参数是字符串，则不需要指定第二个参数。
print(complex("123"))  # >>>>(123+0j)

# dir()　　不带参数时返回当前范围内的变量，方法和定义的类型列表，带参数时返回参数的属性，方法列表。
print(dir())  # >>>>>['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'r', 's']

# divmod()　　分别取商和余数
print(divmod(10,3))  # >>>>>(3, 1)

# eval()　　1.将字符串str当成有效的表达式来求值并返回计算结果2.取出字符串中内容
s = "1 + 3 +5"
print(eval(s))  # >>>>>>9

'''
filter()　　过滤器，构造一个序列，等价于[ item for item in iterables if function(item)]，
在函数中设定过滤条件，逐一循环迭代器中的元素，将返回值为True时的元素留下，形成一个filter类型数据。

filter(function, iterable)

参数function：返回值为True或False的函数，可以为None。

参数iterable：序列或可迭代对象。
'''


def uno(x):
    return x > 10
v = filter(uno, [1, 11, 2, 45, 7, 6, 13])
print(v)  # >>>>><filter object at 0x0000000001143160>

# float()　　讲一个字符串或整数转换为浮点数。
print(float(11))  # >>>>>11.0

# format()　　格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法。
print("i am {0},age{1}".format("tom",18))  # >>>>>>i am tom,age18

# input()　　获取用户输入内容
# print(input("aaa"))  # >>>>>aaa  : 此处需要手工在控制台输入任意字符敲回车才可继续下面代码,故注释

# isinstance()　　检查对象是否是类的对象，返回True或False，isinstance(obj, cls)
# 检查obj是否是类cls的对象, 返回True或False


class Foo(object):
    pass
obj = Foo()
print(isinstance(obj, Foo))  # >>>>>True

# len()　　返回对象长度，参数可以是序列类型（字符串，元组或列表）或映射类型（如字典）
s = "ajljflajfl"
print(len(s))  # >>>>>10

'''
sorted()　　排序
列表排序，按数轴方向排
高阶函数，以绝对值大小排序
字符串排序，按照ASCII的大小排序
如果需要排序的是一个元组，则需要使用参数key，也就是关键字。
反向排序，reserve=True
'''
print(sorted([5, 2, 3, 1, 4]))