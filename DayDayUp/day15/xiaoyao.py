# Web开发
# HTTP协议简介
# HTML简介
# WSGI接口
# 使用Web框架
# 使用模板
# 异步IO
# 协程
# asyncio
# async/await
# aiohttp

# def application(environ, start_response):
# 	start_response('200 OK', [('Content-Type', 'text/html')])
# 	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
# 	return [body.encode('utf-8')]

# from wsgiref.simple_server import make_server

# # 同一文件直接使用
# from hello import application

# httpd = make_server('', 8000, application)
# print('Serving HTTP on port 8000...')

# httpd.serve_forever()

# # flask
# from flask import Flask
# from flas import request

# app = Flask(__name__)


# @app.route('/', methods=['GET'])
# def signin_form():
# 	return '''<form action="/siginin" method="post">
# 			  <p><input name="username"></p>
# 			  <p><input name="password" type="password"></p>
# 			  <p><button type="submit">Sign In</button></p>
# 			  </form>'''


# @app.route('/signin', methods=['POST'])
# def signin():
# 	# 需要从request对象读取表单内容
# 	if request.form['username'] == 'admin' and request.form['password'] == 'password':
# 		return '<h3>Hello, admin!</h3>'
# 	return '<h3>Bad username or password.</h3>'

# if __name__ == '__main__':
# 	app.run()

# # 地址输入 ：http://localhost:8000/signin


# # 协程
# def consumer():
# 	r = ''
# 	while True:
# 		n = yield r
# 		if not n:
# 			return
# 		print('[CONSUMER] Consuming %s...' % n)
# 		r = '200 OK'


# def produce(c):
# 	c.send(None)
# 	n =0
# 	while n < 5:
# 		n = n + 1
# 		print('[PRODUCER] Producing %s...' % n)
# 		r = c.send(n)
# 		print('[PRODUCER] Consumer return: %s' % r)
# 	c.close()

# c = consumer()
# produce(c)

# asyncio client  server 放到同一文件，不能执行。需区分

# import asyncio


# @asyncio.coroutine
# def simple_echo_server():
# 	# Start a socket server, call back for each client connected.
#     # The client_connected_handler coroutine will be automatically converted to a Task
#     yield from asyncio.start_server(client_connected_handler, 'localhost', 2222)


# @asyncio.coroutine
# def client_connected_handler(client_reader, client_writer):
# 	# Runs for each client connected
# 	# client_reader is a StreamReader object
# 	# client_writer is a StreamWriter object
# 	print("Connection received!")
# 	while True:
# 		data = yield from client_reader.read(8192)
# 		if not data:
# 			break
# 		print(data)
# 		client_writer.write(data)


# loop = asyncio.get_event_loop()
# loop.run_util_complete(simple_echo_server())
# try:
# 	loop.run_forever()
# finally:
# 	loop.close()


# # 客户端
# import asyncio

# LASTLINE = b'Last line.\n'


# @asyncio.coroutine
# def simple_echo_client():
# 	# Open a connection and write a few lines by using the StreamWriter object
#     #reader, writer = yield from asyncio.open_connection('localhost', 2222)
#     # reader is a StreamReader object
#     # writer is a StreamWriter object
#     writer.write(b'First line.\n')
#     writer.write(b'Second line.\n')
#     writer.write(b'Third line.\n')
#     writer.write(LASTLINE)

#     # Now, read a few lines by using the StreamReader object
#     print("Lines received")
#     while True:
#     	line = yield from reader.readline()
#     	print(line)
#     	if line == LASTLINE or not line:
#     		break
#     writer.close()


# loop = asyncio.get_event_loop()
# loop.run_util_complete(simple_echo_client())


# # async hello
# import threading
# import asyncio

# async def hello():
# 	print('Hello world! (%s)' % threading.currentThread())
# 	await asyncio.sleep(1)
# 	print('Hello again! (%s)' % threading.currentThread())

# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_util_complete(asyncio.wait(tasks))
# loop.close()


# aio

'''
async web application.
'''

import asyncio

from aiohttp import web

async def index(request):
	await asyncio.sleep(0.5)
	return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
	await asyncio.sleep(0.5)
	text = '<h1>hello, %s!</h1>' % request.match_info['name']
	return web.Response(body=text.encode('utf-8'))

async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	app.router.add_route('GET', '/hello/{name}', hello)
	arv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
	print('Server started at http://127.0.0.1:8000...')
	return srv
loop = asyncio.get_event_loop()
loop.run_util_complete(init(loop))
loop.run_forever()