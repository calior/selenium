from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
	'''百度搜索测试'''
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.base_url ='http://www.baidu.com'
	def test_baidu_search(self):
		driver = self.driver
		driver.get(self.base_url)
		driver.find_element_by_id('kw').send_keys('HTMLTestRunner')
		driver.find_element_by_id('su').click()

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	testunit = unittest.TestSuite()
	testunit.addTest(Baidu('test_baidu_search'))
	now = time.strftime('%Y-%m-%d %H_%M_%S')
	#定义报告存放路径
	fp = open('./'+now+'result.html','wb')
	#定义测试报告
	runner = HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况：')
	#运行测试用例
	runner.run(testunit)
	#关闭报告文件
	fp.close()