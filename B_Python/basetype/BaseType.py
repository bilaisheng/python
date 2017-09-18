counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)


a, b, c, d = 100, 10.0, True, 2-4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, bool))
print(isinstance(d, complex))

# isinstance 和 type 的区别在于：
class A:
    pass

class B(A):
    pass

isinstance(A(), A)  # returns True
type(A()) == A      # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。