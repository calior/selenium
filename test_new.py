from selenium import webdriver
import time
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from get_Screen import get_Screen
from for_test import before_xuezha,while_lianxi_no
from isElementExist import isElementExist
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
base_url = "http://test-new.classba.com.cn/index.php/index/index/token/ecyxJp1hapWQiOjEyMywidG9waWNfaWQiOjEsInVuYW1lIjoieGlhb2xhbjEyMyIsInZlcmlmeSI6Im5hbmppbmcxMiJ9"
base_url1 = 'http://test-new.classba.com.cn/index.php/index/index/token/ecyxJp1hapWQiOjEyMjEsInRvcGljX2lkIjoxMCwidW5hbWUiOiJ4aWFvbGFuMTIyMSIsInZlcmlmeSI6Imt1bnNoYW4xNCJ9'
driver.get(base_url1)
#判断是否在首页视频
before_video_flag = isElementExist(driver,'class','vjs-poster')
#判断是否在边学边练视频
while_video_flag = isElementExist(driver,'class','k-topic-video')
#判断是否在学习程度选择页面
level_flag = isElementExist(driver,'class','page-img')
#判断是否在做题页面
exam_flag = isElementExist(driver,'id','answer-sheet')

print(before_video_flag,while_video_flag,level_flag,exam_flag)
try:
	if before_video_flag == True and while_video_flag == False:#首页视频页面
		#print('111')
		driver.find_element_by_xpath('/html/body/div[4]/div').click()
		#element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.XPATH,'/html/body/div[4]/div'))
		#element.click()
		#print('1')
		sleep(2)
		driver.find_element_by_xpath('/html/body/div[2]/div').click()
		#WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.XPATH,'/html/body/div[2]/div')).click()
		before_xuezha(driver)
		#print('晚饭-================================================')
		while_lianxi_no(driver)
	elif level_flag:#学习程度页面
		#driver.implicitly_wait(10)
		driver.find_element_by_xpath('/html/body/div[2]/div').click()
		
		#WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.XPATH,'/html/body/div[2]/div')).click()
		before_xuezha(driver)
		while_video_flag(driver)
	elif exam_flag:#做题页面
		print('在做题页面')
		before_xuezha(driver)
		while_lianxi_no(driver)
	else:
		print('此链接已经用过，无法测试，请检查!')
		print('当前页面url为',base_url)
		get_Screen(driver)
except Exception as e:
	print(e)
	get_Screen(driver)
driver.quit()