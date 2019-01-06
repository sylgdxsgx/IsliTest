import unittest,time
from base.unitBase import ParametrizedTestCase as pt
from isli.page.RAMS_homepage import RameHome
import logging

class RAhome(pt):
	'''后台管理首页'''

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.t = RameHome(cls.driver)
		cls.t.login_success('hlliu','admin1')
		if not cls.driver.title == '帐户信息管理':
			cls.driver.quit()
			logging.info('登入失败,取消测试')
		time.sleep(1)
		cls.title = cls.driver.title
		cls.nameinfo ='hlliu'
		cls.jobnoinfo ='930719'
		cls.usnameinfo ='刘红亮'
		cls.telinfo = '86-0755-1234567-1'
		cls.phoneinfo = '86-18513519528'
		cls.emailinfo = 'liuhongliang_05@163.com'

		

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()

	def test_000(self):
		'''登入成功'''
		unittest.skip('登入失败,取消测试')
		
	def test_001(self):
		'''登入信息验证'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		time.sleep(1)
		self.assertIn('根据需要维护您的帐户信息，或修改帐户密码',self.t.get_about(self.t.home_tips_loc))
		self.assertEqual(self.nameinfo,self.t.get_about(self.t.home_name_loc))
		self.assertEqual(self.jobnoinfo,self.t.get_about(self.t.home_jobno_loc))
		self.assertEqual(self.usnameinfo,self.t.get_about(self.t.home_usernma_loc))
		self.assertEqual(self.telinfo,self.t.get_about(self.t.home_tel_loc))
		self.assertEqual(self.phoneinfo,self.t.get_about(self.t.home_phone_loc))
		self.assertEqual(self.emailinfo,self.t.get_about(self.t.home_email_loc))

	def test_002(self):
		'''修改姓名为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.clickaction(self.t.home_alterbutton_loc)
		time.sleep(0.5)
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))
		self.t.clearaction(self.t.alter_name_loc)
		self.t.inputaction(self.t.alter_email_loc,self.emailinfo)
		self.t.clickaction(self.t.alter_button_loc)
		self.assertEqual('姓名不能为空',self.t.get_about(self.t.error_altername_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_003(self):
		'''固话区号为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.clearaction(self.t.alter_tel_2_loc)
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('固定电话不能为空',self.t.get_about(self.t.error_alterTel_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_004(self):
		'''固话区号含特殊字符'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_tel_2_loc,'#$')
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('固定电话格式不正确',self.t.get_about(self.t.error_alterTel_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_005(self):
		'''固话区号一位'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_tel_2_loc,'1')
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('固定电话格式不正确',self.t.get_about(self.t.error_alterTel_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_006(self):
		'''固话号码为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.clearaction(self.t.alter_tel_3_loc)
		self.t.inputaction(self.t.alter_tel_2_loc,'0755')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('固定电话不能为空',self.t.get_about(self.t.error_alterTel_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_007(self):
		'''固话号码小于六位'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_tel_3_loc,'12345')
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('固定电话格式不正确',self.t.get_about(self.t.error_alterTel_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_008(self):
		'''固话号码含有特殊字符'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_tel_3_loc,'#￥%1234')
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('固定电话格式不正确',self.t.get_about(self.t.error_alterTel_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_009(self):
		'''固话分机号含有特殊字符'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_tel_3_loc,'7654321')
		self.t.inputaction(self.t.alter_tel_4_loc,'#￥')
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('固定电话格式不正确',self.t.get_about(self.t.error_alterTel_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_010(self):
		'''手机号为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_tel_4_loc,'2')
		self.t.clearaction(self.t.alter_phone_2_loc)
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('联系电话不能为空',self.t.get_about(self.t.error_alterphone_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_011(self):
		'''手机号含有特殊字符'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_phone_2_loc,'123456$%#')
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('手机号码格式不正确',self.t.get_about(self.t.error_alterphone_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_012(self):
		'''手机号小于6位'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_phone_2_loc,'12345')
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('手机号码格式不正确',self.t.get_about(self.t.error_alterphone_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_013(self):
		'''邮箱为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_phone_2_loc,'13125051020')
		self.t.clearaction(self.t.alter_email_loc)
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('*联系邮箱不能为空',self.t.get_about(self.t.error_alteremail_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_014(self):
		'''邮箱格式错误'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_email_loc,'3133')
		self.t.inputaction(self.t.alter_name_loc,'测试修改数据')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(0.5)
		self.assertEqual('*联系邮箱格式不正确',self.t.get_about(self.t.error_alteremail_loc))
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))

	def test_015(self):
		'''正常修改'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.alter_email_loc,'xiaql111@mpreader.com')
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(1.2)
		self.assertIn('根据需要维护您的帐户信息，或修改帐户密码',self.t.get_about(self.t.home_tips_loc))
		self.assertEqual(self.nameinfo,self.t.get_about(self.t.home_name_loc))
		self.assertEqual(self.jobnoinfo,self.t.get_about(self.t.home_jobno_loc))
		self.assertEqual('测试修改数据',self.t.get_about(self.t.home_usernma_loc))
		self.assertEqual('86-0755-7654321-2',self.t.get_about(self.t.home_tel_loc))
		self.assertEqual('86-13125051020',self.t.get_about(self.t.home_phone_loc))
		self.assertEqual('xiaql111@mpreader.com',self.t.get_about(self.t.home_email_loc))

	def test_016(self):
		'''数据还原'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		# self.t.refresh()
		self.t.clickaction(self.t.home_alterbutton_loc)
		time.sleep(1)
		self.assertIn('根据需要维护您的帐户信息',self.t.get_about(self.t.alter_tips_loc))
		self.t.inputaction(self.t.alter_name_loc,self.usnameinfo)
		self.t.inputaction(self.t.alter_tel_2_loc,'0755')
		self.t.inputaction(self.t.alter_tel_3_loc,'1234567')
		self.t.inputaction(self.t.alter_tel_4_loc,'1')
		self.t.inputaction(self.t.alter_phone_2_loc,'18513519528')
		self.t.inputaction(self.t.alter_email_loc,self.emailinfo)
		self.t.clickaction(self.t.alter_button_loc)
		time.sleep(1)
		self.t.refresh()
		self.assertIn('根据需要维护您的帐户信息，或修改帐户密码',self.t.get_about(self.t.home_tips_loc))
		self.assertEqual(self.nameinfo,self.t.get_about(self.t.home_name_loc))
		self.assertEqual(self.jobnoinfo,self.t.get_about(self.t.home_jobno_loc))
		self.assertEqual(self.usnameinfo,self.t.get_about(self.t.home_usernma_loc))
		self.assertEqual(self.telinfo,self.t.get_about(self.t.home_tel_loc))
		self.assertEqual(self.phoneinfo,self.t.get_about(self.t.home_phone_loc))
		self.assertEqual(self.emailinfo,self.t.get_about(self.t.home_email_loc))

	def test_017(self):
		'''修改密码-原密码为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.refresh()
		self.t.clickaction(self.t.home_alterpw_loc)
		time.sleep(1)
		# self.t.refresh()
		self.assertIn('建议定期修改密码，保护帐户安全',self.t.get_about(self.t.pw_tips_loc))
		self.t.clickaction(self.t.pw_old_loc)
		self.t.inputaction(self.t.pw_old_loc,' ')
		# time.sleep(0.25)
		# self.t.clickaction(self.t.pw_new1_loc)
		self.t.inputaction(self.t.pw_new1_loc,'admin1')
		# self.t.inputaction(self.t.pw_new2_loc,'admin2')
		time.sleep(0.25)
		self.assertIn('请输入原密码',self.t.get_about(self.t.error_pw_old_loc))

	def test_018(self):
		'''原密码小于6位'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_old_loc,'1')
		time.sleep(0.25)
		self.t.inputaction(self.t.pw_new1_loc,'admin1')
		time.sleep(0.25)
		self.assertIn('且长度为 6 ~ 20',self.t.get_about(self.t.error_pw_old_loc))

	def test_019(self):
		'''新密码为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_new1_loc,'  ')
		self.t.inputaction(self.t.pw_old_loc,'admin1')
		self.assertIn('输入新密码',self.t.get_about(self.t.error_pw_new1_loc))

	def test_020(self):
		'''新密码小于6位'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_new1_loc,'123')
		self.t.inputaction(self.t.pw_old_loc,'admin1')
		self.assertIn('且长度为 6 ~ 20',self.t.get_about(self.t.error_pw_new1_loc))

	def test_021(self):
		'''新密码纯数字'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_new1_loc,'123456')
		self.t.inputaction(self.t.pw_old_loc,'admin1')
		self.assertIn('是英文字母、数字或符号组合',self.t.get_about(self.t.error_pw_new1_loc))

	def test_022(self):
		'''新密码纯字母'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_new1_loc,'aaaaaa')
		self.t.inputaction(self.t.pw_old_loc,'admin1')
		self.assertIn('是英文字母、数字或符号组合',self.t.get_about(self.t.error_pw_new1_loc))

	def test_023(self):
		'''确认密码为空'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_new2_loc,'  ')
		self.t.inputaction(self.t.pw_old_loc,'admin1')
		self.assertIn('确认新密码',self.t.get_about(self.t.error_pw_new2_loc))

	def test_024(self):
		'''新密码小于6位'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_new2_loc,'123')
		self.t.inputaction(self.t.pw_old_loc,'admin1')
		self.assertIn('且长度为 6 ~ 20',self.t.get_about(self.t.error_pw_new2_loc))

	def test_025(self):
		'''新密码纯数字'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_new2_loc,'123456')
		self.t.inputaction(self.t.pw_old_loc,'admin1')
		self.assertIn('是英文字母、数字或符号组合',self.t.get_about(self.t.error_pw_new2_loc))

	def test_026(self):
		'''新密码纯字母'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_new2_loc,'aaaaaa')
		self.t.inputaction(self.t.pw_old_loc,'admin1')
		self.assertIn('是英文字母、数字或符号组合',self.t.get_about(self.t.error_pw_new2_loc))

	def test_027(self):
		'''原密码错误'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_old_loc,'admin3')
		self.t.inputaction(self.t.pw_new2_loc,'admin2')
		self.t.inputaction(self.t.pw_new1_loc,'admin2')
		self.t.clickaction(self.t.pw_button_loc)
		time.sleep(0.25)
		self.assertIn('原密码不正确',self.t.get_about(self.t.error_pw_old_loc))

	def test_028(self):
		'''新密码不一致'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_old_loc,'admin1')
		self.t.inputaction(self.t.pw_new2_loc,'admin2')
		self.t.inputaction(self.t.pw_new1_loc,'admin3')
		time.sleep(0.25)
		self.t.clickaction(self.t.pw_button_loc)
		self.assertIn('建议定期修改密码，保护帐户安全',self.t.get_about(self.t.pw_tips_loc))
		# self.assertIn('您两次输入的密码不一致，请重新输入',self.t.get_about(self.t.error_pw_new2_loc))

	def test_029(self):
		'''修改成功'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.inputaction(self.t.pw_old_loc,'admin1')
		self.t.inputaction(self.t.pw_new2_loc,'admin2')
		self.t.inputaction(self.t.pw_new1_loc,'admin2')
		self.t.clickaction(self.t.pw_button_loc)
		time.sleep(1)
		self.assertIn('您的密码修改成功',self.t.get_about(self.t.pw_alerttips_loc))
		self.t.clickaction(self.t.pw_alertbutton_loc)
		time.sleep(0.5)
		# self.t.open(r'https://172.16.3.53:8443/isli/irms/manage-manager/base/login')
		self.t.login_success('hlliu','admin2')
		time.sleep(1)
		self.assertIn('根据需要维护您的帐户信息，或修改帐户密码',self.t.get_about(self.t.home_tips_loc))

	def test_030(self):
		'''密码还原'''
		logging.info('开始执行 %s %s'%(self.id(),self.__dict__['_testMethodDoc']))
		self.t.clickaction(self.t.home_alterpw_loc)
		time.sleep(1)
		self.assertIn('建议定期修改密码，保护帐户安全',self.t.get_about(self.t.pw_tips_loc))
		self.t.inputaction(self.t.pw_old_loc,'admin2')
		self.t.inputaction(self.t.pw_new2_loc,'admin1')
		self.t.inputaction(self.t.pw_new1_loc,'admin1')
		time.sleep(0.25)
		self.t.clickaction(self.t.pw_button_loc)
		time.sleep(1)
		self.assertIn('您的密码修改成功',self.t.get_about(self.t.pw_alerttips_loc))
		self.t.clickaction(self.t.pw_alertbutton_loc)
		time.sleep(0.5)
		self.t.login_success('hlliu','admin1')
		time.sleep(1)
		self.assertIn('根据需要维护您的帐户信息，或修改帐户密码',self.t.get_about(self.t.home_tips_loc))




if __name__=="__main__":
	unittest.main()