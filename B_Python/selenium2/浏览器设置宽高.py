# 发起请求,设置浏览器宽高

# 代码中引入selenium版本为:3.4.3
# 通过Chrom浏览器访问发起请求
# Chrom版本:59 ,chromdriver:2.3
# 需要对应版本的Chrom和chromdriver
# 请联系QQ:878799579

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

# 设置浏览器全屏
# driver.maximize_window()

print('设置浏览器宽度为800  高度为800')

driver.set_window_size(800, 800)

#退出(关闭浏览器)
driver.quit()