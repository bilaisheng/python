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
# 字符串 截取 拼接 叠加
stra="My name is Vincent."

print(stra[0])
print(stra[-1])






# 布尔类型 以及 逻辑运算

print (True)
print (False)
if 3>5:
    print (True)
else:
    print (False)

# 集合类数据类型
