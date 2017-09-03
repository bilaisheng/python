from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()

# 访问百度
browser.get("http://www.baidu.com")

# 模拟用户点击登录按钮操作
# xx = browser.find_element_by_name('tj_login')
browser.get('https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F')
# rows = browser.find_elements_by_css_selector(".TCP_RowOdd,.TCP_RowEven")


# # 找到弹框的div
# browser.find_element_by_class_name('tang-content')
# time.sleep(5)
#
# # 填入用户名
# browser.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('username')
# time.sleep(5)
#
# # 填入密码
# browser.find_element_by_id('TANGRAM__PSP_8__password').send_keys('password')
# time.sleep(5)

