# 1、字符串：序列操作、编写字符串的其他方法、模式匹配
S='abcd'
print(len(S))

S[0]   # 'a'
S[1]   # 'b'
S[-1]  # 'd'
S[1,2]  # bc
S[1:]  # bcd
S[:2]  # abc
S[:-1] # abc
S[:] # abcd
S +  'efg' #abcdefg
S * 3 # abcdefg abcdefg abcdefg

# 特定函数
# find函数 没有找到时返回-1
S.find('b') #  1
# replace（）
S.replace('a','XYZ')

# upper() 大写
S.upper()

# isalpha() 测试字符串的内容 ，True ，False
S.isalpha();
# S.rstrip();去空
S.rstrip();
# 帮助文档 help
help(S.replace)

#编写字符的其他方法
s = 'A\nb\tc'
len(s) # 5

ord('\n')  # 10
# r 表示后面的为非转义
print(r'//t//t//n')

# 模式匹配
# 搜索子字符串，这个子字符串以“hello”开始，后面跟着0空格或几个空格或制表符，接着有任意字符并将其保存到group中，最后以world结尾。
import re
match = re.match('hello[ \t]*(.*)world','hello   python world')
match.group(1) # 输出'python '

match = re.match('/(.*)/(.*)/(.*)','/user/home/lumjack')
match.groups()  #输出（'user','home','lumberjack'）


# 2、列表（列表的基本操作）

#序列操作
l = [123,'spam',1.22]
# 求列表长度
len(l)
# 第一个元素
l[0]
# 倒数第一个之前的元素
l[:-1]
# 把一个list 放入另一个 但是不能改变原list的

l+[1,2,3]
# 类型特定的操作 不能改变原list
# 删除对应位置的元素 list从0开始。
l.pop(2)
# 添加元素到末尾
l.append('4897')
# 任意位置插入元素
l.insert('22')
# 任意位置移除元素
l.remove(2)

# 排序
m = [9,5,7,4,6]
m.sort()
# 元素倒转
m.reverse()
# 嵌套
n = [[1,2,3],[4,5,6],[7,8,9]]
print(n[1])
print[n[1][2]]
# 列表解析
col2=[row[1] for row in n]
# col2 [2,5,8] 实现矩阵操作
[row[1] + 1 for row in n]
[row[1] for row in n if row[1] % 2 == 0]

diag = [n [i][i] for i in [0,1,2]]
doubles = [c * 2 for c in 'spam']

# 利用sum函数 转化为元组 或者字典
g = (sum(row) for row in n)
next(g) #  6
next(g) # 15
 # 对各行的统计
list(map(sum,n))
print(list(map(sum,n))) # [6,15,24]
{sum(row) for row in n}
{i:sum(n[i]) for i in range(3)}
# 列表、集合和字典都可以解析创建






# 3、打印九九乘法口诀和循环输出26个字母(并将字母的Ascall码同时输出)
