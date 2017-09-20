# i = -789
# s = str(i)
#
# print(s[::-1])


# def reverse(self, x):
#     if x > 0:
#         s = str(x)
#         s2 = s[::-1]
#         print(s2)
#         return s[::-1]
#     elif x < 0:
#         s2 = str(abs(x))
#         print(s2)
#         s3 = s2[::-1]
#         s4 = '-' + s3
#         print(s4)
#         return s4
#
# x = -998
# reverse(x)

def reverse1( x):
    a = 0
    if x >= 0 :
        a = int(str(x)[::-1])
        print(a)
    else:
        a=- int(str(-x)[::-1])
        print(a)
    if a < 2147483648 and a >= -2147483648:
        return a
    else:
        return 0

b = -99662
reverse1(-99662)
print()

# def reverse(self, x):
#     flag = 1 if x >= 0 else -1
#     new_x, x = 0, abs(x)
#     while x:
#         new_x = 10 * new_x + x % 10
#         x /= 10
#         new_x = flag * new_x
#     return new_x if new_x < 2147483648 and new_x >= -2147483648 else 0