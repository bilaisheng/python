"""
今天知识点：
1.函数参数
2.函数定义
3.函数调用
4.python重点几类函数参数 ，顺序，对函数调用的影响。
练习：用列表生成式实现[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]。函数实现斐波拉契数列
"""
"""
函数定义：
def 函数名（参数列表）：
    函数体
"""


def hello():
    print('Hello,world!')

hello()     # 输出Hello,world!


# 函数参数包含（必选参数，默认参数，可选参数，关键字参数，命名关键字）
# 必选参数：必须以正确的顺序传入函数，调用时的数量和声明时的一样。
def power(x):
    return x*x

print(power(3))  # 输出9  当调用power(x)函数时，必须传入一个且仅有一个参数x.


def power2(x, n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
print(power2(2, 3))  # 输出8 （调用有两个位置参数的函数时，传入两个按照位置顺序依次赋值，缺少参数就会报错。）


# 默认参数：调用函数时，如果没有传递参数，就会使用默认参数。
def power3(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

print(power3(4))  # 输出16 （n是默认参数，当n!=2时，必须传入n,当n=2时，可以不用再传入）


# 关键字参数：允许你将不定长度的键值对作为参数传递给一个函数，调用时的顺序可以和声明时的顺序不一样
# 使用**表示关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Bob', 13, city='beijing'))    # 输出name: Bob age: 13 other: {'city': 'beijing'}


# 可选参数：可选参数是传入的参数是可变的，可以是1个，可以是2个到任意个还可以是0个
# 在参数前面加一个*号就是可变参数
def calc(*numbers):
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n * n
    return sum1

print(calc(2, 4, 1))  # 输出21

# 命名关键字：如果入宫如果
