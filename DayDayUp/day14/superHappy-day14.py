# 电子邮件
# 電子郵件軟件被稱為MUA：Mail User Agent 郵件用戶代理。郵件email從發出去不是直接到達對方電腦，而是MTA ：Mail Transfer Agent 郵件傳輸代理
# 比如網易，新浪等。 Email到達比如網易的MTA后，網易的MTA會把email投遞到郵件的最終目的地MDA：mail Delivery Agent --郵件投遞代理
# 具體路徑類似：發件人->MUA(郵件用戶代理)->MTA（郵件傳輸代理）->MTA->若干MTA->MDA（郵件投遞代理）<-MUA<-收件人
# 因此編寫程序需要：MUA把郵件發送到MTA，MUA從MDA上收取郵件。
# SMTP发送邮件
# SMTP是發送郵件的協議，python內置對SMTP的支持，可以發送純文本郵件、HTML以及附帶的郵件
# python對SMTP支持有smtplib和email兩個模塊，email負責構造郵件，smtplib負責發送郵件
from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from  email.utils import parseaddr,formataddr
import  smtplib

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8') # 第一個參數是郵件正文，第二個參數是MIME的subtype，傳入’plain‘表示純文本，最後一定要用utf-8保證語言兼容性
# from_addr = input('From: ')  # 輸入Email地址
# password = input('Password: ')  # 口令
# to_addr = input('To: ')  # 輸入收緊人的地址
# smtp_server = input('SMTP server: ')  # 輸入SMTP服務器的地址
# import smtplib
# server = smtplib.SMTP(smtp_server, 25)  # smtp協議默認端口是25
# server.set_debuglevel(1)  # 就可以打印出和SMTP服務器交互的所有信息。
# server.login(from_addr,password) # 登錄SMTP服務器
# server.sendmail(from_addr,[to_addr], msg.as_string())  # 發送郵件，一次可發送多人，所傳入list，as——string把MIMEText對象變成str
# server.quit()
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = _format_addr('Python愛好者<%s>' % from_addr)
# msg['To'] = _format_addr('管理員<%s>'% to_addr)
# msg['Subject'] = Header('來自SMTP的問候......', 'utf-8').encode()

# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()
# 發送HTML郵件
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
# 發送附件
# def MIMEMultipart():
#     from_addr = input('From: ')
#     password = input('Password: ')
#     to_addr = input('To: ')
#     smtp_server = input('SMTP server: ')
#
# msg = MIMEMultipart()
#
# msg['From'] = _format_addr('Python愛好者<%s>' % from_addr)
# msg['To'] = _format_addr('管理員<%s>'% to_addr)
# msg['Subject'] = Header('來自SMTP的問候......', 'utf-8').encode()
# msg.attach(MIMEText('send witg file...', 'plain', 'utf-8'))
# with open('E:\github_Clone\python2\python\dengfenghong\day12\/blur.png','rb') as f
#     mime = MIMEBase('image','png',filename='blur.png')
#     mime.add_header('Content-Disposition','attachment',filename='blur.png')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachemnt-Id', '0')
#     mime.set_payload(f.read())
#     encoders.encode_base64(mime)
#     msg.attach(mime)

# 發送圖片
# HTML中通過引用src=“cid:0”就可以把附件作為圖片嵌入。若有多個圖片依次編號
#     msg.attach(MIMEText('<html><body<h1>hello</h1>'+
#                         '<p><img src="cid:0"></p>'+
#                         '</body></html>','html','utf-8'))
# POP3收取邮件
# 收取郵件分為倆步。用poplib把郵件下載導本地，用email解析原始文本，還原郵件對象
# import poplib
# from email.parser import Parser
# from email.header import decode_header
# from email.utils import parseaddr
# email = input('Email: ')
# password = input('Password: ')
# pop3_server = input('POP3 server:')
# server = poplib.POP3(pop3_server)  # 連接到POP3服務器
# server.set_debuglevel(1)  # 可以打開或關閉調試信息
# print(server.getwelcome().decode('utf-8')) # 可選。打印pop3服務器的歡迎文字
# # 身份認證
# server.user(email)
# server.pass_(password)
# # stat()返回郵件數量和佔用空間
# print('message：%s.Size:%s' % server.stat())
# resp, mails, octets=server.list()  # list返回郵件數量和郵件編號
# print(mails)
# # 獲取最新一封郵件，注意索引號從1開始
# index = len(mails)
# resp, lines, octets = server.retr(index)
# # lines存儲了郵件的原始文本的每一行，可以獲取整個郵件的原始文本
# msg_content = b'\r\n'.join(lines).decode('utf-8')
# msg = Parser().parsestr(msg_content)
# server.quit()
# def print_info(msg, indent=0):
#     if indent == 0:
#         for header in ['From', 'To', 'Subject']:
#             value = msg.get(header, '')
#             if value:
#                 if header == 'Subject':
#                     value = decode_str(value)
#                 else:
#                     hdr, addr = parseaddr(value)
#                     name = decode_str(hdr)
#                     value =u'%s<%s>' % (name, addr)
#                 print('%s%s:%s' % (''* indent,header, value))
#
#     if (msg.is_multipart()):
#         parts = msg.get_payload()
#         for n, part in enumerate(parts):
#             print('%spart %s' % ('' * indent, n))
#             print('%s-------------' % ('' * indent))
#             print_info(part, indent + 1)
#     else:
#         content_type = msg.get_content_type()
#         if content_type == 'text/plain' or content_type == 'text/html':
#             content = msg.get_payload(decode= True)
#             charset = guess_charset(msg)
#             if charset:
#                 content = content.decode(charset)
#             print('%sTest: %s' % ('' * indent, content + '...'))
#         else:
#             print('%sAttrachment：%s' % ('' * indent, content_type))
#
#
# def guess_charset(msg):
#     charset = msg.get_charset()
#     if charset is None:
#         content_type = msg.get('Content-Type', '').lower()
#         pos = content_type.find('charset =')
#         if pos >= 0:
#             charset = content_type[pos + 8:].strip()
#     return charset
#
#
# def decode_str(s):
#     value, charset = decode_header(s)[0]
#     if charset:
#         value = value.decode(charset)
#     return value
# 访问数据库
# 使用SQLite
# SQLite是一種嵌入式數據庫，他的數據庫是一個文件。python內置了SQLite3.
import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#cursor.execute('create table user(id VARCHAR (20) PRIMARY KEY , name VARCHAR (20))')
cursor.execute('insert into user(id,name) VALUES (\'122\', \'Michael\')')
print(cursor.rowcount)
cursor.close()
conn.commit()
cursor2 = conn.cursor()
cursor2.execute('SELECT * from user ')
values = cursor2.fetchall()
print(values)
conn.close()
# 使用MySQL
# import mysql.connector
# myconn = mysql.connector.connect(user ='root',password='password')
# mycursor = myconn.cursor()
# mycursor.execute('create table user(id VARCHAR(20) PRIMARY KEY ,NAME  VARCHAR (20))')
# mycursor.execute('insert into USER(id, NAME ) VALUES (%s,%s)', ['1','super'])
# mycursor.rowcount
# myconn.commit()
# mycursor.close()
# sqlcursor = conn.cursor()
# sqlcursor.execute('select * FROM  user where id =%s',('1',))
# values = sqlcursor.fetchall()
# sqlcursor.close()
# 使用SQLAlchemy
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    # 創建對象的基類
    _tablename_='user'
    # 表結構
    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    # 初始化數據庫鏈接
engine = create_engine('mysql+mysqlconnector://root:passwoed@localhost:3306/test')
    # 創建DBSession類型
DBSession = sessionmaker(bind=engine)

# 創建Session對象
session = DBSession()
new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()
# SQLAlchemy提供的查询接口
session = DBSession()
user = session.query(User).filter(User.id == 5).one()
print('type:'.type(user))
print('name', user.name)
session.close()



