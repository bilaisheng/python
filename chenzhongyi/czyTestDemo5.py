# map 函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))   # Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list

# Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

# reduce 函数
'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
    reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
# 序列求和
from functools import reduce   # 导入reduce
def add(x, y):
    return x + y
a = reduce(add,[1,3,5,7,9])
print('a的值是：', a)
# 类似上面的求和函数可以用python的内置函数 sum()

# 写一个str 转换为 int 函数
from functools import reduce   # 导入reduce
def fn(x, y):
    return x * 10 + y
def char2num(x):
    # {}[]的形式可以将[]中的值按照{}里面的字典进行转化
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x]
a = reduce(fn,map(char2num,'26614925'))
print('有reduce和map组合的str转int的结果是：', a)

'''
 filter() 函数 --- 用于筛选
 filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数
 依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
# 删除一个list中的所有偶数只留下奇数
def is_odd(n):
    return n % 2 ==1
a = filter(is_odd, [1,2,3,4,5,6,7,8,9])
print(list(a))

# 一个序列中的空字符串删掉
def not_empty(a):
    return a and a.strip()   # strip()返回移除字符串头尾指定的字符生成的新字符串,默认空格
a = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(a)

# 用filter实现筛选素数
# 思路就是构建一个从2开始的序列，循环下去，例如得到2是一个素数，则把序列中2的
# 倍数删除，得到3是一个素数，同样把3的倍数删除，以此类推一直筛选下去
# 先构建一个从3开始生成器，并且是无限序列（因为确定了2是素数且2的倍数不是）
def _iter():
    n = 1
    while True:
        n = n + 2
        yield n   # 带有 yield 的函数在 Python 中被称之为 generator（生成器）

# 定义一个筛选函数
def _not_divisiable(n):
    return lambda x: x % n > 0
'''
lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体，用函数来表示为：
def g(x):
    return x+1
'''
# 定义一个生成器不断放回下一个素数
def primes():
    yield 2
    it = _iter()   # 初始化序列
    while True:
        n = next(it)   # 返回序列的第一个数
        yield  n
        it = filter(_not_divisiable,it)   # 构造新的序列

# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
for n in primes():
    if n <10:  # 打印1000以内的素数
        print(n)
    else:
        break

# Python内置的sorted()函数就可以对list进行排序 ,默认情况下，对字符串排序，是按照ASCII的大小比较的
a = sorted([36, 5, -12, 9, -21])
print(a)

# 它还可以接收一个key函数来实现自定义的排序，例如接受内置函数abs按绝对值大小排序
a = sorted([36, 5, -12, 9, -21], key=abs)
print(a)

# 对字符串进行排序（首字母）
a = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(a)
# 上面的例子如果想忽略大小写进行排序可以添加 key=str.lower，就是将所有的东西转变为小写或者大写再进行比较
#如果要进行反向排序，可以传入第三个参数  reverse=True
a = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(a)

# 高阶函数中返回一个函数  这种将函数作为返回值的结构叫做闭包结构
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,2,3,4,5,6,7,8,9)
print(f)
print(f())





