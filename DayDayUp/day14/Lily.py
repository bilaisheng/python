"""
电子邮件
SMTP发送邮件
POP3收取邮件
访问数据库
使用SQLite
使用MySQL
使用SQLAlchemy
"""

# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
# 首先，我们来构造一个最简单的纯文本邮件：

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
# 然后，通过SMTP发出去：

# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。
# login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，
# 邮件正文是一个str，as_string()把MIMEText对象变成str。

# POP3协议本身很简单，以下面的代码为例，我们来获取最新的一封邮件内容：

import poplib

# 输入邮件地址, 口令和POP3服务器地址:
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

# 连接到POP3服务器:
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()


# SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
# 在使用SQLite前，我们先要搞清楚几个概念：
# 表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
# 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
# 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
# 由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。
# 我们在Python交互式命令行实践一下：
# # 导入SQLite驱动:
#import sqlite3
# # 连接到SQLite数据库
# # 数据库文件是test.db
# # 如果文件不存在，会自动在当前目录创建:
#conn = sqlite3.connect('test.db')
# # 创建一个Cursor:
#cursor = conn.cursor()
# # 执行一条SQL语句，创建user表:
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# <sqlite3.Cursor object at 0x10f8aa260>
# # 继续执行一条SQL语句，插入一条记录:
#cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# <sqlite3.Cursor object at 0x10f8aa260>
# # 通过rowcount获得插入的行数:
#cursor.rowcount
# 1
# # 关闭Cursor:
#cursor.close()
# # 提交事务:
#conn.commit()
# # 关闭Connection:
#conn.close()
# 我们再试试查询记录：
#
#conn = sqlite3.connect('test.db')
#cursor = conn.cursor()
# # 执行查询语句:
#cursor.execute('select * from user where id=?', ('1',))
# <sqlite3.Cursor object at 0x10f8aa340>
# # 获得查询结果集:
#values = cursor.fetchall()
#values
# [('1', 'Michael')]
#cursor.close()
#conn.close()
# 使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

# 安装MySQL
# 可以直接从MySQL官方网站下载最新的Community Server 5.6.x版本。MySQL是跨平台的，选择对应的平台下载安装文件，安装即可。
# 安装时，MySQL会提示输入root用户的口令，请务必记清楚。如果怕记不住，就把口令设置为password。
# 在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。
# 重启MySQL后，可以通过MySQL的客户端命令行检查编码：

# $ mysql -u root -p

# 安装MySQL驱动
#
# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。
# MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：
#
# $ pip install mysql-connector-python --allow-external mysql-connector-python
# 如果上面的命令安装失败，可以试试另一个驱动：
#
# $ pip install mysql-connector
# 我们演示如何连接到MySQL服务器的test数据库：
#
# # 导入MySQL驱动:
# import mysql.connector
# # 注意把password设为你的root口令:
# conn = mysql.connector.connect(user='root', password='password', database='test')
# cursor = conn.cursor()
# # 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# cursor.rowcount
# 1
# # 提交事务:
# conn.commit()
# cursor.close()
# # 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# values
# [('1', 'Michael')]
# # 关闭Cursor和Connection:
# cursor.close()
# True
# conn.close()

# 首先通过pip安装SQLAlchemy：
#
# $ pip install sqlalchemy
# 然后，利用上次我们在MySQL的test数据库中创建的user表，用SQLAlchemy来试试：
#
# 第一步，导入SQLAlchemy，并初始化DBSession：
#
# # 导入:
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
# engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)
# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class，例如School：
#
# class School(Base):
#     __tablename__ = 'school'
#     id = ...
#     name = ...
# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
#
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
# 你只需要根据需要替换掉用户名、口令等信息即可。
#
# 下面，我们看看如何向数据库表中添加一行记录。
#
# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
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
# 可见，关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。
#
# 如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下：
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
# 运行结果如下：
#
# type: <class '__main__.User'>
# name: Bob
# 可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。
#
# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
#
# 例如，如果一个User拥有多个Book，就可以定义一对多关系如下：
#
# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
#     books = relationship('Book')
#
# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))