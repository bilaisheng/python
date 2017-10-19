# Web开发
# HTTP协议简介
# web應用中服務器把網頁傳給瀏覽器，實際上是把網頁的HTML代碼發送給瀏覽器，瀏覽器顯示出來。而瀏覽器和服務器之間的傳輸協議就是HTTP
# HTML是一種用來定義網頁的文本 HTTP是在網絡上傳輸HTML的協議，用於瀏覽器和服務器的通信
# HTML简介
# WSGI接口
# WSGI接口，要求web開發者實現一個函數，就可以响应HTTP请求


# def application(environ, start_response):  # 就是符合WSGI标准的一个HTTP处理函数，
#     # environ函数包含所有HTTP请求信息的dict对象
#     # start_response,一个发送HTTP响应的函数
#     start_response('200 ok',[('Content-Type', 'text/html')])
#     return [b'<h1> Hello, web!</h1>']
#
# from wsgiref.simple_server import make_server
# from hello import application
# httpd = make_server('', 8000, application)
# print('server http on port 8000...')
# httpd.serve_forever()

# 使用Web框架
# 其实Web App就是写一个处理WSGI的处理函数，针对每个http请求进行响应。
# 处理多个url
# def application(environ, start_reponse):
#     method = environ['REQUEST_METHOD']
#     path = environ['PATH_INFO']
#     if method=='GET' and path=='/':
#         return handle_home(environ, start_reponse)
#     if method=='POST' and path=='/signin':
#         return handle_signin(environ, start_reponse)
# 简化处理，引用flask
# from  flask import Flask
# from flask import request
# app = Flask(__name__)
#
#
# @app.route('/',methods=['GET','GET'])
# def home():
#     return '<h1>Home</h1>'
#
#
# @app.route('/signin',methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign in</button></p>
#               </form>'''
#
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     if request.form['username'] == 'admin' and request.form['password'] == 'password':
#         return '<h3>hello,admin</h3>'
#     return '<h3>bad username or password.</h3>'
# if __name__ == '__main__':
#     app.run()

# 使用模板
#     from flask import Flask, request, render_template
#
#     app = Flask(__name__)
#
#
#     @app.route('/', methods=['GET', 'POST'])
#     def home():
#         return render_template('home.html')
#
#
#     @app.route('/signin', methods=['GET'])
#     def signin_form():
#         render_template('form.html')
#
#
#     @app.route('/signin', methods=['POST'])
#     def signin():
#         username = request.form['username']
#         password = request.form['password']
#         if username == 'admin' and password == 'password':
#             return render_template('signin-ok.html', username=username)
#         return render_template('form.html', message='Bad usernaem or password', username=username)
# 异步IO
# CPU的速度远快于磁盘，网络。在一个线程中，CPU执行代码的速度极快，然而，一旦遇到IO的操作，例如读写文件，发送网络数据时，
        # 就需要等待IO操作的完成，才能进行下一步操作 。这种情况叫做同步IO
# 异步IO。当代码需要执行一个耗时的IO操作时，他只发出IO指令，并不等待IO结果，就去执行其他代码。一段时间后，当IO返回结果时，在通知CPU处理

# 协程
# 子程序调用总是一个入口一次返回，调用顺序是明确的。而协程在执行过程中，子程序内部可中断，然后转而执行别的子程序，在合适的时候在放回来执行。
# 协程最大的优势就是极高的执行效率。因为子程序的切换不是线程切换，而是程序自身控制。
# 第二大优势是不需要多线程的锁机制。因为只有一个线程，也不存在同时写变量的冲突，既充分利用多核，又充分发挥协程的高效率。
# python对协程的支持是通过generator实现的。在generator中，我们不但可以通过for循环，还可以不断调用next函数获取yield语句发挥下一个值
# Python的yield不但可以返回一个值，还可以接收调用者的参数。


# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n+1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#         c.close()
# c = consumer()
# produce(c)
# asyncio
# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print("hello world")
#     r = yield  from asyncio.sleep(1)  # 异步调用asyncio.sleep(1
#     print('hello again!')
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()
# import threading
# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print('hello world!(%s)' % threading.currentThread())
#     yield  from asyncio.sleep(1)
#     print('hello again!(%s)' % threading.currentThread())
# loop = asyncio.get_event_loop()
# tasks=[hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET/HTTP/1.0\r\nHost:%s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield  from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header> %s' % (host, line.decode('utf-8').rstrip()))
#         writer.close()
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# async/await ?????
# import asyncio
# async def hello():
#     print('hello world')
#     r = await asyncio.sleep(1)
#     print("hello again")
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

# aiohttp
import asyncio
from aiohttp import web
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>index</h1>')
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()