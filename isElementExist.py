
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WedDriverWait
from selenium.webdriver.support import expected_conditions as EC

def isElementExist(driver,method,element):
	flag1 = True
	if method == 'id':
		try:
			#print ("------------99977777777779-------")
			driver.find_element_by_id(element)
			#print ("------------888866666666-------")	
			#WedDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.ID,element))
			return flag1
		except:
			#print  ("--------mei zhao dao le --------")
			flag1 = False
			return flag1
	elif method == 'css':
		try:
			driver.find_element_by_css_selector(element)
			#WedDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.CSS_SELECTOR,element))
			return flag1
		except:
			flag1 = False
			return flag1
	elif method == 'xpath':
		try:
			driver.find_element_by_xpath(element)
			#WedDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.XPATH,element))
			return flag1
		except:
			flag1 = False
			return flag1
	elif method == 'class':
		#print('here')
		try:
			#WedDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.CLASS_NAME,element))
			driver.find_element_by_class_name(element)
			#print('走到这了')
			return flag1
		except:
			flag1 = False
			return  flag1
	elif method == 'name':
		try:
			#WedDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.NAME,element))
			driver.find_element_by_name(element)
			return flag1
		except:
			flag1 =False
			return flag1
	elif method == 'tag':
		try:
			#WedDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.TAG_NAME,element))
			driver.find_element_by_tag_name(element)
			return flag1
		except:
			flag1 = False
			return flag1
	elif method == 'link':
		try:
			#WedDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.LINK_TEXT,element))
			driver.find_element_by_link_text(element)
			return flag1
		except:
			flag1 = False
			return flag1
	elif method == 'partical':
		try:
			#WedDriverWait(driver,5,0.5).until(EC.presence_of_element_located(By.PARTICAL_LINK_TEXT,element))
			driver.find_element_by_partical_link_text(element)
			return flag1
		except:
			flag1 = False
			return flag1