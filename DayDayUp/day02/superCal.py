import string

# while实现
n = 9
j = 0
i = 0
while i < n:
    i = i + 1
    while j < i:
        j = j + 1
        print("%d * %d =%d" % (j, i, i * j), end="\t")
        if(j==i):
            j=0
            break
    print(" ")

#  3、打印九九乘法口诀和循环输出26个字母(并将字母的Ascall码同时输出)
for i in string.ascii_lowercase:
    print(str( i ) +r'  '+ str(ord(i)))

for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d" % (j,i,j*i),end="\t")
    print(" ")





