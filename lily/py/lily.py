import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('http://www.taobao.com/robots.txt')
rp.read()
rp.can_fetch('Googlebot','https://www.taobao.com')
s=rp.can_fetch('Googleboot','https://www.taobao.com/artcle')
print(s)

# 对爬虫进行限速
# 添加间隔时间
# import time
# sleep(2)
# 爬虫下载网页的时候
# 上次访问的时间，因为网络原因，他两次访问之间已经存在5秒延迟，7秒的访问间隔
# 保存深度，字典{url:0}

