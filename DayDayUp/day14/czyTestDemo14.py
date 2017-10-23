# SMTP发送邮件
# SMTP是发送邮件的协议，Python内置对SMTP的支持，
# 可以发送纯文本邮件、HTML邮件以及带附件的邮件
# 构建一个简单的纯文本邮件
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 通过SMTP发出去：
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

'''
说明:
1、Python对SMTP支持有smtplib和email两个模块，
email负责构造邮件，smtplib负责发送邮件。
2、构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'
text/plain'，最后一定要用utf-8编码保证多语言兼容性
3、用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。login()方法用来
登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
'''
'''
上面的程序存在的问题是：
邮件没有主题；
收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
明明收到了邮件，却提示不在收件人中。

这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，
而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText
中，才是一封完整的邮件
'''

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 编写一个_format_addr()来格式化一个邮件地址，注意不能简单的传入
# name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码


# 发送html邮件
#在构造MIMEText 对象时，吧HTML字符串传进去，在把第二个参数有plain变为HTML就可以了
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')

# 发送附件
# '''
# 可以构造一个MEMEMultipart对象代表幽暗本身，然后
# 往里面加上一个MIMEText作为邮件正文，在继续往里面加上表示附加的MEMEBase
# 对象即可：
# '''
# # 邮件对象:
# msg = MIMEMultipart()
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#
# # 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
#
# # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
# with open('/Users/michael/Downloads/test.png', 'rb') as f:
#     # 设置附件的MIME和文件名，这里是png类型:
#     mime = MIMEBase('image', 'png', filename='test.png')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition', 'attachment', filename='test.png')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)

# 发送图片
# '''
# 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
# 如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
# 把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片
# '''
# msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
#     '<p><img src="cid:0"></p>' +
#     '</body></html>', 'html', 'utf-8'))

# 利用MEMEMultipari 就可以组合一个html和plain，要注意指定subtype是alternative
# msg = MIMEMultipart('alternative')
# msg['From'] = ...
# msg['To'] = ...
# msg['Subject'] = ...
#
# msg.attach(MIMEText('hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# 正常发送msg对象...

# 加密SMTP
# 实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()
# # 剩下的代码和前面的一模一样:
# server.set_debuglevel(1)

'''
使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的
构造方法，正确设置好邮件头，就可以顺利发出。

构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，
就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示一个
作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，
而MIMEBase可以表示任何对象。它们的继承关系如下：
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
'''