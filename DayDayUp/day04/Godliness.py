# 用戶定义类，数字常量和内置数学工具和扩展，表达式操作符递归阶乘

__author__ = 'bilaisheng'

'''
　1.类的定义
　2.父类，子类定义，以及子类调用父类
　3.类的组合使用
　4.内置功能
'''

# 类的定义


# class Hotel(object):
#     # 构造函数
#     def __init__(self, room, cf=1.0, br=15):
#         self.room = room;
#         self.cf = cf;
#         self.br = br;
#
#     def calc_all(self, days=1):
#         return (self.room * self.cf + self.br) * days
#
# if __name__ == '__main__':
#     stdroom = Hotel(200)
#     big_room = Hotel(230, 0.9)
#     print(stdroom.calc_all())
#     print(stdroom.calc_all(2))
#     print(big_room.calc_all())
#     print(big_room.calc_all(2))

# 父类 子类以及调用父类

# 父类
class AddBook(object):

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_phone(self):
        return self.phone


# 子类继承
# class EmplEmail(AddBook):
#
#     def __int__(self,nm, ph, email):
#         # AddBook.__init__(selef, nm, ph) # 调用父类方法一
#         super(EmplEmail, self).__init__(nm, ph)
#         self.email = email
#
#     def get_email(self):
#         return self.email
#
# # 调用
# if __name__ == '__main__':
#
#     detian = AddBook('Detian', '12345678901')
#     meng = AddBook('Meng', '12345678902')
#     print(detian.get_phone())
#     print(AddBook.get_phone(meng))
#
#     alice = EmplEmail('godliness', '1234567890', 'godliness@qq.com')
#
#     print(alice.get_email(), alice.get_phone())

# 类的组合使用

'''
1.class类的组合使用
2.手机、邮箱、QQ等是可以变化的（定义在一起），姓名不可变（单独定义）。
3.在另一个类中引用
'''

class Info(object):
    def __init__(self, phone, email, qq):
        self.phone = phone
        self.email = email
        self.qq = qq

    def get_phone(self):
        return self.phone

    def update_phone(self, newphone):
        self.phone = newphone
        print("手机号更改已更改")

    def get_email(self):
        return self.email


class AddrBook(object):
    def __init__(self, name, phone, email, qq):
        self.name = name
        self.info = Info(phone, email, qq)


if __name__ == "__main__":
    Detian = AddrBook('godliness', '1234567890', '1234567890@qq.com', '123456')
    print(Detian.info.get_phone())
    Detian.info.update_phone(738423647)
    print(Detian.info.get_phone())
    print(Detian.info.get_email())