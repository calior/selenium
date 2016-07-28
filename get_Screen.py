# coding: UTF-8
from selenium import webdriver
import time

def get_Screen(driver):
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	name = 'test_new' + now
	driver.get_screenshot_as_file('./screen/'+name+'.jpg')
	print(name)