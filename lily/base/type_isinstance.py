#!usr/bin/python3
# Filename : type_isinstance.py
# Author by : Lily
# type() 和isinstance()的区别


class Foo(object):
    pass


class Bar(Foo):
    pass


print(type(Foo()) == Foo)  # True

print(type(Bar()) == Foo)  # False

print(isinstance(Bar(), Foo))  # True
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
