"""
今天的知识点：
1、字符串：序列操作、编写字符串的其他方法、模式匹配
2、列表（列表的基本操作）
3、打印九九乘法口诀和循环输出26个字母(并将字母的Ascall码同时输出)

Note：1.字符串的内建函数列举了部分，还有很多未列举
遗留疑惑点：Unicode字符串；buffer对象
"""

# python 包含6中内建序列：1.列表；2.元组；3.字符串；4.Unicode字符串；5.buffer对象；6.xrange对象（python3是range）
# 字符串的序列操作包括：
# 1）索引
# 2）切片
# 3）连接
# 4）乘
# 5）成员资格（检查某个元素是否属于序列成员）
# 6）计算序列长度
# 7) 最大元素
# 8）最小元素

# 1.索引：序列中所有的元素都有自己的编号，从左往右是0开始递增，从右往左是从-1开始递减
Name = 'Lily'
print(Name[0])   # 输出L
print(Name[1])   # 输出i
print(Name[2])   # 输出l
print(Name[3])   # 输出y
# print(Name[4])   # 给的索引超出范围时候会报错 IndexError: string index out of range
print(Name[-1])   # 输出y
print(Name[-2])   # 输出l
print(Name[-3])   # 输出i
print(Name[-4])   # 输出L

# 索引原则适用于所有序列
List = ['you','have',10000,'yuan','in','bank']
print(List[0])   # 输出you
print(List[-1])  # 输出bank
tuple =(1,2,3)
print(tuple[1])  # 输出2
print(tuple[-2]) # 输出2
r =range(0,10)
print(r[0])      # 输出0
print(r[-1])     # 输出9

# 2.切片：通过冒号相隔的两个索引来实现，用来访问一点范围内的元素，实现提取序列。
# 切片操作需要提供两个索引作为边界，第一个索引的元素包含在切片内，而第二个元素不包含在切片内。
# 步长是切片的第三个参数，默认值是1，当设置大于1时，就会跳过某些元素，当为负数时，从右往左提取元素
s = 'abcdefg'
print(s[0:3])   # 取索引0到2的值，输出abc
print(s[:3])    # 取索引0到2的值，输出abc
print(s[-4:-1]) # 取反向索引-2到-4的值，输出def
print(s[-4:])   # 取反向索引-1到-4的值，输出defg
print(s[:])     # 取整个字符串的值，输出abcdefg
print(s[0:5:2]) # 输出ace
print(s[::3])   # 输出adg
print(s[::-2])  # 输出geca
print(s[-5:-1:2])    # 输出ce
# print(s[-5:-1:-2])  这样写输出的是空行

# 切片原则适用于所有序列
browsers = [360,'Google','Firefox','IE']
print(browsers[0:2])   # 输出[360,'Google']
print(browsers[:2])    # 输出[360,'Google']
print(browsers[-2:-1]) # 输出['Firefox']
print(browsers[-2:])   # 输出['Firefox','IE']
print(browsers[:])     # 输出[360,'Google','Firefox','IE']
print(browsers[0:4:2]) # 输出[360,'Firefox']
print(browsers[::-2])  # 输出['IE'，'Google']
title = ('name','age','sex','ddress','phone')
print(title[:2])       # 输出('name','age')
print(title[:])        # 输出('name','age','sex','ddress','phone')
print(title[0:4:2])    # 输出('name','sex')
print(title[::-3])     # 输出（'phone','age'）
r = range(1,10)
print(r[:5])           # 输出range(1:6)
print(r[5:])           # 输出range(6:10)
print(r[:])            # 输出range(1,10)
print(r[1::3])         # range(2,10,3)
print(r[::-4])         # range(9,0,-4)

# 3.连接：通过使用加号(+)进行连接操作
a = 'abc'
b = 'def'
c = a,b
print(a+b)   # 输出abcdef
print(a,b)   # 输出abc def
print(c)     # 输出('abd','def')
print(type(c))  # 输出<class 'tuple'>

# 连接原则适用于list,tuple,不适用于range()
print(['apple','orange']+['banana','watermemon'])  # 输出['apple','orange','banana','watermemon']
print((1,3,4)+(4,2,6))   # 输出(1,3,4,4,2,6)

# 4.乘：用序列乘以N会生产一个新序列，即原来的序列被重复N次
Hobby = 'badminton'
print(Hobby*3)    # 输出badmintonbadmintonbadminton

# 乘原则适用于list,tuple,不适用于range()
print(['apple']*3)  # 输出['apple', 'apple', 'apple']
print((1,2)*3)      # 输出(1, 2, 1, 2, 1, 2)

# 5.成员资格：in/not in 用来判断一个值是否在序列中，在则返回True,不在则返回False.
member ='Lily,Lucy,Jack'
print('Lily' in member) # 返回True
print('lily' in member) # 返回False,因为区分大小写
print('TOM' not in member) # 返回True
print('Jack' not in member) # 返回False

# 成员资格原则适用于所有序列
print(1 in [1,2,3])          # 返回True
print(8 in ['a','b'])        # 返回False
print('a' in ('a','b'))      # 返回True
print('a' in ('abc','def'))  # 返回False
print(1 in range(0,4))        # 返回True
print(10 in range(1,5))       # 返回False

# 6.计算序列长度：len()
shoes = 'vans,nike,adidas'
print(len(shoes))  # 输出16

# 计算长度方法适用于所有序列
print(len([1,3,4]))         # 输出3
print(len(('a','b','c')))   # 输出3
print(len(range(1,10)))     # 输出9

# 7.最大值 max()
phone = 'vivo,apple,huawei'
num = '12389540'
print(max(phone))  # 输出w
print(max(num))    # 输出9

# 最大值 max()适用于所有序列（数据类型相同的序列）
print(max([1,2,3]))           # 输出3
print(max(['a','b','c',':'])) # 输出c
print(max((1,3,4)))           # 输出4
# print(max(('a','b',1))) 报错，数字和字母不能比大小
print(max(range(1,10)))       # 输出9

# 8.最小值 min()
print(min(phone))  # 输出,
print(min(num))    # 输出0

# 最小值 min()适用于所有序列（数据类型相同的序列）
print(min([1,2,4]))        # 输出1
print(min(['x','r']))      # 输出r
print(min((1,3)))          # 输出1
print(min(('a','y','o')))  # 输出a
print(min(range(5,19)))    # 输出5

# 字符串有很多内建函数，在此列出常用的几个
# 1.string.capitalize() 把字符串的第一个字母大写
# 2.string.center(width)      返回一个原字符串，并使用空格填充至长度width的新字符串
# 3.string.count(str,beg=0,end=len(string))  返回str在string 里面出现的次数，
# 如果beg,end指定则返回在指定范围内str出现的次数
# 4.string.endwith(obj,beg=0,end=len(string)) 检查字符串是否以obj结束，
# 如果beg,end指定则检查指定范围内是否以ob结束，是返回True,不是返回False
# 5.string.find(str,beg=0,end=len(string)) 检测str是否包含在string中，
# 如果beg,end指定则检测指定范围内是否有str,有则返回开始的索引值，否则返回-1
# 6.string.index(str,beg=0,end=len(string))  返回str在string的开始索引，如果str不在string中则报异常
# 7.string.isalnum()  如果string至少有一个字符且所有字符都是字母或者数字则放回True,否则返回False
# 8.string.isalpha()  如果string至少有一个字符且所有字符都是字母则返回Ture,否则返回False
# 9.string.isdigit()  如果string至少有一个字符且所有字符是数字则返回True,否则返回False
# 10.string.islower() 如果string中包含至少一个区分大小写的字符，并且这些字符都是小写，则返回True,否则返回False
# 11.string.isnumeric() 如果string字符里只包含数字字符，则返回True,否则返回False
# 12.string.isspace() 判断string是否只包含空格，是则返回True,否则返回False
# 13.sring.isupper()  判断string是否全都是大写字母，是则返回True,否则返回False
# 14.string.lower() 将string中所有的大写字符转换成小写
# 15.string.lstrip() 截取sting左边的空格
# 16.string.replace(str1,str2,num=string.count(str1)) 把string中str1替换成str2,
# 如果num指定，则替换不超过num次
print('apple'.capitalize())  # 输出Apple
print('apple'.center(10))    # 输出   Apple
print('apple,orange'.count('a')) # 输出2
print('apple'.endswith('e'))     # 返回True
print('apple'.find('p'))         # 返回1
print('apple'.find('r'))         # 返回-1
print('orangesoranges'.index('s')) # 返回6
print('orangesoranges'.index('o')) # 返回0
print('apple23'.isalnum())         # 返回True
print('a+'.isalnum())              # 返回False
print('apple'.isalpha())           # 返回True
print('+'.isalpha())               # 返回False
print('23432'.isalpha())           # 返回False
print('123'.isdigit())             # 返回True
print('+'.isdigit())               # 返回False
print('dsk'.islower())             # 返回True
print('sd'.isnumeric())            # 返回False
print('3'.isnumeric())             # 返回True
print('3 4 2'.isspace())           # 返回False
print('  '.isspace())              # 返回True
print('AB'.isupper())              # 返回True
print('AB'.lower())                # 输出ab
print('  dec'.lstrip())            # 输出dec
print('apple,orange'.replace('a','A'))  # 输出Apple,orAnge

'''
正则表达式的元字符和语法：
.    匹配任意除换行符“\n”外的字符
\    转义字符，使用后一个字符变成原来的意思
[]   字符集，对应的位置可以是字符集中任意字符。第一个字符如果是^,则表示去反，
     在字符集中如果要使用]、-^可以在前面加上反斜杠
\d   数字[0-9]
\D   非数字[^\d]
\s   空白字符[<空格>\t\r\n\f\v]
\S   非空白字符[^\s]
\w   单词字符[A-Za-z0-9]
\W   非单词字符[^\w]
*    匹配前一个字符0次或者无限次
+    匹配前一个字符1次或者无限次
？   匹配前一个字符0次或者一次
{m}  匹配前一个字符m次
{m,n}匹配前一个字符m至n次，若省略m,则匹配0到n次，若省略n,则匹配m到无限次
^    匹配字符串开头，在多行模式中匹配每一行的开头
$    匹配字符串的末尾，在多行模式中匹配每一行的末尾
\A   仅匹配字符串开头
\Z   仅匹配字符串的末尾
\b   匹配\w和\W之间
\B   [^\b]
|    代表左右表达式任意匹配一个

python中正则表达式模块re的方法：
1. res = re.match(pattern,string,flag=0) 字符串的开头是否能匹配正则表达式，如果匹配则返回_sre.SRE_Match对象
   res.string可以原始的原字符串，不匹配则返回None
2. re.sub(pattern,rep1,string,count=0,flag=0)   找到re匹配的所有子串，并将其用rep1替换
   count 是模式匹配后替换的最大次数；count必须是非负数，缺省值是0，表示所有的匹配
   如果无匹配则返回原字符串，如果有匹配则返回替换后的字符串
3.re.findall(pattren,string)  从string中找到所有匹配pattern的子串，作为列表返回
   如果没有匹配返回空数组，可用来当做if的判断条件，空数组为False
4.re.search(pattern,string) 查找，如果找到则返回一个match对象，找不到则返回None
5.match(),search()如果匹配成功则返回一个对象，这个对象有以下属性和方法：
group()  返回被re匹配的字符串
start()  返回匹配开始的位置
end()    返回匹配结束的位置
span()   返回一个元组包含匹配（开始，结束）的位置
6.re.split(pattern,string,maxsplit=0) 见字符串按照pattern分割成几段单词列表
7.re.compile(pattern) 可以把正则表达式编译成一个表达式对像，可以把常用的表达式编译成对象，可以提高效率
'''

import re
print(re.match(r'a','abc'))  # <_sre.SRE_Match object; span=(0, 1), match='a'>
print(re.match(r'a','abc').string)  # 输出abc
print(re.match(r'q','abc'))    # 返回None
print(re.sub(r'a','A','appleappleapple'))  # 返回AppleAppleApple
print(re.sub(r'124','0','apple'))          # 返回apple
print(re.findall(r'\d','apple124apple123'))  # 返回['1', '2', '4', '1', '2', '3']
print(re.findall(r'\n','sdk'))    # 返回[]
print(re.search(r'b','abcabc').string)     # 返回abcabc
print(re.search(r'b','abcabc').start())    # 返回1
print(re.search(r'ab','abcabc').end())     # 返回2
print(re.search(r'ab','abcabc').group())   # 返回ab
print(re.split(r'b','abcabc'))             # 返回['a', 'ca', 'c']
p = re.compile(r'b')
print(p.split('abcabc'))                   # 返回['a', 'ca', 'c']

'''
列表的基本操作:
1. list.append(obj)  在元素的末尾添加新的对象
2. list.count(obj)   统计某个元素在列表出现的次数
3. list.extend(obj)  在列表的末尾一次性追加另一个序列的多个值
4. list.index(obj)   从列表中找到某个值得第一个匹配的索引位置
5. list.insert(index,obj) 将对象插入列表
6. list.pop(obj=list[-1])  移除列表中的一个元素（默认最后一个），并且返回该元素的值
7. list.remove(obj)    移除列表中的某一个值得第一个匹配项
8. list.reverse()  反向列表中的元素
9. list.sort([func])  对列表进行排序
10.list.clear()  清空列表
11.list.copy()
'''

L1 = [1,3]
L2 = ['a','b','c','d','a']
L1.append([4,5])
print(L1)            # 输出[1, 3, [4, 5]]
print(L2.count('a')) # 输出2
L1.extend([4,5])
print(L1)            # 输出[1, 3, [4, 5], 4, 5]
print(L2.index('c')) # 输出2
L2.insert(0,'Q')
print(L2)            # 输出['Q', 'a', 'b', 'c', 'd', 'a']
L2.pop()
print(L2)            # 输出['Q', 'a', 'b', 'c', 'd']
L2.remove('a')
print(L2)            # 输出['Q','b', 'c', 'd']
L2.reverse()
print(L2)            # 输出['d', 'c', 'b', 'Q']
L2.sort()
print(L2)            # 输出['Q', 'b', 'c', 'd']
L2.clear()
print(L2)            # 输出[]
L3 = L1.copy()
print(L3)            # 输出[1, 3, [4, 5], 4, 5]

# 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}" .format(i,j,i*j),end=" ")
    print("\n")

# 循环输出26个字母(并将字母的Ascall码同时输出)
for alpha in range(ord('a'),ord('z')+1):
    print(alpha,chr(alpha))


