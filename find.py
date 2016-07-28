from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import ctime

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')
try:
	print(ctime())
	link = driver.find_element_by_link_text('设置')
	ActionChains(driver).move_to_element(link).perform()
	driver.find_element_by_link_text('搜索设置').click()
	driver.get_screenshot_as_file('D:\\2tu\\baidu.jpg')
	driver.find_element_by_id('save').click()
	driver.switch_to_alert().accept()
except NoSuchElementException as e:
	print(e)
finally:
	print(ctime())
 