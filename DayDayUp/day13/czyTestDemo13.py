# # 第一步是导入Tkinter包的所有内容
# from tkinter import *
#
# # 第二步是从Frame派生一个Application类，这是所有Widget的父容器
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()
#
# '''
# 说明：
# 在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
# pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
# 在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出
# '''
# # 第三步，实例化Application，并启动消息循环
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()


# # 文本输入
# from tkinter import *
# import tkinter.messagebox as messagebox
#
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
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)
#
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()

# # TCP编程
# '''
# 大多数连接都是可靠的TCP连接时，创建TCP连接时，主动发起连接的交客户端，被动
# 相应连接的交服务器
# '''
# # 创建一个基于TCP
# # 导入socket库:
# import socket
#
# # 创建一个socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('www.sina.com.cn', 80))
# # 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# '''
# 说明：
# 创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，
# 就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，
# 这样，一个Socket对象就创建成功，但是还没有建立连接。
# 客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号
# 建立TCP连接后我们就可以向新浪服务器发送请求，要求放回首页的内容
#
# TCP连接创建的是双向通道，双发都可以同时给对方发送数据，但是谁先发税后发
# 怎么协调都是根据具体的协议来决定的。例如：http协议规定客户端必须先发请求给服务器，
# 服务器收到后才发送数据给客户端
# '''
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     # 接受数据是调用recv(max)方法，一次指定最后接收的字节数
#     # 在一个while循环中反复接受，知道revv()返回空数据，表示接受完毕，退出循环
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# # 接受完数据后调用close()方法关闭Socket,这样一次完整的网络通信就结束了
# # 关闭连接:
# s.close()
#
# # 接收到的数据包括http头和网页本身。我们只需要把http头和
# # 网页分离一下，吧http头打印出来，网页内容保存到文件：
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

'''
服务器变成：
服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。
所以，服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接。由于服务器会有大量来自客户端的连接，所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。一个Socket依赖4项：
服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。
但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。
'''
# import socket
# import  threading
# import tkinter.messagebox as messagebox
# # 首先创建一个基于IPv4和TCP协议的Socket：
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 然后绑定坚挺的地址和端口
# # 监听端口:
# s.bind(('127.0.0.1', 9999))
# # 接着调用listen（）方法开始坚挺端口，传入的参数指定等待连接的最大数量
# s.listen(5)
# print('Waiting for connection...')
# # 接下来，服务器程序通过一个永久循环来接受来自客户端的连接，
# # accept(）会等待并返回一个客户端的连接：
# while True:
#     # 接受一个新连接:
#     sock, addr = s.accept()
#     # 创建新线程来处理TCP连接:
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()
#
# # 每个连接都必须创建系线程（或进程连处理），否则，单线程在处理
# # 连接的过程中无法接受其他客户端的连接：
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
# # 要测试上面的服务器程序我们还需要编写一个客户端程序：
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








