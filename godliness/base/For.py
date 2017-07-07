languages = ["C", "C++", "Perl", "Python"]

for x in  languages :
    print(x);


sites = ["Baidu", "Google","Runoob","Taobao"]

for site in sites :
    if site == "Runoob":
        print("Runoob : "+site)
        break
    else:
        print("当前站点名称为" +site)
print("完成循环")

# 0,1,2,3,4,5,6,7,8,9,
for i in range(10) :
    print(i,end=" ")

print("")

# 5 6 7  左包含 右不包含
for j in range(5,8):
    print(j,end=" ")

print("")

#0 3 6 9  左包含 右不包含  从几开始 到几结束 步长多少
for k in range(0,10,3) :
    print(k,end=" ")

print("")

#-10 -40 -70 同上
for m in range(-10, -100, -30) :
    print(m,end=" ")

print("")
#range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for f in range(len(a)):
    print(f,a[f])

print("")
#range()创建列表
print(list(range(10)))

print("")

#enumerate 函数进行遍历
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print(i, j)

