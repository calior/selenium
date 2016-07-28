# coding: UTF-8
from selenium import webdriver
import time
#from get_Screen import isElementExist
from for_test import while_lianxi_no

driver = webdriver.Chrome()
driver.get("http://test-new.classba.com.cn/index.php/index/index/token/ecyxJp1hapWQiOjEyMzIsInRvcGljX2lkIjoxMSwidW5hbWUiOiJ4aWFvbGFuMTIzMiIsInZlcmlmeSI6Im5hbmppbmcxMiJ9")
while_lianxi_no(driver)