from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

print('浏览器最大化')

driver.maximize_window()

#driver.quit()