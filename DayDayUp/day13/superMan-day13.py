# virtualenv
# 图形界面
# Python支持多種圖形界面的第三方庫
# Tk，是一個圖形庫.
# 在gui中，每個Button、label，輸入框等，都是一個widget。frame是可以容納其他widget的widget。
# pack()方法把widget放入父容器中，并實現佈局。pack是最簡單的佈局，grid可以實現複雜的佈局。
# 在createWidgets方法中，我們創建一個label和一個button。quit方法退出。
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        self.helloLabel = Label(self, text='Hello, world')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command = self.quit)
        self.quitButton.pack()

app = Application()
app.master.title('hello,world')
app.mainloop()


class Appli(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app2 = Appli()
app2.master.title('hello world')
app2.mainloop()

# wxWidgets，Qt，GTK

# 网络编程
# TCP/IP简介
# Ip協議負責吧數據從一台計算機通過網絡發送到另一台計算機。數據被分割成一小塊一小塊。
#然後通過IP包發送出去。TCP協議是建立在IP協議上的。TCP協議負責兩台計算機之間建立可靠連接，保證數據包順序到達。，
# TCP協議會通過握手建立連接，然後對每個IP包編號，確保對方按順序收到，若包丟失，就會自動重發。
# 許多更高級的協議都是建立在TCP協議上的，例如瀏覽器的HTTP協議，發送郵件的SMTP協議。
# 一個IP包除了要傳輸的數據外，還包含IP地址和目標IP地址，源端口和目標端口。
# TCP编程
import socket
# 創建一個socket AF_INFO指定使用IPv4，AF_INET6是IPv6。SOCK_STREAM指定使用面向流的TCP協議
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80)) # 建立連接。注意是一個tuple參數
s.send(b'GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection: close\r\n\r\n') # 向新浪發送請求要求返回首頁的內容
# TCP 連接創建的是雙向通道，雙方都可以同時給對方發送數據。
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)
# UDP编程
# udp是面向無連接的協議
# 使用UDP協議不需要建立連接，只要知道對方的IP地址和端口號，就可以直接發送數據包。udp傳輸數據不可靠，但是速度快。
# 使用udp協議，也需要客戶端和服務器
Sudp= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM指定的socket類型是udp。
Sudp.bind(('127.0.0.1', 9999))
print('bind udp on 9999')
while True:
    data, addr=Sudp.recvfrom(1024) # recvfrom方法返回數據和客戶端的地址和端口，服務器收到數據后，直接調用sendto方法把數據用udp發送給客戶端
    print('received from %s:%s'% addr)
    Sudp.sendto(b'hello, %s'% data, addr)
# 客戶端使用udp時，不需要調用connect，直接通過sendto給服務器發送數據。
Cudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'superMan', b'superStar',b'SuperGod']:
    Cudp.sendto(data)
    print(Cudp.recv(1024).decode('utf-8'))
Cudp.close