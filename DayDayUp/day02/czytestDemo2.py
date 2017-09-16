import os
import sys
#获取当前所工作的目录的名称
#得到D:\AllWorkSpace\python_space\python\DayDayUp\day02
f = os.getcwd()
print(f)
#打印系统平台的名称
print(sys.platform)
#range(1,10)为1——9
#打印九九乘法表
print('第一种方法：')
for i in range(1,10):
    for a in range(1,i+1):
        re = str(i*a)  #将相乘结果转换成str用于拼接
        rs = str(i)+'*'+str(a)+'='+re
        #end为结束后追加的内容
        print(rs,end='\t')
    print('\n')

print('第二种方法：')
for i in range(1, 10):
    for j in range(1, i+1):
        # %前为占位符 后面括号中参数对应占位符位置, end 结束后追加的内容
        print("%d*%d=%d" % (i, j, i*j), end="\t")
    print("")

print('第三种方法：')
i = 1
while i < 10:
    if i == 1:
      j = i
      print("%d*%d=%d" % (i, j, i * j), end="\t")
      i = i + 1
    else:
        j = 1
        while j < i+1:
            print("%d*%d=%d" % (i, j, i * j), end="\t")
            j = j + 1
        i += 1
    print("")

