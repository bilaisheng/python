# 打开一个文件
#f = open("foo.txt", "w")

#f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
#f.close()


f = open("foo.txt","r")

#读取一行
#print(f.readline())

#读取所有
#print(f.read())

#读取所有行
print(f.readlines())
f.close()

#通过循环方式 获取文件内容

# 打开一个文件
f = open("foo.txt", "r")

for line in f:
    print(line, end='')

print(f.tell())

# 关闭打开的文件
f.close()