# 模拟浏览器前进后退操作
# 代码中引入selenium版本为:3.4.3
# 通过Chrom浏览器访问发起请求
# Chrom版本:59 ,chromdriver:2.3
# 需要对应版本的Chrom和chromdriver 请联系QQ:878799579

from selenium import webdriver

# 通过Chrome访问
driver = webdriver.Chrome()

# 访问百度首页
first_url = 'http://www.baidu.com'
print('now access %s' % first_url)
driver.get(first_url)

# 访问新闻页面
second_url = 'http://news.baidu.com'
print('now access %s' % second_url)
driver.get(second_url)

# 返回(后退) 到百度首页
print('back to %s' % first_url)
# 返回
driver.back()

# 前进到新闻页面
print('forward to %s' % second_url)
# 前进
driver.forward()

# 关闭浏览器
driver.quit()