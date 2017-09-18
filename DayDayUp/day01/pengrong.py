'''

1 数据类型 (类型转换 .每个类型常用方法, )
2 字符操作(截取 拼接,替换 等)
3 循环(for ,  for else , while ,while else 常用循环判断)
'''

# 基本数据类型 数字(整数， 浮点型）， 字符串
 # 整数
inta=10
intb=21
print (inta+intb) # 30
print (intb/inta) # 2.1
print (inta/intb) #0.47619047619047616 含有小数
print (intb //inta) # 2 整除
print (intb % inta) #1 求余
print (intb*inta) # 210



# 浮点型，科学计数法;非精确
ef=2.1*10e10
print (ef)
ef=ef*2.5654
print (ef)
# 字符串 单，双引号
stra="zhongguo"
strb="zhongguo's"
strc="zhongguo\"" # 转义
strd="zhongguo\"\'" # 转义
stre=r"zhongguo\"\'" # 不转义
strf="""
    zhongguo,
    meiguo,
    huawei,
    xiaomi,
    OPPO
"""
print (stra)
print (strb)
print (strc)
print (strd)
print (stre)
print (strf)
print(stra,strb,strc,strd,stre,strf)

# 字符串 截取 拼接 叠加
stra="My name is Vincent."

print(stra[0])
print(stra[-1])
print(stra*3)
print(len("中文")) # 计算中文字符数
print(len("中文".encode("utf-8"))) # 计算字节数组长度
bytess="中文".encode("utf-8")
stra=bytess.decode("utf-8")
print(stra)

# 格式化输出字符串 ，整数，浮点数
print("Hi %s, your age is %d, your score is %f"%("Jack",16,85.6))
# 输出多个字符串组合的一起的字符串。每个字符串之间空一个空格。
print(stra,strb,strc,strd,stre)
# 自己拼接的无空格
print(stra+strb+strc+strd+stre)



# 布尔类型 以及 逻辑运算

print (True)
print (False)
print(not True)
print(not False)
if 3>5:
    print (True)
else:
    print (False)

# pyton 动态语言特性
stra="ABC"
print(stra) # ABC 变量可以指向任何类型
stra=12122311
print(stra) # 12122311
strb=stra
stra=111
print(stra) # 111
print(strb) # 12122311

# 集合类数据类型
# 列表(List)
# 元祖(Tuple)
# 集合(Sets)
# 字典(Dictionary)

# list 是有序集合
classmates = ['Michael', 'Bob', 'Tracy']
list1=['I','am',18]
list2=['you',23,list1]

# List截取 拼接,替换，可以替换变量对应数据对象，或者增加列表元素；list 是用 [ ] 作为边界符
# 循环输出，必须用Range输出
for index in  range(0,len(classmates)):
    print(classmates[index])

print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates+list1) #拼接
print(list1*3)# 3个同样的list拼接
print(list2*2) # 元素包含一个
print(list2+list1)
classmates.append("bb") # 增加
classmates.insert(0,'Jack') #指定位置增加
print(classmates[0])
print(classmates[-1])
print(classmates)
#print(classmates.sort())
classmates.sort()  # 排序
print(classmates)


# 删除 末尾元素
classmates.pop()
classmates.pop(0)
print(classmates)

# 替换 指定位置元素内容
classmates[0]="BBBBB"
print(classmates)


# tuple  tuple一旦初始化就不能修改元祖元素所指向的对象 ，但是对象的属性可以改变。
# 元祖以 ( ) 作为元素边界符
classmates = ('AA', 'BB', 'DD')
print(classmates)

# classmates.append('df') 无append属性，不能尾加。
# classmates[0]='ee' tuple元素 不支持分配新对象给元素。

print(classmates)

# 定义空tuple
tuple1=()
print(tuple1)
#定义一个元素的tuple
tuple1=(1,)
print(tuple1)

# tuple 里面包含list， 元祖指向[34,56,78,90]这个list指向不可变，
# 但是list里面的list元素可以改变。tuple一开始指向的list并没有改成别的list；
classmates = ('AA', 'BB', 'DD',[34,56,78,90])
print(classmates)
classmates[3][0]=100
classmates[3][1]=200
print(classmates)

#理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。 元祖指向元祖

classmates = (('AA',),( 'BB',), ('DD',),(34,56,78,90))
print(classmates)
# classmates[3][0]=45 tuple 的元素指向一个元祖，元祖是不可变的。那么就实现了元祖的内容也是不变的。
print(classmates)



# Set 类型


# Dict类型


# 三大流程结构

# if -elif -else

age=16
age=input("please a age: ") # input 返回的是str  ，要进行类型强制转换。
age=int(age)
if age>=18:
    print("成年人")
elif age>12 :
    print("青少年")
else:
    print("小孩")

# 循环结构
    # for x in ...:
    # while  x:
sum=0
for x in  range(101):
    sum+=x
print(sum)

#第二种循环是while循环，只要条件满足，就不断循环
sums=0
while sum>0:
    sums+=sum
    sum=sum-1000
print(sums)