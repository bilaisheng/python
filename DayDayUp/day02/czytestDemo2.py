import os
import sys
#获取当前所工作的目录的名称
#得到D:\AllWorkSpace\python_space\python\DayDayUp\day02
f = os.getcwd()
print(f)
#打印系统平台的名称
print(sys.platform)
#range(1,10)为1——9
#打印九九乘法表
print('第一种方法：')
for i in range(1,10):
    for a in range(1,i+1):
        re = str(i*a)  #将相乘结果转换成str用于拼接
        rs = str(i)+'*'+str(a)+'='+re
        #end为结束后追加的内容
        print(rs,end='\t')
    print('\n')

print('第二种方法：')
for i in range(1, 10):
    for j in range(1, i+1):
        # %前为占位符 后面括号中参数对应占位符位置, end 结束后追加的内容
        print("%d*%d=%d" % (i, j, i*j), end="\t")
    print("")

print('第三种方法：')
i = 1
while i < 10:
    if i == 1:
      j = i
      print("%d*%d=%d" % (i, j, i * j), end="\t")
      i = i + 1
    else:
        j = 1
        while j < i+1:
            print("%d*%d=%d" % (i, j, i * j), end="\t")
            j = j + 1
        i += 1
    print("")

'''
常用列表操作方法
    1、list.append():追加成员    
    2、list.count(x):计算列表中参数x出现的次数    
    3、list.extend(L):向列表中追加另一个列表L    
    4、list.index(x):获得参数x在列表中的位置    
    5、list.insert():向列表中插入数据    
    6、list.pop():删除列表中的成员（通过下标删除）    
    7、list.remove():删除列表中的成员（直接删除）    
    8、list.reverse():将列表中成员的顺序颠倒    
    9、list.sort():将列表中成员排序
'''
# 列表(List)
#定义一个空列表
list=[]

#想列表中添加数据 append()方法，默认在末尾追加，
list.append('A')
list.append('B')
print(list)

#若想在特定的位置插入数据可以用 insert（）
list.insert(1,'C')
print(list)

#计算list中某个元素出现的次数
list.count('A')
print(list.count('A'))

#向列表中添加一个列表 默认在末尾追加
list.extend(['E','F','G'])
print(list)

#删除list中的元素 pop() 根据下标 默认删除最后一个 可以指定位置(如果打印的话可以得到具体删除的那个元素)
list.pop()
print(list)
print(list.pop(4))

#删除列表中具体的元素 remove
list.remove('A')
print(list)

#获得元素在list中的位置
print(list.index('B'))

#颠倒列表的顺序
list.reverse()
print(list)

#将list的成员重新排序
list.sort()
print(list[:2])

'''
    tuple 与list 的相同之处
    1、定义 tuple 与定义list的方式相同,除了整个元素集用小括号包围的而不是方括号
    2、tuple的元素与list一样按定义的次序进行排序 tuple的索引与list一样从0开始,所以
    3、一个非空的tuple的一个元素总是t[0]
    4、负数索引与list一样从tuple的尾部开始计数
    5、与list一样分片(slice)也可以使用 .注意当分割一个list时,会得到一个新的list;当分割
    所以当分割一个tuple时,会得到一个新的tuple
    
    tuple不存在的方法
    1、不能从一个tuple增加元素。所以没有append 和extend方法
    2、不能用tuple删除元素,所以没有remove和pop方法 但是经tuple合并
    3、然而可以使用index 来查看一个元素是否存在tuple中
    
    使用tuple的好处
    1、tuple比list操作速度快.如果定义了一个值的常量集,并且唯一要用它做的是不断地遍历
    则用tuple代替list
    2、如果对不需要修改的数据进行"写保护",它可以使代码更安全.使用tuple而不是list如同拥有一个
    隐含的assert语句,说明这一数据是常量.如果必须要修改这些值.可以把tuple转换list
    的转换
    3、虽然tuple中的元素不可变，但是可以嵌套可变的元素

'''

'''
    元祖常用的方法：
        1、count() 统计元祖中某个元素的个数
        2、index() 获取元素在元祖中的位置
'''
# 元祖(Tuple)
#创建一个空元祖
tt = ('a','b','c','d','e','f','g','h','i')

#统计元祖中某元素的个数
num = tt.count('a')
print(num)

#获取元素在元祖中位置
print(tt.index('a'))

#合并两个元祖
tt = tt + ('j','k')
print(tt)

#将元祖的内容重复N次成一个新的元祖
tt = tt * 2
print(tt)

#将元祖切片
print(tt[:3])

'''
    set集合，是一个无序且不重复的元素集合。所以
    无法像list和tuple一样用索引去取值
'''
# 集合(Sets)
#创建空集合  两种创建方法
ss = set()

#创建空集合时，只能用set(),如果用第二种方法s={}，创建的实际上是一个空字典 可以通过type打印验证
s = {}
print(type(s))

#增加元素
ss.add('甲')
print(ss)

#在ss中添加多项
print(ss.update(['乙','丙','丁']))

#删除集合中的元素,有几种方法
ss.remove('丁')
print(ss)
ss.discard('丁') #如果集合中有‘丁’则删除
ss.pop()  #删除并且返回 set “ss”中的一个不确定的元素, 如果为空则引发 KeyError
ss.clear() #删除所有元素
print(ss)
#集合的计算
ss = set('i love China')
s = {'C','H','i','n','a',}
#交集
ss.intersection(s)
print(ss & s)
#并集
s.union(ss)
print(ss | s)
#差集
ss.difference(s)
print(ss - s)
#对称差集（项在ss或s中，但不会同时出现在二者中）
ss.symmetric_difference(s)
print(ss ^ s)

#判断是不是包含关系
s.issubset(ss)  # ss >= s
ss.issuperset(s)

#去重
s = [1,1,2,5,3,6,4,4,8,7,9,2]
ss = set(s)
print(ss)

#判断集合中是否存在或不存在某个元素
1 in s
'甲' not in s


# 字典(Dictionary)
