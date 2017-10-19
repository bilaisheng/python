# # 通过poplib模块实现POP3协议来接收邮件
# import poplib
#
# # 输入邮件地址, 口令和POP3服务器地址:
# email = input('Email: ')
# password = input('Password: ')
# pop3_server = input('POP3 server: ')
#
# # 连接到POP3服务器:
# server = poplib.POP3(pop3_server)
# # 可以打开或关闭调试信息:
# server.set_debuglevel(1)
# # 可选:打印POP3服务器的欢迎文字:
# print(server.getwelcome().decode('utf-8'))
#
# # 身份认证:
# server.user(email)
# server.pass_(password)
#
# # stat()返回邮件数量和占用空间:
# print('Messages: %s. Size: %s' % server.stat())
# # list()返回所有邮件的编号:
# resp, mails, octets = server.list()
# # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
# print(mails)
#
# # 获取最新一封邮件, 注意索引号从1开始:
# index = len(mails)
# resp, lines, octets = server.retr(index)
#
# # lines存储了邮件的原始文本的每一行,
# # 可以获得整个邮件的原始文本:
# msg_content = b'\r\n'.join(lines).decode('utf-8')
# # 稍后解析出邮件:
# msg = Parser().parsestr(msg_content)
#
# # 可以根据邮件索引号直接从服务器删除邮件:
# # server.dele(index)
# # 关闭连接:
# server.quit()

# 用POP3获取邮件其实很简单，要获取所有邮件只需要训话使用retr()
# 把每一封邮件内容拿到即可

# 解析邮件
# from email.parser import Parser
# from email.header import decode_header
# from email.utils import parseaddr
#
# import poplib
#
# msg = Parser().parsestr(msg_content)
# 递归第打印出Message对象的层次结构：
# indent用于缩进显示:
# def print_info(msg, indent=0):
#     if indent == 0:
#         for header in ['From', 'To', 'Subject']:
#             value = msg.get(header, '')
#             if value:
#                 if header=='Subject':
#                     value = decode_str(value)
#                 else:
#                     hdr, addr = parseaddr(value)
#                     name = decode_str(hdr)
#                     value = u'%s <%s>' % (name, addr)
#             print('%s%s: %s' % ('  ' * indent, header, value))
#     if (msg.is_multipart()):
#         parts = msg.get_payload()
#         for n, part in enumerate(parts):
#             print('%spart %s' % ('  ' * indent, n))
#             print('%s--------------------' % ('  ' * indent))
#             print_info(part, indent + 1)
#     else:
#         content_type = msg.get_content_type()
#         if content_type=='text/plain' or content_type=='text/html':
#             content = msg.get_payload(decode=True)
#             charset = guess_charset(msg)
#             if charset:
#                 content = content.decode(charset)
#             print('%sText: %s' % ('  ' * indent, content + '...'))
#         else:
#             print('%sAttachment: %s' % ('  ' * indent, content_type))

# 邮件的Subject或者Email中包含的名字都是经过编码后的str要正常显示就必须decode
# def decode_str(s):
#     value, charset = decode_header(s)[0]
#     if charset:
#         value = value.decode(charset)
#     return value
# 文本邮件的内容也是str，还需要检测编码否则费utf-8编码的邮件都无法正常显示：
# def guess_charset(msg):
#     charset = msg.get_charset()
#     if charset is None:
#         content_type = msg.get('Content-Type','').lower()
#         pos = content_type.find('charset=')
#         if pos >= 0:
#             charset = content_type[pos + 8].strip()
#         return charset

# 导入SQLite 驱动
import  sqlite3
# 连接到SQLite 数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录穿件
conn = sqlite3.connect('test.db')
# 创建一个Cursor;
cursor = conn.cursor()
# 执行一条sql语句，创建User表
cursor.execute('create table user(id varchar(20)) primary key, name varchar(20))')
# 继续执行一条sql语句，插入一条记录：
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数:
cursor.rowcount
1
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

'''
总结：
使用python的DB-AP 时，只要搞清楚Connection个和Cursor对象，打开后一定要记得
关闭，就可以放心地使用
使用Cursor对象执行insert，update，delete语句是，执行结构有rowcoun返回
影响的行数就可以拿到执行结果
使用Cursor对象执行select语句时，通过featchall()可以拿到结果集，结果集
是一个list，每个元素都是一个tuple对应一行记录
如果sql语句草油参数那么就需要吧参数按照位置传递给execute()方法，
有几个？占位符就必须对应几个参数，例如：
cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法
'''

'''
一个web应用的本质就是：
    浏览器发送一个http请求
    服务器收到请求生成一个HTML文档
    服务器吧HTML 文档作为http相应的body发送给浏览器
    浏览器收到http响应，从http body 取出HTML文档并显示
    
    WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求
'''
def application(environ, start_response):
    # 发送http响应的header
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

'''
上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
environ：一个包含所有HTTP请求信息的dict对象；
start_response：一个发送HTTP响应的函数。
'''

# 运行WSGI服务
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数：
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

# 从environ里读取PATH_INFO,这样就可以显示
# 更加动态的内容
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

'''
总结：
无论多么复杂的尾巴应用程序，入口都是一个WSGI处理函数，http请求的所有输入信息都可以通过
environ获得，http相应的输出都可以通过start_response()加上函数方绘制作为body。

复杂的web应用程序，光靠一个WSGI函数来处理还是太底层，我们需要在WSGI纸上在抽象出web框架
进一步简化web开发
'''