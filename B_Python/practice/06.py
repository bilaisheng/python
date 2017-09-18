# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
from sys import stdout

from pip._vendor.distlib.compat import raw_input

n = int(raw_input("请输入正整数 ： "))

for i in range(2,n+1):
    while n != i:
        if n % i == 0:
            stdout.write(str(i))
            stdout.write('*')

            # 用int转换，否则会出现结果最后一个数字带小数点
            n = int(n / i)
        else:
            break
print(n)