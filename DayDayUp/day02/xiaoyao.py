# 1、字符串：序列操作、编写字符串的其他方法、模式匹配
# 去空格及特殊符号
# lstrip：删除左边的空格
# rstrip：删除右边的空格
# strip：删除两端的空格
s = "   changjie   l "
print(s.lstrip())
print(s.rstrip())
print(s.strip())
# 复制字符串
str1 = 'occupation'
str2 = str1
str1 = 'occupation2'
print(str1,str2)
# 连接字符串
str1 = 'my'
str2 = 'job'
str1 += str2
print(str1)
# 查找字符 <0 为未找到
str1 = 'meaning'
str2 = 'n'
n = str1.index(str2) # 若要查找字符出现多次，则输出最早出现的该字符的下标
print(n)
# 比较字符串
# Python 3.X 的版本中已经没有 cmp 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象，包含的方法有：
# operator.lt(a, b) 等价于a<b
# operator.le(a, b) 等价于a<=b
# operator.eq(a, b)  等价于a=b
# operator.ne(a, b)  等价于a!=b
# operator.ge(a, b)  等价于a>=b
# operator.gt(a, b)  等价于a>b
import operator
str1 = 'player'
str2 = 'play'
print(operator.gt(str1,str2))
# 字符串长度
str1 = 'chang'
print(len(str1))
# 扫描字符串是否包含指定的字符
myStr1 = 'professional'
myStr2 = 'fess'
print(len(myStr1 and myStr2)) # 如果myStr1的值为true的话，则返回myStr2的值， len取得myStr2长度
# 将字符串中的大小写转换
sStr1 = 'upStAir'
# sStr1 = sStr1.upper() # 转大写
# sStr1 = sStr1.lower() # 转小写
# sStr1 = sStr1.swapcase()  # 大小写互换
sStr1 = sStr1.capitalize()  # 首字母大写
print(sStr1)
# 追加指定长度的字符串
sStr1 = 'drink'
sStr2 = 'water234'
sStr1 += sStr2[0:5]
print(sStr1)
# 字符串指定长度比较
sStr1 = 'drink'
sStr2 = 'drink234'
n = 5
print(operator.eq(sStr1[0:n],sStr2[0:n]))
# 复制指定长度的字符
sStr1 = ''
sStr2 = 'drink234'
n = 4
sStr1 = sStr2[0:n]
print(sStr1)
# 将字符串前n个字符替换为指定的字符
sStr1 = 'grape'
ch = 'c'
n = 3
sStr1 = n*ch + sStr1[n:]
print(sStr1)
# 扫描字符串
sStr1 = 'abcdrgjh'
sStr2 = 'caj'
n = -1
for c in sStr2:
    if c in sStr1:
        n = sStr1.index(c)
        break
print(n)
# 翻转字符串
sStr1 = 'chang'
sStr1 = sStr1[::-1]
print(sStr1)
# 查找字符串
sStr1 = 'changjie'
sStr2 = 'jie'
print(sStr1.find(sStr2))
# 分割字符串
sStr1 = 'a,cd,erf,w,qe'
sStr2 = ','
sStr1 = sStr1[sStr1.find(sStr2)+1:]
print(sStr1)
# 或者
s = 'ab,cde,fgh,ijk'
print(s.split(' '))  # 将string转list，以空格区分
# 连接字符串
sStr1 = ' '
sStr2 = ['banana','apple','pear','grape']
print(sStr1.join(sStr2))  # 将list转string，以空格连接
#  S.find(substring, [start [,end]]) #可指范围查找子串，返回索引值，否则返回-1
#   S.rfind(substring,[start [,end]]) ##返回S中最后出现的substr的第一个字母的标号，如果S中没有substring则返回-1，也就是说从右边算起的第一次出现的ssubstring的首字母标号
#   S.index(substring,[start [,end]]) #同find，只是找不到产生ValueError异常
#    S.rindex(substring,[start [,end]])#同上反向查找
#    S.count(substring,[start [,end]]) #返回找到子串的个数
sStr1 = 'ab,cde,fgh,ijk'
sStr2 = 'qw'
print(sStr1.find(sStr2,0,10))
print(sStr1.rfind(sStr2,10,0))
# print(sStr1.index(sStr2,0,10))
# print(sStr1.rindex(sStr2))
# print(sStr1.count(sStr2))
# S.replace(oldstr, newstr, [count])
# 把S中的oldstar替换为newstr，count为替换次数。这是替换的通用形式，还有一些函数进行特殊字符的替换
sStr1 = 'abcdefg'
sStr2 = 'w'
print(sStr1.replace('d',sStr2,1))
# 将字符串转为int，float
sStr1 = '11'
print(int(sStr1))
print(float(sStr1))
# 引入正则表达式包
import re
# findall(rule , target [,flag] )在目标字符串中查找符合规则的所有字符串
sStr1 = '123abcd789jkabhg'
print(re.findall(r'ab',sStr1))
# 正则表达式基本规则
'''
‘[‘  ‘]’ 字符集合设定符
 [a-zA-Z]来指定所以英文字母的大小写
 [^a-zA-Z]表明不匹配所有英文字母
 如果 ‘^’不在开头，则它就不再是表示取非，而表示其本身，如[a-z^A-Z]表明匹配所有的英文字母和字符’^’。
 ‘|’    或规则: 只要满足其中之一就可以匹配。比如:[a-zA-Z]|[0-9] 表示满足数字或字母就可以匹配，这个规则等价于 [a-zA-Z0-9]
 ‘‘/d’ 匹配数字 
 /D’ 匹配非数字 ‘
 /w’ 匹配字母和数字 
 ‘/W’ 匹配非英文字母和数字
'''
'''
    re包中常用方法
    search: 搜索整个字符串，直到发现符合的子字符串。
    match:从头开始检查字符串是否符合正则表达式。必须从字符串的第一个字符开始就相符。
    sub: 在string中利用正则变换pattern进行搜索，对于搜索到的字符串，用另一字符串replacement替换。返回替换后的字符串。
    split: 根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回
    findall: 根据正则表达式搜索字符串，将所有符合的子字符串放在一给表(list)中返回
    compile: 可以把正则表达式编译成一个正则表达式对象。
'''
'''
匹配中文字符的正则表达式： [/u4e00-/u9fa5]
    匹配双字节字符(包括汉字在内)：[^/x00-/xff]
    匹配空行的正则表达式：/n[/s| ]*/r
    匹配HTML标记的正则表达式：/<(.*)>.*<///1>|<(.*) //>/
    匹配首尾空格的正则表达式：(^/s*)|(/s*$)
    匹配Email地址的正则表达式：/w+([-+.]/w+)*@/w+([-.]/w+)*/./w+([-.]/w+)*
    匹配网址URL的正则表达式：^[a-zA-z]+://(//w+(-//w+)*)(//.(//w+(-//w+)*))*(//?//S*)?$
    匹配帐号是否合法(字母开头，允许5-16字节，允许字母数字下划线)：^[a-zA-Z][a-zA-Z0-9_]{4,15}$
    匹配国内电话号码：(/d{3}-|/d{4}-)?(/d{8}|/d{7})?
'''
sStr1 = 'I have a dog,I have a cat'
print(re.findall('I have a (?:dog|cat)', sStr1))
print(re.findall( r'I have a dog|cat', sStr1))
# ‘.’    匹配所有字符 匹配除换行符’/n’外的所有字符。
s='123 /n456 /n789'
print(re.findall('([0-9]*\d+)',s))
print(re.findall('.+' , s ))
# ‘/d’ 匹配数字
sStr1='123adsdfk'
ret = re.findall('\d',sStr1)
print(str(ret))

# search方法 re.search 扫描整个字符串并返回第一个成功的匹配。
sStr1 = 'changjiehelo'
sStr2 = 'he'
print(re.search(sStr2,sStr1))

phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)

# 匹配出所有的整数
digit = '31,-3,gh,-2.5,7,asdf'
# ret = re.findall(r"'(-*\d+)'",str(re.split(",", digit)))
# 或者
ret = re.findall(r"'(-?\d+)'",str(re.split(",", digit)))
print(ret)

# 匹配一段文本中的每行的邮箱
y = '123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
ret = re.findall(r'\w+@(?:qq|163|126).com',y)
print(ret)

# 匹配一段文本中的每行的时间字符串，比如：‘1990-07-12’
time = 'asfasf1999-07-22asdfAAAbbbb434241'
# ret = re.search(r'(?P<year>19[09]\d)',time)
ret = re.search(r'(?P<year>19[09]\d)-(?P<month>\d+)-(?P<day>\d+)',time)
# findall 输出的是元组
# ret = re.findall(r'(?P<year>19[09]\d)-(?P<month>\d+)-(?P<day>\d+)',time)
# print(ret)
print(ret.group('year'))
print(ret.group('month'))
print(ret.group('day'))

# 匹配一段文本中的数字。
card = 'sfafsf,3423423,1231313132'
ret = re.findall("\d{7}", card)
print(ret)

# # 2、列表（列表的基本操作）
# list 和 tuple 的相互转化 tuple(ls)  list(ls)
list1 = [1, 2, 3, 4, 5]
print(list1)
print(tuple(list1))
t1 = (1, 2, 3, 4, 5)
print(t1)
print(list(t1))
# 创建一个列表
list1 = ['apple', 'orange', 12, 34,'watermelon']
list2 = [1, 2, 3, 4, 5]

# 访问列表中的值
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# 更新列表list1中的值
print(list1[2])
list1[2] = 'pear'
print(list1[2])

# 删除列表元素
del list1[2]
print("删除后的列表元素有 : ")
print(list1)

# 创建连续的list
list1 = range(1, 5)       # 即 list1=[1,2,3,4],不含最后一个元素
print(list1)
list2 = range(1, 10, 2)  # 即 list2=[1, 3, 5, 7, 9]
print(list2)

# 将对象插入列表
list1 = ['a','cf','gf',2,5,7]
list1.insert(0,'hello')
print(list1)
# 反向列表中元素
list1.reverse()
print(list1)
# 遍历一个列表
L = ['a','cf','gf',2,5,7]

# 对原列表进行排序
list1 = ['3','7','23','1','21','36','18']
list2 = [3,7,23,1,21,36,18]
list1.sort()
list2.sort()
print("排序后的列表为：",list1)
print("排序后的列表为：",list2)

for a in L:
    # 打印列表中的值
    print(a)

# 通过while遍历一个列表
count = 0
while count < len(L):
    print(L[count])
    count += 1
# 3、打印九九乘法口诀和循环输出26个字母(并将字母的Ascii码同时输出)
for i in range (1,10):
    for j in range (1,i+1):
        # %前为占位符 后面括号中参数对应占位符位置, end 结束后追加的内容
        # print("%d*%d=%d"%(j,i,j*i),end="\t")
        print(j,"*",i,"=",j*i,end="\t")
    print(" ")
# 通过while方法处理
i = 0
j = 0
while i<9:
    i=i+1
    while j<9:
        j=j+1
        print("%d*%d=%d" % (j, i, j * i), end="\t")
        if i==j:
            j=0
            print("")
            break

# 输出26个字母以及对应ASCII码
import string
# chr(a)将a转为对应的字母
for a in range(97,123):
    print(chr(a)+"\t"+str(a))
# 输出小写字母及对应ASCII码
for word in string.ascii_lowercase:
    # 由于print中有字符拼接,数字只能通过转换为str()字符进行输出
    print(word + "\t" + str(ord(word)))
# 输出大写字母及对应ASCII码
for word in string.ascii_uppercase:
    # 由于print中有字符拼接,数字只能通过转换为str()字符进行输出
    print(word + "\t" + str(ord(word)))