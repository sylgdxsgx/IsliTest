import sys
# sys.path.append("..")
from base.unitBase import ParametrizedTestCase as pt
from projects.isli.page.RAMS_loginpage import Login_RA_MS
import unittest,time
import logging

class RAMS_login(pt):
	'''RA后台登陆'''
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.t = Login_RA_MS(cls.driver)
		cls.t.open(Login_RA_MS.Ra_MS_url)	#在浏览器打开该URL并最大化窗口
		cls.t.select_language()				#选择一种语言

	def test_01(self):
		'''用户名为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.input_passwd("aaaaaa")
		self.t.input_code('8888')
		self.t.click_submit()
		self.assertEqual('请输入您的用户名',self.t.get_error())

	def test_02(self):
		'''用户名不存在'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.input_usname('www')
		self.t.click_submit()
		self.assertEqual('帐号不存在',self.t.get_error())

	def test_03(self):
		'''账号已停用'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.input_usname('shigx2')
		self.t.input_passwd('a123456')
		self.t.input_code('8888')
		self.t.click_submit()
		self.assertEqual('您的帐户已被禁用，请联系ISLI注册机构。',self.t.get_error())
		
	def test_04(self):
		'''密码为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.input_usname('shigx1')
		self.t.input_passwd('')
		self.t.input_code('8888')
		self.t.click_submit()
		self.assertEqual('请输入密码',self.t.get_error())

	def test_05(self):
		'''密码错误'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.input_usname('isli')
		self.t.input_passwd('qqqqqq')
		self.t.input_code('8888')
		self.t.click_submit()
		self.assertEqual('密码错误',self.t.get_error())

	def test_06(self):
		'''验证码为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.input_passwd('qqqqqq')
		self.t.click_submit()
		self.assertEqual('请输入4位验证码',self.t.get_error())

	def test_07(self):
		'''登入成功'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.input_passwd('aaaaaa')
		self.t.input_code('8888')
		self.t.click_submit()
		self.assertIn('或修改帐户密码',self.t.get_text(('css selector','.warnTip')))


if __name__=="__main__":
	unittest.main()