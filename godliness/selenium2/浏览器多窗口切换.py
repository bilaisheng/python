# 模拟浏览器多窗口切换
# 代码中引入selenium版本为:3.4.3
# 通过Chrom浏览器访问发起请求
# Chrom版本:59 ,chromdriver:2.3
# 需要对应版本的Chrom和chromdriver
# 请联系QQ:878799579

from selenium import webdriver
import time

chrome = webdriver.Chrome()

# 设置窗口最大化
chrome.maximize_window()

# 打开百度首页
chrome.get('http://www.baidu.com')

# 获得当前窗口句柄
nowhandle = chrome.current_window_handle

# 通过js的方式打开新的新闻窗口
chrome.execute_script("window.open('http://news.baidu.com')")
time.sleep(5)

# 输出当前窗口句柄
print(chrome.current_window_handle)

# 获取当前打开所有窗口
allhandles = chrome.window_handles

# 通过循环方式判断窗口是否为当前窗口
for handle in allhandles:
    if nowhandle != handle:

        # 重新回到百度首页
        chrome.switch_to_window(nowhandle)
        time.sleep(5)

        # 关闭百度首页窗口 ,此时只剩下新闻窗口
        chrome.close()
        time.sleep(5)

# 退出
chrome.quit()
