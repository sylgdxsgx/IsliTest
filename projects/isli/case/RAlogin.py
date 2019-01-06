# 此4条代码可以直接运行该脚本调试

import os,sys
base_path = "D:\共享\内部SVN\Test_Au\IsliTest"
# base_path = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"..")	#获取当前文件的前两级目录
sys.path.append(base_path)

from base.unitBase import ParametrizedTestCase as pt
from projects.isli.common import function, variable
from projects.isli.page.loginModular import loginModular
import unittest,time
import logging


flag = True

class RAlogin(pt):
	'''web登入测试'''

	@classmethod
	def setFlag(cls,value):
		global flag
		flag = False
		print('flag=',flag)

	@classmethod
	def setUpClass(cls):
		logging.info('测试模块: %s (%s)'%(cls.__name__,cls.__doc__))
		super().setUpClass()
		cls.t_login = loginModular(cls.driver)
		cls.t_login.open(loginModular.url)  #浏览器打开URL

	def test_01(self):
		'''成功弹窗'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.swit_haead(0)
		#self.t_login.click_action()   #右上角的登入按钮
		#self.assertIs(result,True)   #成功弹窗
		result = self.t_login.login_popup()
		# print(result)
		# if result:
			# self.setFlag(True)
		self.setFlag(result)
		# self.failIf(not result,msg="没有弹窗")   #failIf 条件为真时设为失败 self.fail(msg="") 强制将测试结果设为fail
		
	# @unittest.skipUnless(flag,'')		#条件为假时，跳过
	def test_02(self):
		'''全都不输入'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.swit_haead(0)
		self.t_login.user_login_verify()
		time.sleep(0.5)
		self.assertEqual(self.t_login.error_hint(),'請輸入您的登錄郵箱')
		
	# @unittest.skipUnless(False,'')		#条件为假时，跳过
	def test_03(self):
		'''全都不输入'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.swit_haead(0)
		self.t_login.user_login_verify()
		time.sleep(0.5)
		self.assertEqual(self.t_login.error_hint(),'請輸入您的登錄郵箱')
		
	@unittest.skipIf(True,'tiao')
	def test_04(self):
		'''不输入密码'''
		#t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz@mpreader.com',password='', codecon='8888')
		self.assertEqual(self.t_login.error_hint(),'請輸入密碼')
		
	@unittest.expectedFailure
	def test_05(self):
		'''不输入密码'''
		#t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz@mpreader.com',password='', codecon='8888')
		self.assertEqual(self.t_login.error_hint(),'請輸入密碼')
	"""
	def test_04(self):
		'''不输入验证码'''
		#t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz@mpreader.com', password='aaaaaa',codecon='')
		self.assertEqual(self.t_login.error_hint(), '請輸入驗證碼')

	def test_05(self):
		'''帐号不存在'''
		#t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz', password='aaaaaa', codecon='8888')
		self.assertEqual(self.t_login.error_hint(), '帳號不存在')

	def test_06(self):
		'''密码错误'''
		#t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz@mpreader.com', password='aaaaa', codecon='8888')
		time.sleep(0.25)
		self.assertEqual(self.t_login.error_hint(), '密碼錯誤')

	def test_07(self):
		'''验证码不正确'''
		# t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz@mpreader.com', password='aaaaaa', codecon='888')
		self.assertEqual(self.t_login.error_hint(), '驗證碼錯誤')

	def test_08(self):
		'''输入以前的密码'''
		# t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz@mpreader.com',password='a123456', codecon='8888')
		self.assertEqual(self.t_login.error_hint(),'密碼錯誤')

	def test_09(self):
		'''用已经冻结的账号登入'''
		# t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz@mpreader',password='aaaaaa', codecon='8888')
		self.assertEqual(self.t_login.error_hint(),'帳號不存在')

	def test_10(self):
		'''用审核中的账号登入'''
		# t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz1@mpreader.com',password='aaaaaa', codecon='8888')
		self.assertEqual(self.t_login.error_hint(),'帳號不存在')

	def test_11(self):
		'''验证码输入为空'''
		# t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz1@mpreader.com',password='aaaaaa', codecon='')
		self.assertEqual(self.t_login.error_hint(),'請輸入驗證碼')

	def test_12(self):
		'''SP账户登入成功'''
		# t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz@mpreader.com',password='aaaaaa', codecon='8888')
		time.sleep(0.25)
		time.sleep(3)
		# print(self.t_login.get_hand())
		self.t_login.swit_haead(1)
		self.assertIn('http://172.16.3.53:8080/isli/irms/workbench-provider/base/provider/SPInfo',self.t_login.get_url())
		time.sleep(0.25)
		self.t_login.close()

	def test_13(self):
		'''LC账户登入成功'''
		#t_login = loginModular(self.driver)
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.swit_haead(0)
		self.t_login.click_action()
		time.sleep(0.5)
		self.t_login.user_login_verify(username='liuhongliang_05@163.com',password='admin1', codecon='8888')
		time.sleep(0.25)
		self.t_login.swit_haead(1)
		self.assertEqual('中国ISLI注册中心-出版者业务管理系统',self.t_login.get_LCtitle())
		time.sleep(0.25)
		self.t_login.close()
		self.t_login.swit_haead(0)


	"""



if __name__=="__main__":
	unittest.main()