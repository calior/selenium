# coding=utf-8
from selenium import webdriver
from time import *
from selenium.webdriver.common.action_chains  import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
'''
#获取输入框尺寸
size = driver.find_element_by_id('kw').size
print(size)
#获取底部备案信息text
#text1 = driver.find_element_by_id('cp').text
#print(text1.decode('utf-8'))
above = driver.find_element_by_link_text('更多产品')

ActionChains(driver).move_to_element(above).perform()
ActionChains(driver).drag_to_drop(element,target).perform()
'''
driver.find_element_by_id('kw').send_keys('selenium')
sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)

driver.find_element_by_id('kw').clear()

driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys('教程')
sleep(2)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
sleep(2)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
sleep(2)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
sleep(2)

now_url = driver.current_url
print(now_url)
title = driver.title
print(title)









