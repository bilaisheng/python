# 1. 数据类型 (类型转换 .每个类型常用方法, )
# 1 字符串（String）
s1 = "chang"
s2 = "jie"

print(s1) # 输出完整字符串
print (s1[0])       # 输出s1字符串中的第一个字符
print (s1[1:5])     # 输出s1字符串中第二个至第五个之间的字符串
print (s1[2:])     # 输出s1中从第三个字符开始的字符串
print (s1 * 2)      # 输出字符串两次
print (s1+s2)      # 输出连接字符串s1 s2

# 数字（Digit）
a = 123
# 列表（List）

list1 = ['c', 'h', 'a', 'n','g']
list2 = [1,2,3]
list3 =["chang"]

print (list1)  # 输出完整列表list1
print (list1[0]) # 输出列表list1的第一个元素
print (list1[1:4])  # 输出list1第二个至第四个的元素

# 对列表list2进行更新操作
print (list2[1])
list2[1] = 999   # 修改list2中的第2个元素
print (list2[1]) # 输出更新后的元素

#删除列表元素
print (list2[1])
del list2[1]  #删除list2中的第2个元素
print (list2) # 输出删除后的列表

# 元组（Tuple）
# 创建元组
tup1=(1,2,3)
print (tup1)
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合
print ("tup1[0]: ", tup1[0]) # 输出元组tup1中第1个元素
print ("tup1[1:]: ", tup1[1:])

tup2 = ("all")
print (tup2)  # 输出字符串 all，这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号
tup3 = ("all",) # 如果元组只有1个元素，就必须加一个逗号，防止被当作括号运算
print (tup3)

# 集合（Sets）
# 集合用于包含一组无序的不重复的对象
s = set([3, 5, 9, 10])  # 创建一个数值集合
print(s)

# 自动过滤重复元素
s = set([1, 1, 2, 2, 4, 5, 4])
print(s)
# 添加一项
s.add('x')
print(s)
# 在s中添加多项
s.update([10, 37, 42])
print(s)

# 使用remove()可以删除一项：
s.remove(4)
print(s)
# 集合支持一系列标准操作，包括并集、交集、差集和对称差集
s1=set([1,2])
s2=set([1,4])
print( s1 | s2 ) # s1 和s2的并集
print( s1 & s2)  # s1 和 s2的交集
print(s1 - s2 ) # 求差集（项在s1中，但不在s1中）
print(s1 ^ s2)  # 对称差集（项在s1或s2中，但不会同时出现在二者中）

# 字典（Dictionary）
# 创建字典  键必须是唯一的，但值则不必。
d = {'Name': 'Zara', 'Age': 7}

print(dict)
print("d['Age']: ", ['Age'])
# 查找字典
# dict是通过key来查找value，表示的是意义对应的关系，可以通过d[key]的方式
print("d['Age']: ", d['Age'])

# 日期(Date)
import time  # 引入time模块
# 时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年
ticks = time.time()
print("当前时间戳为:", ticks)
# 从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
localtime = time.localtime(time.time())
print("本地时间为 :", localtime)
# 获取格式化的时间,最简单的获取可读的时间模式的函数是asctime():
localtime = time.asctime( time.localtime(time.time()) )
print("本地时间为 :", localtime)

# 2字符操作(截取 拼接,替换 等)
str = 'hellopython'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "cj")  # 连接字符串


# 3 循环(for ,  for else , while ,while else 常用循环判断)
# for循环
animals ={'pig','monkey','dog'}
for animal in animals:
    if animal == 'dog':
        print('当前动物222:'+animal)
        break;
    else:
        print("当前动物为：" +animal)

for num in range(1,10):  # 迭代 1到 10 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:     # 确定第一个因子
         j=num/i          # 计算第二个因子
         print('%d 等于 %d * %d' %(num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print(num,'是一个质数')

# while循环
i = 1
while 1:            # 循环条件为1必定成立
    print(i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

j=1
while j<5:    # 循环条件
    print(j,"j小于5")
    j=j+2
else:   # 当i大于等于5时
    print(j, "j大于等于5")

