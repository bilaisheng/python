
def tow(nums, target):
 l2 = []
 len1=len(nums)
 for i in range(0,len1) :
    for j in range(i+1,len1):
           if(l[i]+l[j] == target):
               print(i)
               print(j)
               l2.append(i)
               l2.append(j)
 return l2


l = [3, 4, 5]
tow(l,9)

l = [3, 4, 5,4,3,1]
enum = enumerate(l)
e = list(enum)
for i in e:
    print(i[0])
    print(i[1])
print(e)

print(l)
