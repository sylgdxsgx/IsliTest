
# 此4条代码可以直接运行该脚本调试

# import os,sys
# base_path = "D:\共享\内部SVN\Test_Au\IsliTest"	#直接绝对路径赋值
# base_path = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"..")	#获取当前文件的前两级目录
# sys.path.append(base_path)

import time
import logging
from base.unitBase import ParametrizedTestCase as pt
from projects.isli_zh.page.isli_p_loginModular import Module


class isli_p_login(pt):
	'''中国ISLI业务系统登入测试'''

	@classmethod
	def setUpClass(cls):
		'''打开指定网页'''
		# logging.info('测试模块: %s (%s)'%(cls.__name__,cls.__doc__))
		super().setUpClass()
		cls.t_login = Module(cls.driver)
		cls.t_login.open(cls.t_login.base_url)  #浏览器打开URL

	def test_01(self):
		'''全都不输入'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.switch_handle_index(0)
		self.t_login.user_login_verify()
		time.sleep(0.5)
		self.assertEqual(self.t_login.error_username(),'您还没有输入用户名')

	
	def test_02(self):
		'''不输入密码'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='xitest051@163.com',password='', codecon='8888')
		self.assertEqual(self.t_login.error_pwd(),'您还没有输入密码')

	def test_03(self):
		'''不输入验证码'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='xitest051@163.com', password='a123456',codecon='')
		self.assertEqual(self.t_login.error_codecon(), '您还没有输入验证码')

	def test_04(self):
		'''帐号不存在'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='sunsz', password='aaaaaa', codecon='8888')
		self.assertEqual(self.t_login.error_tips(), '账户不存在！')

	def test_05(self):
		'''密码校验错误'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='xitest051@163.com', password='12', codecon='8888')
		time.sleep(1)
		self.assertEqual(self.t_login.error_pwd(), '密码最小为6位')
		
	def test_06(self):
		'''密码错误'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='xitest051@163.com', password='1234567', codecon='8888')
		time.sleep(1)
		self.assertEqual(self.t_login.error_tips(), '密码错误！')

	def test_07(self):
		'''验证码不正确'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='xitest051@163.com', password='a123456', codecon='')
		self.assertEqual(self.t_login.error_tips(), '验证码错误')

	def test_08(self):
		'''输入以前的密码'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='xitest051@163.com',password='islimpr123', codecon='8888')
		self.assertEqual(self.t_login.error_tips(),'密码错误！')

	def test_09(self):
		'''用已经冻结的账号登入'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='xitest053@163.com',password='a123456', codecon='8888')
		self.assertEqual(self.t_login.error_tips(),'账号已冻结！')

	def test_10(self):
		'''用审核中的账号登入'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='test22_17@163.com',password='aaaaaa', codecon='8888')
		self.assertEqual(self.t_login.error_tips(),'账号未审核！')


	def test_11(self):
		'''SP账户登入成功'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_login.user_login_verify(username='xitest051@163.com',password='a123456', codecon='8888')
		time.sleep(2)
		self.assertIn('toMyAccount',self.t_login.get_url())

	




if __name__=="__main__":
	import unittest
	unittest.main()