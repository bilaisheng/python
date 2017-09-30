# 电子邮件
# SMTP发送邮件
# POP3收取邮件
# 访问数据库
# 使用SQLite
# 使用MySQL
# 使用SQLAlchemy

# 照github练习， 不知道SMTP server 地址，跳过
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
# import smtplib
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')
#
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# from email.parser import Parser
# from email.header import decode_header
# from email.utils import parseaddr
#
# import poplib
#
# # 输入邮件地址, 口令和POP3服务器地址:
# email = input('Email: ')
# password = input('Password: ')
# pop3_server = input('POP3 server: ')
#
# def guess_charset(msg):
#     charset = msg.get_charset()
#     if charset is None:
#         content_type = msg.get('Content-Type', '').lower()
#         pos = content_type.find('charset=')
#         if pos >= 0:
#             charset = content_type[pos + 8:].strip()
#     return charset
#
# def decode_str(s):
#     value, charset = decode_header(s)[0]
#     if charset:
#         value = value.decode(charset)
#     return value
#
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
#
# # 连接到POP3服务器:
# server = poplib.POP3(pop3_server)
# # 可以打开或关闭调试信息:
# server.set_debuglevel(1)
# # 可选:打印POP3服务器的欢迎文字:
# print(server.getwelcome().decode('utf-8'))
# # 身份认证:
# server.user(email)
# server.pass_(password)
# # stat()返回邮件数量和占用空间:
# print('Messages: %s. Size: %s' % server.stat())
# # list()返回所有邮件的编号:
# resp, mails, octets = server.list()
# # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
# print(mails)
# # 获取最新一封邮件, 注意索引号从1开始:
# index = len(mails)
# resp, lines, octets = server.retr(index)
# # lines存储了邮件的原始文本的每一行,
# # 可以获得整个邮件的原始文本:
# msg_content = b'\r\n'.join(lines).decode('utf-8')
# # 稍后解析出邮件:
# msg = Parser().parsestr(msg_content)
# print_info(msg)
# # 可以根据邮件索引号直接从服务器删除邮件:
# # server.dele(index)
# # 关闭连接:
# server.quit()

# import sqlite3
#
# # 连接到SQLite数据库
# # 数据库文件是test.db
# # 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect('test.db')
# # 创建一个Cursor:
# cursor = conn.cursor()
# # 执行一条SQL语句，创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# # 通过rowcount获得插入的行数:
# print('rowcount =', cursor.rowcount)
# # 关闭Cursor:
# cursor.close()
# # 提交事务:
# conn.commit()
# # 关闭Connection:
# conn.close()
#
# # 查询记录：
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# # 执行查询语句:
# cursor.execute('select * from user where id=?', '1')
# # 获得查询结果集:
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()


# import mysql.connector
#
# # change root password to yours:
# conn = mysql.connector.connect(user='root', password='password', database='test')
#
# cursor = conn.cursor()
# # 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
# print('rowcount =', cursor.rowcount)
# # 提交事务:
# conn.commit()
# cursor.close()
#
# # 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
# # 关闭Cursor和Connection:
# cursor.close()
# conn.close()


'''
sqlalchemy 提前准备好数据库 ，否则执行失败
'''

# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# # 创建对象的基类:
# Base = declarative_base()
#
# # 定义User对象:
# class User(Base):
#     # 表的名字:
#     __tablename__ = 'user'
#
#     # 表的结构:
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#
# # 初始化数据库连接:
# engine = create_engine('mysql+mysqlconnector://root:123456@127.0.0.1:3306/test')
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)
#
# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()
#
# # 创建Session:
# session = DBSession()
# # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.id=='5').one()
# # 打印类型和对象的name属性:
# print('type:', type(user))
# print('name:', user.name)
# # 关闭Session:
# session.close()