#！/usr/bin/python3
# Filename : chengfabiao.py
# Author by : Lily

#实现乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d" %(j,i,i*j),end="  ")
    print("\n")