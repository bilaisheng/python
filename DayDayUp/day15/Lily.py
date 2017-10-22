"""
Web开发
HTTP协议简介
HTML简介
WSGI接口
使用Web框架
使用模板
异步IO
协程
asyncio
async/await
aiohttp
"""

# 在Web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让浏览器显示出来。而浏览器和服务器之间的传输协议是HTTP，所以：
# HTML是一种用来定义网页的文本，会HTML，就可以编写网页；
# HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信。
# HTTP请求
# 跟踪了新浪的首页，我们来总结一下HTTP请求的流程：
# 步骤1：浏览器首先向服务器发送HTTP请求，请求包括：
# 方法：GET还是POST，GET仅请求资源，POST会附带用户数据；
# 路径：/full/url/path；
# 域名：由Host头指定：Host: www.sina.com.cn
# 以及其他相关的Header；
# 如果是POST，那么请求还包括一个Body，包含用户数据。
# 步骤2：服务器向浏览器返回HTTP响应，响应包括：
# 响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
# 响应类型：由Content-Type指定；
# 以及其他相关的Header；
# 通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。
# 步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。
# Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。当我们编写一个页面时，
# 我们只需要在HTTP请求中把HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个HTTP请求，因此，一个HTTP请求只处理一个资源。
# HTTP协议同时具备极强的扩展性，虽然浏览器请求的是http://www.sina.com.cn/的首页，但是新浪在HTML中可以链入其他服务器的资源，
# 比如<img src="http://i1.sinaimg.cn/home/2013/1008/U8455P30DT20131008135420.png">，从而将请求压力分散到各个服务器上，
# 并且，一个站点可以链接到其他站点，无数个站点互相链接起来，就形成了World Wide Web，简称WWW。


# 网页就是HTML？这么理解大概没错。因为网页中不但包含文字，还有图片、视频、Flash小游戏，有复杂的排版、动画效果，所以，HTML定义了一套语法规则，来告诉浏览器如何把一个丰富多彩的页面显示出来。
# HTML长什么样？上次我们看了新浪首页的HTML源码，如果仔细数数，竟然有6000多行！
# 所以，学HTML，就不要指望从新浪入手了。我们来看看最简单的HTML长什么样：

# <html>
# <head>
#   <title>Hello</title>
# </head>
# <body>
#   <h1>Hello, world!</h1>
# </body>
# </html>
# HTML文档就是一系列的Tag组成，最外层的Tag是<html>。规范的HTML也包含<head>...</head>和<body>...</body>（注意不要和HTTP的Header、Body搞混了），
# 由于HTML是富文档模型，所以，还有一系列的Tag用来表示链接、图片、表格、表单等等。
# CSS简介
# CSS是Cascading Style Sheets（层叠样式表）的简称，CSS用来控制HTML里的所有元素如何展现，比如，给标题元素<h1>加一个样式，变成48号字体，灰色，带阴影：
#
# <html>
# <head>
#   <title>Hello</title>
#   <style>
#     h1 {
#       color: #333333;
#       font-size: 48px;
#       text-shadow: 3px 3px 3px #666666;
#     }
#   </style>
# </head>
# <body>
#   <h1>Hello, world!</h1>
# </body>
# </html>

# JavaScript虽然名称有个Java，但它和Java真的一点关系没有。JavaScript是为了让HTML具有交互性而作为脚本语言添加的，
# JavaScript既可以内嵌到HTML中，也可以从外部链接到HTML中。如果我们希望当用户点击标题时把标题变成红色，就必须通过JavaScript来实现：

# <html>
# <head>
#   <title>Hello</title>
#   <style>
#     h1 {
#       color: #333333;
#       font-size: 48px;
#       text-shadow: 3px 3px 3px #666666;
#     }
#   </style>
#   <script>
#     function change() {
#       document.getElementsByTagName('h1')[0].style.color = '#ff0000';
#     }
#   </script>
# </head>
# <body>
#   <h1 onclick="change()">Hello, world!</h1>
# </body>
# </html>


# 了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：
# 浏览器发送一个HTTP请求；
# 服务器收到请求，生成一个HTML文档；
# 服务器把HTML文档作为HTTP响应的Body发送给浏览器；
# 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。
# 所以，最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。
# 如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。
# 正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。
# 这个接口就是WSGI：Web Server Gateway Interface。
# WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：
# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello, web!</h1>']
# 上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。
# 在application()函数中，调用：
# start_response('200 OK', [('Content-Type', 'text/html')])
# 就发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。
# start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。
# 通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。
# 然后，函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。
# 有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过start_response()发送Header，最后返回Body。
# 整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，我们只负责在更高层次上考虑如何响应请求就可以了。
# 不过，等等，这个application()函数怎么调用？如果我们自己调用，两个参数environ和start_response我们没法提供，返回的bytes也没法发给浏览器。
# 所以application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。
# 但是现在，我们只想尽快测试一下我们编写的application()函数真的可以把HTML输出到浏览器，所以，要赶紧找一个最简单的WSGI服务器，把我们的Web应用程序跑起来。
# 好消息是Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。
# 运行WSGI服务
# 我们先编写hello.py，实现Web应用程序的WSGI处理函数：
#
# # hello.py
#
# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello, web!</h1>']
# 然后，再编写一个server.py，负责启动WSGI服务器，加载application()函数：
#
# # server.py
# # 从wsgiref模块导入:
# from wsgiref.simple_server import make_server
# # 导入我们自己编写的application函数:
# from hello import application
#
# # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
# httpd = make_server('', 8000, application)
# print('Serving HTTP on port 8000...')
# # 开始监听HTTP请求:
# httpd.serve_forever()

# 了解了WSGI框架，我们发现：其实一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。
# 但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL。
# 每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。
# 一个最简单的想法是从environ变量里取出HTTP请求的信息，然后逐个判断：
# def application(environ, start_response):
#     method = environ['REQUEST_METHOD']
#     path = environ['PATH_INFO']
#     if method=='GET' and path=='/':
#         return handle_home(environ, start_response)
#     if method=='POST' and path='/signin':
#         return handle_signin(environ, start_response)
#     ...
# 只是这么写下去代码是肯定没法维护了。
# 代码这么写没法维护的原因是因为WSGI提供的接口虽然比HTTP接口高级了不少，但和Web App的处理逻辑比，还是比较低级，我们需要在WSGI接口之上能进一步抽象，让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做。
# 由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。
# 这里我们先不讨论各种Web框架的优缺点，直接选择一个比较流行的Web框架——Flask来使用。
# 用Flask编写Web App比WSGI接口简单（这不是废话么，要是比WSGI还复杂，用框架干嘛？），我们先用pip安装Flask：
# $ pip install flask
# 然后写一个app.py，处理3个URL，分别是：

# GET /：首页，返回Home；

# GET /signin：登录页，显示登录表单；

# POST /signin：处理登录表单，显示登录结果。

# 注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。
# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来，所以，我们写出来的代码就像这样：

# from flask import Flask
# from flask import request
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'
#
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'
#
# if __name__ == '__main__':
#     app.run()
# 运行python app.py，Flask自带的Server在端口5000上监听：
#
# $ python app.py
#  * Running on http://127.0.0.1:5000/

# Web框架把我们从WSGI中拯救出来了。现在，我们只需要不断地编写函数，带上URL，就可以继续Web App的开发了。
# 但是，Web App不仅仅是处理逻辑，展示给用户的页面也非常重要。在函数中返回一个包含HTML的字符串，简单的页面还可以，但是，想想新浪首页的6000多行的HTML，你确信能在Python的字符串中正确地写出来么？反正我是做不到。
# 俗话说得好，不懂前端的Python工程师不是好的产品经理。有Web开发经验的同学都明白，
# Web App最复杂的部分就在HTML页面。HTML不仅要正确，还要通过CSS美化，再加上复杂的JavaScript脚本来实现各种交互和动画效果。总之，生成HTML页面的难度很大。
# 由于在Python代码里拼字符串是不现实的，所以，模板技术出现了。
# 使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户：


# 在学习异步IO模型前，我们先来了解协程。
# 协程，又称微线程，纤程。英文名Coroutine。
# 协程的概念很早就提出来了，但直到最近几年才在某些语言（如Lua）中得到广泛应用。
# 子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
# 子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

#
# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
# 用asyncio实现Hello world代码如下：
#
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()