# virtualenv
# 图形界面
# 网络编程
# TCP/IP简介
# TCP编程
# UDP编程

# virtualenv 无多个python版本  故跳过

'''
Python支持多种图形界面的第三方库，包括：
Tk,wxWidget,Qt,GTK
Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
所以，我们的代码只需要调用Tkinter提供的接口就可以了。
'''

# from tkinter import *
# from tkinter import Label
#
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLable = Label(self, text='hello world!')
#         self.helloLable.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()
#
# # app = Application()
# # # 设置窗口标题:
# # app.master.title('A Title')
# # # 主消息循环
# # app.mainloop()
#
# import tkinter.messagebox as messagebox
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alterButton = Button(self, text='hello', command = self.hello)
#         self.alterButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello %s' % name)
#
# app = Application()
# # 设置标题
# app.master.title('Alert Message')
# # 主消息循环
# app.mainloop()

# TCP
import socket

# 创建一个socket
from twisted.internet import tcp

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('www.sina.com.cn', 80))

# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收1K字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)

# 监听端口

# # 下方代码测试时候进行分开 ， 否则失败 ，现有合成一个文件
# import threading,time
#
#
# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)
#
# while True:
#     # 接受一个新连接
#     sock, addr = s.accept()
#     # 创建新线程来处理TCP连接
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('127.0.0.1', 9999))
# # 接收欢迎消息:
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()



# UDP SERVER

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)

# udp CLIENT


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()