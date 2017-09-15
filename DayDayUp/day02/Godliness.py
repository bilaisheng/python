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

