
# 此3条代码可以直接运行该脚本调试
import os,sys
base_path = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"..")	#前两级目录。详细用法见function中的get_dir函数
sys.path.append(base_path)

import time
import logging,unittest
from base.unitBase import ParametrizedTestCase as pt
from base.function import function_log,conf_read,conf_write,SkipIf_Fail,SkipIf_NotPass,SkipIf_PrevNotPass
from projects.isli_zh.page.isli_p_loginModular import Module

class isli_m_operate(pt):
	'''中国ISLI业务系统登入测试'''
	'''每个testcase就是一个个TestCase类的实例对象。每个testcase就是由TestCase实例化的一个独立的实例。那是不是就是每个TestCase不能共享数据呢？答案是否定的，不能共享的原因是我们上面用到的是self（实例对象属性），能共享我们就必须使用类属性（如建立类属性：isli_m_operate.flag）'''
    
	# global flag
	# flag=True
    
	# def __init__(self):
		# super().__init__()
		# conf_write()   #初始化TestFlag
        
	@classmethod
	def setUpClass(cls):
		'''打开指定网页'''
		super().setUpClass()
		conf_write()   #初始化TestFlag
		cls.t_login = Module(cls.driver)
		cls.t_login.open(cls.t_login.base_url)  #浏览器打开URL
        
		
	def test_01(self):
		'''全都不输入'''
		self.t_login.switch_handle_index(0)
		self.t_login.user_login_verify()
		time.sleep(0.5)
		self.assertEqual(self.t_login.error_username(),'您还没有输入用户名1')
        
	@SkipIf_Fail('test_01')
	def test_02(self):
		'''不输入密码'''
		conf_write(self._testMethodName)    #把用例设置为Fail
		self.t_login.user_login_verify(username='xitest051@163.com',password='', codecon='8888')
		self.assertEqual(self.t_login.error_pwd(),'您还没有输入密码')
        
	@SkipIf_PrevNotPass()
	def test_03(self):
		'''不输入验证码'''
		self.t_login.user_login_verify(username='xitest051@163.com', password='a123456',codecon='')
		self.assertEqual(self.t_login.error_codecon(), '您还没有输入验证码')

	@SkipIf_PrevNotPass()
	def test_04(self):
		'''帐号不存在'''
		self.t_login.user_login_verify(username='sunsz', password='aaaaaa', codecon='8888')
		self.assertEqual(self.t_login.error_tips(), '账户不存在！1')
            


	def test_05(self):
		'''密码校验错误'''
		self.t_login.user_login_verify(username='xitest051@163.com', password='12', codecon='8888')
		time.sleep(1)
		self.assertEqual(self.t_login.error_pwd(), '密码最小为6位')
		
	@SkipIf_NotPass('test_04')
	def test_06(self):
		'''密码错误'''
		self.t_login.user_login_verify(username='xitest051@163.com', password='1234567', codecon='8888')
		time.sleep(1)
		self.assertEqual(self.t_login.error_tips(), '密码错误！')
	"""	
	@unittest.SkipIf_TestCaseFail('test_05')
	def test_07(self):
		'''验证码不正确'''
		self.t_login.user_login_verify(username='xitest051@163.com', password='a123456', codecon='')
		self.assertEqual(self.t_login.error_tips(), '验证码错误')

	def test_08(self):
		'''输入以前的密码'''
		self.t_login.user_login_verify(username='xitest051@163.com',password='islimpr123', codecon='8888')
		self.assertEqual(self.t_login.error_tips(),'密码错误！')

	def test_09(self):
		'''用已经冻结的账号登入'''
		self.t_login.user_login_verify(username='xitest053@163.com',password='a123456', codecon='8888')
		self.assertEqual(self.t_login.error_tips(),'账号已冻结！')

	def test_10(self):
		'''用审核中的账号登入'''
		self.t_login.user_login_verify(username='test22_17@163.com',password='aaaaaa', codecon='8888')
		self.assertEqual(self.t_login.error_tips(),'账号未审核！')


	def test_11(self):
		'''SP账户登入成功'''
		self.t_login.user_login_verify(username='xitest051@163.com',password='a123456', codecon='8888')
		time.sleep(2)
		self.assertIn('toMyAccount',self.t_login.get_url())
	"""
	




if __name__=="__main__":
	import unittest
	unittest.main()