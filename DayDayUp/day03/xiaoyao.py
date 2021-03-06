# 函数定义
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
# 我们以自定义一个求绝对值的my_abs函数为例：


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-3))  # 输出调用函数my_abs（）以后的值
'''
    函数可以带参数和返回值，参数将按从左到右的匹配，
    参数可设置默认值，当使用函数时没给相应的参数时，
    会按照默认值进行赋值
'''


# 定义一个空函数
def nop():
    pass  # pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来


# 函数参数
def power(x):  # 定义一个计算x2的函数：
    return x * x
# 当我们调用power函数时，必须传入有且仅有的一个参数x：
p = power(5)
print(p)


def power(x,n=2):  # 计算x的任意n次方
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
# 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数n，导致旧的代码因为缺少一个参数而无法正常调用：
# 由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
# 当我们调用power(5)时，相当于调用power(5, 2)：而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)
print(power(5))
print(power(5,3))
'''
  设置默认参数时，有几点要注意：

  一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

  二是如何设置默认参数。 
'''


# 把年龄和性别设置为默认参数
def enroll(name, gender='男', age=6):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)


# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3]))
print(calc((1, 2, 3)))

__author__ = "bilaisheng"
if __name__ == "__main__":
    print(calc([1, 2, 3]))


# 把def calc(numbers):改为可变参数为：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(100))


# 关键字参数：允许你将不定长度的键值对作为参数传递给一个函数，调用时的顺序可以和声明时的顺序不一样
# 使用**表示关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Bob', 13, city='beijing'))    # 输出name: Bob age: 13 other: {'city': 'beijing'}

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

s = "banana"
v = bytes(s,encoding="utf-8")
print(v)  # >>>>>>b'banana'

# divmod()　　分别取商和余数
print(divmod(9,3))  # >>>>>(3, 1)

# eval()　　1.将字符串s当成有效的表达式来求值并返回计算结果2.取出字符串中内容
s = "1 + 3 +5"
print(eval(s))  # >>>>>>9

# 将值转换为整形
print(int('123'))
print(int(12.34))  # >>>>>>12

# 将值转换为float
print(float('12.34'))  # >>>>>>12.34
print(float(11))  # >>>>>11.0

# 将数字转换为字符
print(str(1.23))  # >>>>>>'1.23'

# 将其他数据转换为bool型
print(bool(1))  # >>>>>>True
print(bool(''))  # >>>>>>False

# len()　　返回对象长度，参数可以是序列类型（字符串，元组或列表）或映射类型（如字典）
s = "ahigutfiyuioyhl"
print(len(s))  # >>>>>15

'''
sorted()　　排序
字符串排序，按照ASCII的大小排序
如果需要排序的是一个元组，则需要使用参数key，也就是关键字。
反向排序，reserve=True
'''
print(sorted([5, 2, 3, 1, 4]))


'''
所有参数（自变量）在Python里都是按引用传递。
如果你在函数里修改了参数，那么在调用这个函数的函数里，
原始的参数也被改变了
'''
# 修改列表的值


def change(list):
    "修改传入的列表"
    list.append([1,2,3,4])
    print("函数内取值: ", list)
    return

# 调用change函数
list = [10,20,30]
change(list)
print("函数外取值: ", list)
#  传入函数的和在末尾添加新内容的对象用的是同一个引用。故输出结果如下：
#  函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
#  函数外取值:  [10, 20, 30, [1, 2, 3, 4]]

'''
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。
'''
total = 0;  # This is global variable.


def sum(arg1, arg2):  # 返回2个参数的和.
    total = arg1 + arg2  # total在这里是局部变量.
    print("Inside the function local total : ", total)
    return total

# 调用sum函数
sum(10, 20)
print("Outside the function global total : ", total)
# 以上实例输出结果：
# Inside the function local total :  30
# Outside the function global total :  0

# complie()　将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译。`
s = "print('helloworld')"
r = compile(s, "<string>", "exec")
print(r)  # >>>>>>><code object <module> at 0x0000000000B426F0, file "<string>", line 1>

# 函数声明只有3种类型, arg, *arg , **arg
# *arg 和 **arg可以为空值.
# arg, *arg和**arg作用举例
def test2(a,*b,**c):
    print(a,b,c)

# *arg 和 **arg可以不传递参数
print(test2(1)) # >>>>>>>1 () {}

# arg必须传递参数
print(test2())  # 运行报错
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: test2() takes at least 1 argument (0 given)




