# 引入字符包
import string

# 输出26个字母以及对应ASCII码
for word in string.ascii_lowercase:
    # 由于print中有字符拼接,数字只能通过转换为str()字符进行输出
    print(str(word) + "\t" + str(ord(word)))

# 九九乘法表
# range(1,10) 从1到9 不包含10
for i in range(1, 10):
    for j in range(1, i+1):
        # %前为占位符 后面括号中参数对应占位符位置, end 结束后追加的内容
        print("%d*%d=%d" % (i, j, i*j), end="\t")
    print("")

# 通过while方式处理
i = 0
j = 0
while i < 9:
    i += 1
    while j < 9:
        j += 1
        # 与上述for中的输出方式不同.更换为单个参数
        print(j, "*", i, "=", i * j, "\t", end="")
        if i == j:
            j = 0
            print("")
            break

# 字符串：序列操作、编写字符串的其他方法、模式匹配

'''
    String模块，提供的方法
    S.find(substring, [start [,end]]) #可指范围查找子串，返回索引值，否则返回-1
    S.rfind(substring,[start [,end]]) #反向查找
    S.index(substring,[start [,end]]) #同find，只是找不到产生ValueError异常
    S.rindex(substring,[start [,end]])#同上反向查找
    S.count(substring,[start [,end]]) #返回找到子串的个数

    S.lowercase()
    S.capitalize()      #首字母大写
    S.lower()           #转小写
    S.upper()           #转大写
    S.swapcase()        #大小写互换

    S.split(str, ' ')   #将string转list，以空格切分
    S.join(list, ' ')   #将list转string，以空格连接

    处理字符串的内置函数
    len(str)                #串长度
    cmp("my friend", str)   #字符串比较。第一个大，返回1
    max('abcxyz')           #寻找字符串中最大的字符
    min('abcxyz')           #寻找字符串中最小的字符

    string的转换

    oat(str) #变成浮点数，float("1e-1")  结果为0.1
    int(str)        #变成整型，  int("12")  结果为12
    int(str,base)   #变成base进制整型数，int("11",2) 结果为2
    long(str)       #变成长整型，
    long(str,base)  #变成base进制长整型，
'''

# 去空格以及特殊符号
# s.strip().lstrip().rstrip(',')

# 复制字符串
sStr1 = 'strcpy'
sStr2 = sStr1
sStr1 = 'strcpy2'
print(sStr1, sStr2)

# 连接字符串
sconnect = 'strcat'
sconnect2 = 'append'
sconnect += sconnect2
print(sconnect)

# 查找字符 <0 为未找到
sfind = 'strschr'
sfind2 = 's'
nPos = sfind.index(sfind2)
print(nPos)

# 扫描字符串是否包含指定的字符
sStr1 = '12345678'
sStr2 = '456'
# sStr1 and chars both in sStr1 and sStr2
print(len(sStr1 and sStr2))

# 字符串长度
sStr1 = 'strlen'
print(len(sStr1))

# 字符串中的大小写转换
sStr1 = 'JCstrlwr'
# 转换为大写
sStr1 = sStr1.upper()
# 转换为小写
sStr1 = sStr1.lower()
print(sStr1)

# 追加指定长度的字符串
sStr1 = '12345'
sStr2 = 'abcdef'
n = 3
sStr1 += sStr2[0:n]
print(sStr1)

# 复制指定长度的字符
sStr1 = ''
sStr2 = '12345'
n = 3
sStr1 = sStr2[0:n]
print(sStr1)

# 将字符串前n个字符替换为指定的字符
sStr1 = '12345'
ch = 'r'
n = 3
sStr1 = n * ch + sStr1[3:]
print(sStr1)

# 扫描字符串
sStr1 = 'cekjgdklab'
sStr2 = 'gka'
nPos = -1
for c in sStr1:
    if c in sStr2:
        nPos = sStr1.index(c)
        break
print(nPos)

# 翻转字符串
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]
print(sStr1)

# 分割字符串
sStr1 = 'ab,cde,fgh,ijk'
sStr2 = ','
sStr1 = sStr1[sStr1.find(sStr2) + 1:]
print(sStr1)
#或者
s = 'ab,cde,fgh,ijk'
print(s.split(','))

# 连接字符串
delimiter = ','
myList = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(myList))

# 正则表达式
# 常用符号
'''
    \d  匹配任何十进制数
    \D  匹配任何非数字字符
    \s  匹配任何空白字符
    \S  匹配任何非空白字符
    \w  匹配任何字母数字下划线
    \W  匹配任何非字母数字字下划线
    .   代表任意字符
    |   逻辑或操作符
    []  匹配内部的任一字符或子表达式
    [^] 对字符集和取非
    -   定义一个区间
    \   对下一字符取非(通常是普通变特殊,特殊变普通)
    *   匹配前面的字符或者子表达式0次或多次
    *?  惰性匹配上一个
    +   匹配前一个字符或子表达式一次或多次
    +?  惰性匹配上一个
    ?   匹配前一个字符或子表达式0次或1次重复
    {n} 匹配前一个字符或表达式
    {m,n} 匹配前一个字符或字表达式至少m次至多n次
    {n,}  匹配前一个字符或者字表达式至少n次
    {n,}? 前一个的惰性匹配
    ^    匹配字符串的开头
    \A   匹配字符串的开头
    $    匹配字符串结束
    [\b] 退格字符
    \c   匹配一个控制符
    \t   匹配一个制表符
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
    常用正则表达式
    "^/d+$"　　//非负整数（正整数 + 0） 
    "^[0-9]*[1-9][0-9]*$"　　//正整数 
    "^((-/d+)|(0+))$"　　//非正整数（负整数 + 0） 
    "^-[0-9]*[1-9][0-9]*$"　　//负整数 
    "^-?/d+$"　　　　//整数 
    "^/d+(/./d+)?$"　　//非负浮点数（正浮点数 + 0） 
    "^(([0-9]+/.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*/.[0-9]+)|([0-9]*[1-9][0-9]*))$"　　//正浮点数 
    "^((-/d+(/./d+)?)|(0+(/.0+)?))$"　　//非正浮点数（负浮点数 + 0） 
    "^(-(([0-9]+/.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*/.[0-9]+)|([0-9]*[1-9][0-9]*)))$"　　//负浮点数 
    "^(-?/d+)(/./d+)?$"　　//浮点数 
    "^[A-Za-z]+$"　　//由26个英文字母组成的字符串 
    "^[A-Z]+$"　　//由26个英文字母的大写组成的字符串 
    "^[a-z]+$"　　//由26个英文字母的小写组成的字符串 
    "^[A-Za-z0-9]+$"　　//由数字和26个英文字母组成的字符串 
    "^/w+$"　　//由数字、26个英文字母或者下划线组成的字符串 
    "^[/w-]+(/.[/w-]+)*@[/w-]+(/.[/w-]+)+$"　　　　//email地址 
    "^[a-zA-z]+://(/w+(-/w+)*)(/.(/w+(-/w+)*))*(/?/S*)?$"　　//url
    /^(d{2}|d{4})-((0([1-9]{1}))|(1[1|2]))-(([0-2]([1-9]{1}))|(3[0|1]))$/   //  年-月-日
    /^((0([1-9]{1}))|(1[1|2]))/(([0-2]([1-9]{1}))|(3[0|1]))/(d{2}|d{4})$/   // 月/日/年
    "^([w-.]+)@(([[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.)|(([w-]+.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(]?)$"   //Emil
    "(d+-)?(d{4}-?d{7}|d{3}-?d{8}|^d{7,8})(-d+)?"     //电话号码
    "^(d{1,2}|1dd|2[0-4]d|25[0-5]).(d{1,2}|1dd|2[0-4]d|25[0-5]).(d{1,2}|1dd|2[0-4]d|25[0-5]).(d{1,2}|1dd|2[0-4]d|25[0-5])$"  //IP地址
     
    
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
# 引入正则表达式包
import re

# 匹配一段文本中的每行的邮箱
y = '123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
ret = re.findall('\w+@(?:qq|163|126).com', y)
print(ret)

# 匹配一段文本中的每行的时间字符串，比如：‘1990-07-12’
time = 'asfasf1990-07-12asdfAAAbbbb434241'
ret = re.search(r'(?P<year>19[09]\d)-(?P<month>\d+)-(?P<day>\d+)', time)
print(ret.group('year'))
print(ret.group('month'))
print(ret.group('day'))

# 匹配一段文本中所有的身份证数字。
card = 'sfafsf,34234234234,1231313132,154785625475896587,sdefgr54184785ds85,4864465asf86845'
ret = re.findall("\d{18}", card)
print(ret)

# 匹配出所有整数
digit = '1,-3,a,-2.5,7.7,asdf'
ret = re.findall(r"'(-?\d+)'",str(re.split(",", digit)))
print(ret)

'''
    列表操作包含以下函数:
    1、cmp(list1, list2)：比较两个列表的元素 
    2、len(list)：列表元素个数 
    3、max(list)：返回列表元素最大值 
    4、min(list)：返回列表元素最小值 
    5、list(seq)：将元组转换为列表 
    列表操作包含以下方法:
    1、list.append(obj)：在列表末尾添加新的对象
    2、list.count(obj)：统计某个元素在列表中出现的次数
    3、list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    4、list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
    5、list.insert(index, obj)：将对象插入列表
    6、list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    7、list.remove(obj)：移除列表中某个值的第一个匹配项
    8、list.reverse()：反向列表中元素
    9、list.sort([func])：对原列表进行排序
'''
'''
    list 和 tuple 的相互转化
    tuple(ls) 
    list(ls)
'''

# 创建一个列表
# 与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

# 访问列表中的值
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# 更新列表
print("Value available at index 2 : ")
print(list1[2])
list1[2] = 2000
print("New value available at index 2 : ")
print(list1[2])

# 删除列表元素
del list1[2]
print("After deleting value at index 2 : ")
print(list1)

# 用某个固定值初始化列表

initial_value = 0
list_length = 5
sample_list = [initial_value for i in range(10)]
sample_list = [initial_value] * list_length
print(sample_list)

# 创建连续的list
L = range(1, 5)       # 即 L=[1,2,3,4],不含最后一个元素
print(L)
L1 = range(1, 10, 2)  # 即 L=[1, 3, 5, 7, 9]
print(L1)

# 遍历一个列表
for var in L:
    # 打印列表中的值
    print(var)

# 通过while遍历一个列表
count = 0
while count < len(L):
    print(L[count])
    count += 1



