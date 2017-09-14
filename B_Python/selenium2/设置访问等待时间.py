from selenium import webdriver

#导入WebDriverWait 包
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
# WebDriverWait()方法使用

element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('kw'))

element.send_keys('selenium')

# 添加智能等待
driver.implicitly_wait(30)
driver.find_element_by_id('su').click()

# 添加固定休眠时间
time.sleep(5)

driver.quit()
