# 重点积累函数参数，顺序，对函数调用的影响

#pass 可以作为占位符，比如现在还没有想好怎么写函数的代码就可以先放一个pass让代码运行起来
def nep():
    pass

#使用 isinstance 为函数进行参数类型检查
def my_abc(x):
    if not isinstance(x,(int,float)):
        raise TypeError('错误的数据类型')
    if x >=0:
        return x
    else:
        return -x
print(my_abc(-2))

#使用函数返回多个值
#虽然表面上函数返回多个值，但是这只是假象，返回的是一个turple
import math  #导入数学相关包
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
print(move(100,100,60,math.pi/6))

#默认参数
'''
默认参数可以简化函数
设置默认参数的时候要注意一下几点：
    1、必选参数在前，默认参数在后
    2、当函数有多个参数时，吧变化大的参数放在前面，变化小的
       参数放在后面，变化小的参数可以作为默认参数
    3、当有多个默认参数的时候既可以按照书序调用，也可以不按
       顺序提供参数，这个时候需要把参数名一起带上
    4、默认参数必须指向不变对象，否则每次调用默认参数都会改变如 例子一
'''
# 函数传入多个值，可以在传入的值中设定默认值
# 例如计算想x^n
def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s * x
    return 'x的'+str(n)+'次方是： '+str(s)
print (power(5))  #默认输出5的平方
print (power(5,5))   #输出5的5次方

# 例子一
def test(L=[]):
    L.append('END')
    return  L
print ('第一次调用默认参数：',test())
print ('第二次调用默认参数：',test())

# 可变参数
'''
可变函数就是传入的参数个数是可以发生变化的，你可以向函数中传入
，也就是说一个或者多个的参数。
可变函数优化了函数中传入list和tuple的方式。可变函数的使用就是
在参数前面添加*
'''
# 计算阶乘
def test_calc(*number):
    sum = 0
    for i in number:
        sum = sum + i * i
    return sum
print (test_calc(1,2,3,4,5,6,7))
#向上面的函数中添加一个list
list = [1,2,3]
print ('如果传入的值是一个list或tuple的话直接在参数前面添加*：',test_calc(*list))

# 关键字参数
'''
可变参数允许你传入0个或者多个参数，这些可变参数在函数调用时
自动组装为一个tuple，而关键字参数允许你传入0个或人一个含参数名
的参数，这些参数在函数调用时自动组装为一个dict
说明：关键字参数在调用函数的时候除了需要传入必选参数外，还接受
传入任意个数的关键字参数
'''
# 定义一个person函数
def person(name, age, **kw):   # 还可以给这个人添加其他的属性，他们会自动的组装成dict
    print ('name: ', name, 'age: ', age,'其他：', kw)

'''
# 总结：
#     1、一个函数可以包含必选参数，默认参数，可变参数和关键字参数
#     2、调用的顺序是必选参数，默认参数，可变参数，关键字参数
# '''
#
# #实现倒序排序和冒泡排序
# list = [5,8,6,9,3,4,8,9,5,1,4]
# list_len = len(list)   #获取列表长度
# #倒叙排列
# l_len = list_len/2
# for i in range(l_len):
#     list[i],list[list_len-1-i] = list[list_len-1-i], list[i]
# print (list)
# #冒泡排序
# for i in range(list_len - 1):
#     for j in range(i,list_len):
#         if list[i] > list[j]:   #相邻两个比较
#             list[i],list[j] = list[j],list[i]
# print (list)

# #统计字符串字符个数，空格字符个数，数字字符个数，其他字符个数
# import string
# s=input('请输入想要统计的字符串:')
# letters = 0   #统计字符个数
# space = 0   #统计空格个数
# digit = 0   #统计数字个数
# others =0   #同价其他
# for ch in s:
#     #检测字符串是否只由字母组成
#     if ch.isalpha():
#         letters += 1
#     #检测是否是空格
#     elif ch.isspace():
#         space += 1
#     #检测是否是数字
#     elif ch.isdigit():
#         digit += 1
#     else:
#         others += 1
# print('字符个数为：',letters,'\n','空格个数为：', space,'\n' ,'数字个数为', digit, '\n','其他为：',others)
#
# #有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#                 print (i,j,k)
#
# #获取 100 以内的质数
# num=[];
# i=2
# for i in range(2,100): #质数大于1
#    j=2   #避免忽略2
#    for j in range(2,i):
#       if(i%j==0):
#          break
#    else:
#       num.append(i)
# print(num)
#
# #打印 max 个 斐波拉契数列
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b ,a + b
#         n = n + 1
#
# print(fib(10))
#
# #忽略大小写按照字母表进行排序
# def cmp_ignore_case(s1,s2):
#     u1 = s1.upper()
#     u2 = s2.upper()
#     if u1 < u2:
#         return 1
#     if u1 > u2:
#         return -1
#     return 0
#
# def test1():
#     a,b = 'B','A'
#     flag = cmp_ignore_case(a,b)
#     if flag > 0:
#         return a+b
#     if flag < 0:
#         return b+a
#     return '输入错误'
# print(test1())
# sorted(['D','A','C','B','F','G','E'],cmp_ignore_case)
#
# #把一个序列中的空字符串去掉
# def not_empty(s):
#     return s and s.strip()
# b = filter(not_empty,['A','','B','C','','D','','E','F'])
# print(b)




