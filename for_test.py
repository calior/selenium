from selenium import webdriver
from time import sleep
from get_Screen import get_Screen
from isElementExist import isElementExist

def  before_xuezha(driver):
	flag = True
	#先行测试循环做题页面，学渣路线
	while(flag):
		try:
			#print('herezuoti')
			if flag == isElementExist(driver,'id','continue'):
				print ("------00000------------------------")
				get_Screen(driver)
				#driver.find_element_by_id('continue').click()
				flag = False
			#获取先行测试截图
			driver.find_element_by_xpath('/html/body/div[4]/div').click() #试题页面点击下一步   continue-submit-answer
			driver.find_element_by_class_name('layui-layer-btn0').click() #点击确定
			#print('走到这了m')
			
		except Exception as e:
			print(e)


def  while_lianxi_no(driver):
	flag = True
	
	while(flag):
		sleep(2)
		print  ("===================22222222===============")
		driver.find_element_by_id('continue').click()#点击视频页面下一步
		sleep(5)
		print  ("===================33333333===============")
		sleep(2)
		driver.find_element_by_id('continue').click()#点击讲义页面下一步
		print  ("===================444444===============")

		sleep(2)
		flag1 = True
		while(flag1):
			sleep(2)
			print  ("===================55555===============")

			driver.find_element_by_id('continue-submit-answer').click() #练习题点击下一步
			driver.find_element_by_class_name('layui-layer-btn0').click() #点击确定
			driver.find_element_by_id('continue-submit-answer').click() #解析卡页面点击下一步
			print  ("===================6666===============")
			sleep(2)
			if(flag1 == isElementExist(driver,'id','continue')):
				get_Screen(driver)
				driver.find_element_by_id('continue').click()
				flag1 = False
			elif(flag == isElementExist(driver,'link','专题报告')):
				get_Screen()
				flag = False



	





