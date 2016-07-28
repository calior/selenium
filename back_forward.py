#coding utf-8
from selenium import webdriver
import time
#访问百度首页
driver = webdriver.Chrome()
first_url = 'http://www.baidu.com'
driver.get(first_url)
print('现在url是百度首页%s',first_url)
time.sleep(3)
#访问百度新闻首页
second_url = 'http://news.baidu.com'
driver.get(second_url)
print('现在url是新闻首页%s',second_url)
time.sleep(3)
#返回到百度首页
driver.back()
print()
print('现在url是百度首页%s',first_url)
time.sleep(3)

#前进到新闻页面
driver.forward()
print('现在url是新闻首页%s',second_url)
time.sleep(3)

driver.quit()

