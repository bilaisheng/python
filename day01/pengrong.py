'''

1 数据类型 (类型转换 .每个类型常用方法, )
2 字符操作(截取 拼接,替换 等)
3 循环(for ,  for else , while ,while else 常用循环判断)
'''

# 基本数据类型 整数， 浮点型， 字符串
 # 整数 计算正确
inta=10
intb=21
print (inta+intb) # 30
print (intb/inta) # 2.1
print (inta/intb) #0.47619047619047616
print (intb*inta) # 210
# 浮点型，科学计数法;非精确
ef=2.1*10e10
print (ef)
ef=ef*2.5654
print (ef)
# 字符串 以单引号 ，或者双引号括起来的文本。
name= input("input >>>: ")  # 以输入内容以 字符串形式表示
nametype=type(name) # string
print(name)
print(nametype)
stra="abc"
strb='def'
strc="I'm Ok" # 包含单 双引号
strd="I'm \"Ok" # 双引号里面还有双引号字符。 需要转义
stre='I\'m "ok"'
print(stra)
print(strb)
print(strc)
print(strd)
print(stre)

# 不想转义 \n \t \\ 等字符
strh=r"\n\t\\"
print(strh) # 输出  \n\t\\

# """ """ 字符串界定符输入多行的一个字符串,有\n字符表示换行多一个空行
strj="""sdlfkj\n
lsdkfj
lkjdfldk
lsdfkj
"""
print(strj)

# r字符表示对字符内容不进行转义
strj=r"""sdlfkj\n
lsdkfj
lkjdfldk
lsdfkj
"""
print(strj)
# 布尔类型


# 集合类数据类型
