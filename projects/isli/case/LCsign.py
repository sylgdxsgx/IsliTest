# import sys
# sys.path.append("..")
from base.unitBase import ParametrizedTestCase as pt
from projects.isli.page.LC_signinpage import Signpage
from projects.isli.common.read_excel import Read
import unittest
import time,os,sys
import logging


class LCsign(pt):
	'''LC 注册'''
	@classmethod
	def setUpClass(cls):
		logging.info('测试模块: %s (%s)'%(cls.__name__,cls.__doc__))
		super().setUpClass()
		file_xpath = r'%s/projects/isli/date/ISLI_RA_signLCdata.xls'%sys.path[0]
		# print(file_xpath)
		cls.data = Read(file_xpath)
		cls.t = Signpage(cls.driver)
		#cls.driver = Signpage()
		cls.t.open(Signpage.sing_url)		#浏览器打开URL
		# time.sleep(1)
	
	def test_001(self):
		'''邮箱格式错误'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eamil(self.data.read_cell(2,1))
		self.t.click_submit()
		self.assertEqual('電子郵件地址不正確',self.t.get_mail_error())
	
	def test_002(self):
		'''邮箱已注册'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eamil(self.data.read_cell(3,1))
		self.t.click_submit()
		self.assertEqual('電子郵件地址已註冊',self.t.get_mail_error())

	def test_003(self):
		'''申请人姓名超过20字符'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_name(self.data.read_cell(4,2))
		self.t.click_submit()
		self.assertIn('姓名最長為20個字',self.t.get_name_error())

	def test_004(self):
		'''验证电话号码输入框一为中文'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.refresh()
		self.t.input_tel_01(self.data.read_cell(5,3))
		time.sleep(0.25)
		self.t.input_tel_02(self.data.read_cell(5,4))
		self.t.input_name('11')
		self.t.click_submit()
		time.sleep(0.5)
		self.assertIn('輸入1~4位數字',self.t.get_tel_error())			#输入框一为中文

	def test_005(self):
		'''验证电话号码输入框一为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_tel_01(self.data.read_cell(6,3))
		self.t.input_tel_02(self.data.read_cell(5,4))
		self.t.input_name('11')
		# self.t.click_submit()
		self.assertIn('請輸入完整的固話',self.t.get_tel_error())			#输入框一为空

	def test_006(self):
		'''验证电话号码输入框二为中文'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_tel_02(self.data.read_cell(7,4))
		self.t.input_tel_01(self.data.read_cell(7,3))
		self.t.input_name('11')
		# self.t.click_submit()
		self.assertIn('請輸入6~11位數字',self.t.get_tel_error())			#输入框二为中文

	def test_007(self):
		'''验证电话号码输入框二为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_tel_02(self.data.read_cell(8,4))
		self.t.input_tel_01(self.data.read_cell(7,3))
		self.t.input_name('11')
		self.t.click_submit()
		self.assertIn('輸入完整的固話',self.t.get_tel_error())			#输入框二为空

	def test_008(self):
		'''验证电话号码输入框二小于6位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_tel_02(self.data.read_cell(9,4))
		time.sleep(0.25)
		self.t.input_tel_01(self.data.read_cell(7,3))
		self.t.input_name('11')
		time.sleep(0.25)
		self.t.click_submit()
		self.assertIn('輸入6~11位數字',self.t.get_tel_error())			#输入框二小于6位

	def test_009(self):
		'''联系电话手机超过11位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_phone_01(self.data.read_cell(10,5))
		self.t.click_submit()
		self.assertIn("流動電話不正確",self.t.get_phone_error())		#联系电话手机超过11位

	def test_010(self):
		'''联系电话手机小于11位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_phone_01(self.data.read_cell(11,5))
		self.t.click_submit()
		self.assertIn("流動電話不正確",self.t.get_phone_error())		#联系电话手机小于11位

	def test_011(self):
		'''联系电话手机非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_phone_01(self.data.read_cell(12,5))
		self.t.click_submit()
		self.assertIn("流動電話不正確",self.t.get_phone_error())		#联系电话手机非数字

	def test_012(self):
		'''选择出版单位省份'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		###后期优化底层封装
		# self.t.click_submit()
		# c = self.t.is_exists(Signpage.province_erroe_loc)   				#未选择省份，提示信息存在
		# self.assertTrue(c)
		self.assertTrue(self.t.is_visibility(Signpage.province_erroe_loc),5)
		self.t.input_province('2')
		# b = self.t.is_exists(Signpage.province_erroe_loc)					#选择省份之后，提示信息不存在
		# self.assertFalse(b)
		self.assertFalse(self.t.is_invisibility(Signpage.province_erroe_loc),5)

	def test_013(self):
		'''选择出版单位归属'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		###后期优化底层封装
		# self.t.click_submit()
		# self.assertTrue(self.t.is_exists(Signpage.group_error_loc))		#未选择出版单位归属，错误信息存在
		self.assertTrue(self.t.is_visibility(Signpage.group_error_loc),5)		#封装后
		self.t.input_affiliation('0')
		self.t.click_submit()
		time.sleep(0.5)
		# self.assertFalse(self.t.is_exists(Signpage.group_error_loc))		#选择独立出版社，错误提示不存在
		self.assertTrue(self.t.is_invisibility(Signpage.group_error_loc),5)		#封装后

	def test_014(self):
		'''选择出版单位归属集团下属'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_affiliation('1')
		self.t.click_submit()
		# self.assertTrue(self.t.is_exists(Signpage.group_select_error_loc))		#选择集团下属出版社，错误信息存在
		self.assertTrue(self.t.is_visibility(Signpage.group_select_error_loc),5)
		self.t.input_group('50000172')
		# self.assertFalse(self.t.is_exists(Signpage.group_select_error_loc))	#选择所属集团，错误信息不存在
		self.assertFalse(self.t.is_invisibility(Signpage.group_select_error_loc),5)

	def test_015(self):
		'''出版单位中文名超过100字符长度'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_publisherCn(self.data.read_cell(14,9))
		self.t.click_submit()
		self.assertIn("出版單位名稱中文",self.t.get_publishCn_error())	#出版社中文名超过100字符长度

	def test_016(self):
		'''出版社英文长度超过500'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_publisherEn(self.data.read_cell(15,10))
		self.t.click_submit()
		self.assertIn("出版單位名稱英文最長為",self.t.get_publishEn_error())

	def test_017(self):
		'''出版单位英文名不为数字或字母'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_publisherEn(self.data.read_cell(16,10))
		self.t.input_name('11')
		# self.t.click_submit()
		self.assertIn("只能輸入英文",self.t.get_publishEn_error())
	
	def test_018(self):
		'''统一社会代码非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.refresh()
		# time.sleep(0.25)
		self.t.input_creditcode(self.data.read_cell(17,11))			#统一社会代码非数字
		self.t.input_bookrange('11111')
		time.sleep(0.25)
		self.t.input_bookrange(1)
		self.t.input_name('11')
		# time.sleep(2)
		self.t.click_submit()
		time.sleep(0.5)
		self.assertIn("請輸入15-18位數字或字母",self.t.get_creditcode_error())

	def test_019(self):
		'''统一社会代码非15或18位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_creditcode(self.data.read_cell(18,11))			#统一社会代码非15或18位
		self.t.input_bookrange(1)
		self.t.input_name('11')
		# self.t.click_submit()
		time.sleep(0.25)
		self.assertIn("請輸入15-18位數字或字母",self.t.get_creditcode_error())
	
	def test_020(self):
		'''出版范围超过200字符长度'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_bookrange(self.data.read_cell(19,12))
		self.t.click_submit()
		self.assertIn("出版範圍最長為200個字",self.t.get_bookrange_error())

	def test_021(self):
		'''通讯地址超过100字符长度'''
		self.t.input_add(self.data.read_cell(20,13))
		self.t.click_submit()
		self.assertIn("通訊地址最長為100個字",self.t.get_add_error())

	def test_022(self):
		'''邮编不为数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_zipcode(self.data.read_cell(21,14))
		self.t.click_submit()
		self.assertIn("郵編不正確",self.t.get_zipcode_error())		#邮编不为数字

	def test_023(self):
		'''邮编小于六位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_zipcode(self.data.read_cell(22,14))
		self.t.click_submit()
		self.assertIn("郵編不正確",self.t.get_zipcode_error())		#邮编小于六位

	def test_024(self):
		'''邮编大于六位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_zipcode(self.data.read_cell(23,14))
		self.t.click_submit()
		self.assertIn("郵編不正確",self.t.get_zipcode_error())		#邮编大于六位

	def test_025(self):
		'''出版单位网址格式错误'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_website(self.data.read_cell(24,15))
		self.t.click_submit()
		self.assertIn("網址不正確",self.t.get_website_error())

	def test_026(self):
		'''主办单位超过100字符长度'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_sponsor(self.data.read_cell(25,16))
		self.t.click_submit()
		self.assertIn("主辦單位最長為100個字",self.t.get_sponsor_error())

	def test_027(self):
		'''主管单位超过100字符长度'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_organ(self.data.read_cell(26,17))
		self.t.click_submit()
		self.assertIn("主管單位最長為100個字",self.t.get_organization_error())

	def test_028(self):
		'''法人代表姓名超过20字符'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lpname(self.data.read_cell(27,18))
		self.t.click_submit()
		self.assertIn("法人代表姓名最長20個字",self.t.get_legalname_error())

	def test_029(self):
		'''法人代表电话输入框一位非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.refresh()
		self.t.input_lptel_1(self.data.read_cell(28,19))
		self.t.click_submit()
		time.sleep(1)
		self.assertIn('請輸入1~4位數字',self.t.get_legaltel_error())			#法人代表电话输入框一位非数字

	def test_030(self):
		'''法人代表电话输入框一位空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lptel_1(self.data.read_cell(29,19))
		self.t.input_lptel_2(self.data.read_cell(28,20))
		self.t.click_submit()
		time.sleep(1)
		self.assertIn('請輸入完整的固話',self.t.get_legaltel_error())		#法人代表电话输入框一位空

	def test_031(self):
		'''法人代表电话输入框二为非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		time.sleep(0.5)
		self.t.input_lptel_1(self.data.read_cell(30,19))
		self.t.input_lptel_2(self.data.read_cell(30,20))
		self.t.click_submit()
		time.sleep(0.25)
		self.assertIn('請輸入6~11位數字',self.t.get_legaltel_error())			#法人代表电话输入框二为非数字

	def test_032(self):
		'''法人代表电话输入框二为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lptel_2(self.data.read_cell(31,20))
		self.t.click_submit()
		# time.sleep(1)
		self.assertIn('請輸入完整的固話',self.t.get_legaltel_error())			#法人代表电话输入框二为空

	def test_033(self):
		'''法人代表电话输入框二小于6位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lptel_2(self.data.read_cell(32,20))
		self.t.input_lpphone('18513519528')
		self.t.click_submit()
		# time.sleep(0.5)
		self.assertIn('請輸入6~11位數字',self.t.get_legaltel_error())				#法人代表输入框二小于6位

	def test_034(self):
		'''法人代表手机非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lpphone(self.data.read_cell(33,21))
		self.t.click_submit()
		self.assertIn('法人代表流動電話不正確',self.t.get_legalphone_error())					#法人代表手机非数字

	def test_035(self):
		'''法人代表手机大于11位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lpphone(self.data.read_cell(34,21))
		self.t.click_submit()
		self.assertIn('法人代表流動電話不正確',self.t.get_legalphone_error())					#法人手机大于11位

	def test_036(self):
		'''法人代表手机小于11位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lpphone(self.data.read_cell(35,21))
		self.t.click_submit()
		self.assertIn('法人代表流動電話不正確',self.t.get_legalphone_error())					#法人手机小于11位

	def test_037(self):
		'''法人代表职务超过20字符'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lppost(self.data.read_cell(36,22))
		self.t.click_submit()
		self.assertIn('法人代表職位最長20個字',self.t.get_legalpost_error())

	def test_038(self):
		'''法人代表传真不为数字	'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lpfax(self.data.read_cell(37,23))
		self.t.click_submit()
		self.assertIn('法人代表傳真不正確',self.t.get_legalfax_error())				#法人代表传真不为数字

	def test_039(self):
		'''法人代表传真不为数字	'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lpfax(self.data.read_cell(38,23))
		self.t.click_submit()
		self.assertIn('法人代表傳真不正確',self.t.get_legalfax_error())				#法人代表传真小于7位

	def test_040(self):
		'''法人代表传真大于13位	'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lpfax(self.data.read_cell(39,23))
		self.t.click_submit()
		self.assertIn('法人代表傳真不正確',self.t.get_legalfax_error())				#法人代表传真大于13位

	def test_041(self):
		'''法人代表邮箱格式不正确'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lpmail(self.data.read_cell(40,24))
		self.t.click_submit()
		self.assertIn('法人代表電郵不正確',self.t.get_legalmail_error())

	def test_042(self):
		'''联系人姓名超过20字符'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contactname(self.data.read_cell(41,25))
		self.t.click_submit()
		self.assertIn("聯絡人姓名最長20個字",self.t.get_contactname_error())

	def test_043(self):
		'''联系人电话输入框一位非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.refresh()
		time.sleep(0.5)
		self.t.input_contact_tel_1(self.data.read_cell(42,26))
		self.t.input_contact_tel_2(self.data.read_cell(42,27))
		self.t.click_submit()
		# time.sleep(1)
		self.assertIn('請輸入1~4位數字',self.t.get_contacttel_error())			#联系人电话输入框一位非数字

	def test_044(self):
		'''联系人电话输入框一位空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contact_tel_1(self.data.read_cell(43,26))
		self.t.input_contact_tel_2(self.data.read_cell(42,27))
		# self.t.click_submit()
		# time.sleep(1)
		self.assertIn('請輸入完整的固話',self.t.get_contacttel_error())		#联系人电话输入框一位空

	def test_045(self):
		'''联系人电话输入框二为非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contact_tel_2(self.data.read_cell(44,27))
		self.t.input_contact_tel_1(self.data.read_cell(44,26))
		# self.t.click_submit()
		# time.sleep(1)
		self.assertIn('請輸入6~11位數字',self.t.get_contacttel_error())			#联系人电话输入框二为非数字

	def test_046(self):
		'''联系人电话输入框二为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contact_tel_2(self.data.read_cell(45,27))
		self.t.input_contact_tel_1(self.data.read_cell(42,27))
		# self.t.click_submit()
		# time.sleep(1)
		self.assertIn('請輸入完整的固話',self.t.get_contacttel_error())			#联系人电话输入框二为空

	def test_047(self):
		'''联系人电话输入框二小于6位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contact_tel_2(self.data.read_cell(46,27))
		self.t.input_contact_tel_1(self.data.read_cell(44,26))
		self.t.click_submit()
		self.assertIn('請輸入6~11位數字',self.t.get_contacttel_error())				#联系人电话输入框二小于6位

	def test_048(self):
		'''联系人手机非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contact_phone(self.data.read_cell(49,28))
		self.t.click_submit()
		self.assertIn('聯絡人流動電話不正確',self.t.get_contactmobile_error())					#法人代表手机非数字

	def test_049(self):
		'''联系人手机大于11位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lpphone(self.data.read_cell(47,28))
		self.t.click_submit()
		self.assertIn('聯絡人流動電話不正確',self.t.get_contactmobile_error())					#法人手机大于11位

	def test_050(self):
		'''联系人手机小于11位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_lpphone(self.data.read_cell(48,28))
		self.t.click_submit()
		self.assertIn('聯絡人流動電話不正確',self.t.get_contactmobile_error())					#法人手机小于11位

	def test_051(self):
		'''联系人职务超过20字符'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contact_post(self.data.read_cell(50,29))
		self.t.click_submit()
		self.assertIn('聯絡人職務最長20個字',self.t.get_contactpost_error())

	def test_052(self):
		'''联系人传真非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contact_fax(self.data.read_cell(51,30))
		self.t.click_submit()
		self.assertIn('聯絡人傳真不正確',self.t.get_contactfax_error())						#联系人传真非数字

	def test_053(self):
		'''联系人传真小于7位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contact_fax(self.data.read_cell(52,30))
		self.t.click_submit()
		self.assertIn('聯絡人傳真不正確',self.t.get_contactfax_error())						#联系人传真小于7位

	def test_054(self):
		'''联系人传真大于13位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contact_fax(self.data.read_cell(53,30))
		self.t.click_submit()
		self.assertIn('聯絡人傳真不正確',self.t.get_contactfax_error())								#联系人传真大于13位

	def test_055(self):
		'''联系人邮箱格式错误'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_contact_mail(self.data.read_cell(54,31))
		self.t.click_submit()
		self.assertIn("聯絡人電郵不正確",self.t.get_contactmail_error())

	def test_056(self):
		'''出版物资质勾选图书'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.refresh()
		self.assertTrue(self.t.is_invisibility(Signpage.bookisbn_1_loc))
		self.t.click_book()
		# time.sleep(2)
		self.assertTrue(self.t.is_visibility(Signpage.bookisbn_1_loc))

	def test_057(self):
		'''出版物资质勾选报纸'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.assertTrue(self.t.is_invisibility(Signpage.newscn_1_loc))
		self.t.click_news()
		self.assertTrue(self.t.is_visibility(Signpage.newscn_1_loc))

	def test_058(self):
		'''出版物资质勾选期刊'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.assertTrue(self.t.is_invisibility(Signpage.issn_1_loc))
		self.t.click_periodical()
		self.assertTrue(self.t.is_visibility(Signpage.issn_1_loc))

	def test_059(self):
		'''出版物资质勾选音像'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.assertTrue(self.t.is_invisibility(Signpage.videoisbn_1_loc))
		self.t.click_video()
		self.assertTrue(self.t.is_visibility(Signpage.videoisbn_1_loc))

	def test_060(self):
		'''出版物资质勾选电子出版物'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.assertTrue(self.t.is_invisibility(Signpage.eleisbn_1_loc))
		self.assertTrue(self.t.is_invisibility(Signpage.elecn_1_loc))
		self.t.click_ele()
		self.assertTrue(self.t.is_visibility(Signpage.eleisbn_1_loc))
		self.assertTrue(self.t.is_visibility(Signpage.elecn_1_loc))

	def test_061(self):
		'''图书isbn输入框一为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.refresh()
		self.t.click_book()
		# self.t.input_bookisbn_1(self.data.read_cell(56,32))
		self.t.input_bookisbn_2(self.data.read_cell(56,33))
		self.t.input_bookisbn_3(self.data.read_cell(56,34))
		self.t.input_contact_tel_1(self.data.read_cell(42,27))
		self.t.input_name('11')
		time.sleep(0.5)
		self.t.click_submit()
		# time.sleep(0.5)
		self.assertIn('請輸入完整的ISBN（圖書）前',self.t.get_bookisbn_error())

	def test_062(self):
		'''图书ISBN输入框二为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_bookisbn_1(self.data.read_cell(57,32))
		self.t.input_bookisbn_2(self.data.read_cell(57,33))
		self.t.input_bookisbn_3(self.data.read_cell(56,34))
		self.t.input_name('11')
		self.t.click_submit()
		self.assertIn('請輸入完整的ISBN（圖書）前',self.t.get_bookisbn_error())

	def test_063(self):
		'''图书ISBN输入框三为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_bookisbn_2(self.data.read_cell(58,33))
		self.t.input_bookisbn_3(self.data.read_cell(58,34))
		self.t.input_bookisbn_1(self.data.read_cell(57,32))
		self.t.input_name('11')
		self.t.click_submit()
		self.assertIn('請輸入完整的ISBN（圖書）前',self.t.get_bookisbn_error())

	def test_064(self):
		'''图书ISBN输入框一不为978/979'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_bookisbn_1(self.data.read_cell(55,32))
		self.t.input_bookisbn_3(self.data.read_cell(55,34))
		self.t.input_name('11')
		self.t.click_submit()
		self.assertIn('輸入框一為978或979',self.t.get_bookisbn_error())

	def test_065(self):
		'''图书ISBN输入框二超过1位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_bookisbn_1(self.data.read_cell(59,32))
		self.t.input_bookisbn_2(self.data.read_cell(59,33))
		# self.t.input_name('11')
		self.t.input_name('11')
		self.t.click_submit()
		self.assertIn('輸入框二為1位的數字',self.t.get_bookisbn_error())

	def test_066(self):
		'''图书ISBN输入框二为非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_bookisbn_2(self.data.read_cell(62,33))
		time.sleep(0.25)
		self.t.click_submit()
		self.assertIn('輸入框二為1位的數字',self.t.get_bookisbn_error())

	def test_067(self):
		'''图书ISBN输入框三小于2位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_bookisbn_2(self.data.read_cell(60,33))
		self.t.input_bookisbn_3(self.data.read_cell(60,34))
		self.t.click_submit()
		self.assertIn('輸入框三最長为5位的數字',self.t.get_bookisbn_error())

	def test_068(self):
		'''图书ISBN输入框三大于7位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_bookisbn_3(self.data.read_cell(61,34))
		self.t.click_submit()
		self.assertIn('輸入框三最長为5位的數字',self.t.get_bookisbn_error())

	def test_069(self):
		'''图书ISBN输入框三非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_bookisbn_3(self.data.read_cell(63,34))
		self.t.click_submit()
		self.assertIn('輸入框三最長为5位的數字',self.t.get_bookisbn_error())

	def test_070(self):
		'''报纸CN第一个输入框为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.refresh()
		self.t.click_news()
		self.t.input_newscn_1(self.data.read_cell(64,35))
		self.t.input_newscn_2(self.data.read_cell(64,36))
		self.t.click_submit()
		self.assertIn('請填寫完整的',self.t.get_newscn_error())

	def test_071(self):
		'''报纸CN第一个输入框小于2位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_newscn_1(self.data.read_cell(66,35))
		self.t.click_submit()
		self.assertIn('輸入框一長度為2位數字',self.t.get_newscn_error())

	def test_072(self):
		'''报纸CN第一个输入框大于2位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_newscn_1(self.data.read_cell(67,35))
		self.t.click_submit()
		self.assertIn('輸入框一長度為2位數字',self.t.get_newscn_error())

	def test_073(self):
		'''报纸CN第一个输入框非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_newscn_1(self.data.read_cell(68,35))
		self.t.click_submit()
		self.assertIn('輸入框一長度為2位數字',self.t.get_newscn_error())

	def test_074(self):
		'''报纸CN第二个输入框为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_newscn_1(self.data.read_cell(65,35))
		self.t.input_newscn_2(self.data.read_cell(65,36))
		self.t.click_submit()
		self.assertIn('請填寫完整的（CN）',self.t.get_newscn_error())

	def test_075(self):
		''''期刊ISSN输入框一为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.refresh()
		time.sleep(0.25)
		self.t.click_periodical()
		self.t.input_issn_1(self.data.read_cell(69,37))
		self.t.input_issn_2(self.data.read_cell(69,38))
		self.t.click_submit()
		self.assertIn('請填寫完整的（ISSN',self.t.get_issn_error())

	def test_076(self):
		''''期刊ISSN输入框二为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_issn_1(self.data.read_cell(70,37))
		self.t.input_issn_2(self.data.read_cell(70,38))
		self.t.click_submit()
		self.assertIn('請填寫完整的（ISSN',self.t.get_issn_error())

	def test_077(self):
		'''音像isbn输入框一为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.refresh()
		time.sleep(0.25)
		self.t.click_video()
		# self.t.input_videoisbn_1(self.data.read_cell(79,42))
		self.t.input_videoisbn_2(self.data.read_cell(79,43))
		self.t.input_videoisbn_3(self.data.read_cell(79,44))
		self.t.click_submit()
		self.assertIn('請輸入完整的ISBN（音像）前',self.t.get_videoisbn_error())

	def test_078(self):
		'''音像ISBN输入框二为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_videoisbn_2(self.data.read_cell(80,43))
		self.t.input_videoisbn_1(self.data.read_cell(80,42))
		self.t.click_submit()
		self.assertIn('請輸入完整的ISBN（音像）前',self.t.get_videoisbn_error())

	def test_079(self):
		'''音像ISBN输入框三为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_videoisbn_3(self.data.read_cell(81,44))
		self.t.input_videoisbn_2(self.data.read_cell(81,43))
		self.t.click_submit()
		self.assertIn('請輸入完整的ISBN（音像）前',self.t.get_videoisbn_error())

	def test_080(self):
		'''音像ISBN输入框一不为978/979'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_videoisbn_1(self.data.read_cell(55,32))
		self.t.input_videoisbn_3(self.data.read_cell(82,44))
		self.t.click_submit()
		self.assertIn('輸入框一為978或979',self.t.get_videoisbn_error())

	def test_081(self):
		'''音像ISBN输入框二超过1位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_videoisbn_2(self.data.read_cell(82,43))
		self.t.input_videoisbn_1(self.data.read_cell(82,42))
		self.t.click_submit()
		self.assertIn('輸入框二為1位的數字',self.t.get_videoisbn_error())

	def test_082(self):
		'''音像ISBN输入框二为非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_videoisbn_2(self.data.read_cell(85,43))
		self.t.input_videoisbn_1(self.data.read_cell(82,42))
		self.t.click_submit()
		self.assertIn('輸入框二為1位的數字',self.t.get_videoisbn_error())

	def test_083(self):
		'''音像ISBN输入框三小于2位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_videoisbn_2(self.data.read_cell(83,43))
		self.t.input_videoisbn_3(self.data.read_cell(83,44))
		self.t.input_videoisbn_1(self.data.read_cell(82,42))
		self.t.click_submit()
		self.assertIn('入框三最長为5位的數字',self.t.get_videoisbn_error())

	def test_084(self):
		'''音像ISBN输入框三大于7位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_videoisbn_3(self.data.read_cell(84,44))
		self.t.input_videoisbn_1(self.data.read_cell(82,42))
		self.t.click_submit()
		self.assertIn('輸入框三最長为5位的數字',self.t.get_videoisbn_error())

	def test_085(self):
		'''音像ISBN输入框三非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_videoisbn_3(self.data.read_cell(86,44))
		self.t.input_videoisbn_1(self.data.read_cell(82,42))
		self.t.click_submit()
		self.assertIn('輸入框三最長为5位的數字',self.t.get_videoisbn_error())

	def test_086(self):
		'''电子出版物CN第一个输入框为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.refresh()
		time.sleep(0.25)
		self.t.click_ele()
		self.t.input_elecn_1(self.data.read_cell(87,45))
		self.t.input_elecn_2(self.data.read_cell(87,46))
		self.t.click_submit()
		self.assertIn('請填寫完整的（CN',self.t.get_eleicn_error())

	def test_087(self):
		'''电子出版物CN第一个输入框小于2位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_elecn_1(self.data.read_cell(89,45))
		self.t.click_submit()
		self.assertIn('輸入框一長度為2位數字',self.t.get_eleicn_error())

	def test_088(self):
		'''电子出版物CN第一个输入框大于2位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_elecn_1(self.data.read_cell(90,45))
		self.t.click_submit()
		self.assertIn('輸入框一長度為2位數字',self.t.get_eleicn_error())

	def test_089(self):
		'''电子出版物CN第一个输入框非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_elecn_1(self.data.read_cell(91,45))
		self.t.click_submit()
		self.assertIn('輸入框一長度為2位數字',self.t.get_eleicn_error())

	def test_090(self):
		'''电子出版物CN第二个输入框为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_elecn_1(self.data.read_cell(88,45))
		self.t.input_elecn_2(self.data.read_cell(88,46))
		self.t.click_submit()
		self.assertIn('請填寫完整的（CN',self.t.get_eleicn_error())

	def test_091(self):
		'''电子出版物isbn输入框一为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eleisbn_1(self.data.read_cell(79,42))
		self.t.input_eleisbn_2(self.data.read_cell(79,43))
		self.t.input_eleisbn_3(self.data.read_cell(79,44))
		self.t.click_submit()
		self.assertIn('輸入完整的ISBN（電子）前綴',self.t.get_eleisbn_error())

	def test_092(self):
		'''电子出版物ISBN输入框二为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eleisbn_1(self.data.read_cell(80,42))
		self.t.input_eleisbn_2(self.data.read_cell(80,43))
		self.t.click_submit()
		self.assertIn('輸入完整的ISBN（電子）前綴',self.t.get_eleisbn_error())

	def test_093(self):
		'''电子出版物ISBN输入框三为空'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eleisbn_2(self.data.read_cell(81,43))
		self.t.input_eleisbn_3(self.data.read_cell(81,44))
		self.t.click_submit()
		self.assertIn('輸入完整的ISBN（電子）前綴',self.t.get_eleisbn_error())

	def test_093(self):
		'''电子出版物ISBN输入框一不为978/979'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eleisbn_1(self.data.read_cell(55,32))
		self.t.input_eleisbn_3(self.data.read_cell(82,44))
		self.t.click_submit()
		self.assertIn('輸入框一為978或97',self.t.get_eleisbn_error())

	def test_095(self):
		'''电子出版物ISBN输入框二超过1位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eleisbn_1(self.data.read_cell(82,42))
		self.t.input_eleisbn_2(self.data.read_cell(82,43))
		self.t.click_submit()
		self.assertIn('輸入框二為1位的數字',self.t.get_eleisbn_error())

	def test_096(self):
		'''电子出版物ISBN输入框二为非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eleisbn_2(self.data.read_cell(85,43))
		self.t.click_submit()
		self.assertIn('輸入框二為1位的數字',self.t.get_eleisbn_error())

	def test_097(self):
		'''电子出版物ISBN输入框三小于2位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eleisbn_2(self.data.read_cell(83,43))
		self.t.input_eleisbn_3(self.data.read_cell(83,44))
		self.t.click_submit()
		time.sleep(0.25)
		self.assertIn('輸入框三最長为5位的數字',self.t.get_eleisbn_error())

	def test_098(self):
		'''电子出版物ISBN输入框三大于7位'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eleisbn_3(self.data.read_cell(84,44))
		self.t.input_eleisbn_2(self.data.read_cell(81,43))
		self.t.click_submit()
		self.assertIn('輸入框三最長为5位的數字',self.t.get_eleisbn_error())

	def test_099(self):
		'''电子出版物ISBN输入框三非数字'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eleisbn_3(self.data.read_cell(86,44))
		self.t.input_eleisbn_2(self.data.read_cell(81,43))
		self.t.click_submit()
		self.assertIn('輸入框三最長为5位的數字',self.t.get_eleisbn_error())

	def test_100(self):
		'''返回上一步：注册协议界面'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.click_back()
		text = self.t.get_text(('css selector','.btnBackh'))
		self.assertEqual('稍後再說',text)

	def test_101(self):
		'''协议页面跳转至信息填写页面'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.click(('css selector','.regBtnOk'))
		self.assertEqual('申請人信息',self.t.get_text(('css selector','.regisBox>h3:nth-child(1)')))

	def test_102(self):
		'''单个必填项错误进行提交'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		time.sleep(1)
		self.t.input_eamil(self.data.read_cell(92,1))
		self.t.input_name(self.data.read_cell(92,2))
		self.t.input_phone_01(self.data.read_cell(92,5))
		self.t.input_province(self.data.read_cell(92,6))
		self.t.input_affiliation(self.data.read_cell(92,7))
		self.t.input_publisherCn(self.data.read_cell(92,9))
		self.t.input_publisherEn(self.data.read_cell(92,10))
		self.t.input_creditcode(self.data.read_cell(92,11))
		self.t.input_add(self.data.read_cell(92,13))
		self.t.input_zipcode(self.data.read_cell(92,14))
		self.t.input_sponsor(self.data.read_cell(92,16))
		self.t.input_organ(self.data.read_cell(92,17))
		self.t.input_lpname(self.data.read_cell(92,18))
		self.t.input_contactname(self.data.read_cell(92,25))
		self.t.input_contact_tel_1(self.data.read_cell(92,26))
		self.t.input_contact_tel_2(self.data.read_cell(92,27))
		self.t.input_contact_phone(self.data.read_cell(92,28))
		self.t.input_contact_mail(self.data.read_cell(92,31))
		self.t.click_book()
		self.t.click_submit()
		self.assertEqual('電子郵件地址不正確',self.t.get_mail_error())
	
	@unittest.skip('取消该用例')
	def test_104(self):
		'''所有必填项输入正确'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		time.sleep(1)
		self.t.input_eamil(self.data.read_cell(93,1))
		self.t.input_name(self.data.read_cell(93,2))
		self.t.input_phone_01(self.data.read_cell(93,5))
		self.t.input_province(self.data.read_cell(93,6))
		self.t.input_affiliation(self.data.read_cell(93,7))
		self.t.input_publisherCn(self.data.read_cell(93,9))
		self.t.input_publisherEn(self.data.read_cell(93,10))
		self.t.input_creditcode(self.data.read_cell(93,11))
		self.t.input_add(self.data.read_cell(93,13))
		self.t.input_zipcode(self.data.read_cell(93,14))
		self.t.input_sponsor(self.data.read_cell(93,16))
		self.t.input_organ(self.data.read_cell(93,17))
		self.t.input_lpname(self.data.read_cell(93,18))
		self.t.input_contactname(self.data.read_cell(93,25))
		self.t.input_contact_tel_1(self.data.read_cell(93,26))
		self.t.input_contact_tel_2(self.data.read_cell(93,27))
		self.t.input_contact_phone(self.data.read_cell(93,28))
		self.t.input_contact_mail(self.data.read_cell(93,31))
		self.t.click_book()
		self.t.click_submit()
		time.sleep(0.5)
		self.assertEqual("ISLI關聯標識符登記者（出版機構）注冊表",self.t.get_text(('css selector','.priH3')))

	def test_103(self):
		'''非必填项输入错误    --电话号码错误'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		time.sleep(0.25)
		# self.t.click(('css selector','.btnBackh'))
		# time.sleep(0.25)
		self.t.input_tel_01(self.data.read_cell(94,3))
		self.t.input_tel_02(self.data.read_cell(94,4))
		self.t.click_submit()
		self.assertEqual('請輸入6~11位數字',self.t.get_tel_error())

	def test_105(self):
		'''所有输入框正常输入注册'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.input_eamil(self.data.read_cell(95,1))
		self.t.input_name(self.data.read_cell(95,2))
		self.t.input_phone_01(self.data.read_cell(95,5))
		self.t.input_province(self.data.read_cell(95,6))
		self.t.input_affiliation(self.data.read_cell(95,7))
		self.t.input_publisherCn(self.data.read_cell(95,9))
		self.t.input_publisherEn(self.data.read_cell(95,10))
		self.t.input_creditcode(self.data.read_cell(95,11))
		self.t.input_add(self.data.read_cell(95,13))
		self.t.input_zipcode(self.data.read_cell(95,14))
		self.t.input_sponsor(self.data.read_cell(95,16))
		self.t.input_organ(self.data.read_cell(95,17))
		self.t.input_lpname(self.data.read_cell(95,18))
		self.t.input_contactname(self.data.read_cell(95,25))
		self.t.input_contact_tel_1(self.data.read_cell(95,26))
		self.t.input_contact_tel_2(self.data.read_cell(95,27))
		self.t.input_contact_phone(self.data.read_cell(95,28))
		self.t.input_contact_mail(self.data.read_cell(95,31))
		self.t.input_tel_02(self.data.read_cell(95,4))
		self.t.input_affiliation(self.data.read_cell(95,7))
		self.t.input_group(str(self.data.read_cell(95,8)))
		self.t.input_bookrange(self.data.read_cell(95,12))
		self.t.input_website(self.data.read_cell(95,15))
		self.t.input_lptel_1(self.data.read_cell(95,19))
		self.t.input_lptel_2(self.data.read_cell(95,20))
		self.t.input_lpphone(self.data.read_cell(95,21))
		self.t.input_lppost(self.data.read_cell(95,22))
		self.t.input_lpfax(self.data.read_cell(95,23))
		self.t.input_lpmail(self.data.read_cell(95,24))
		self.t.input_contact_post(self.data.read_cell(95,29))
		self.t.input_contact_fax(self.data.read_cell(95,30))
		self.t.click_book()
		self.t.click_news()
		self.t.click_video()
		self.t.click_ele()
		self.t.click_periodical()
		self.t.click_internet()
		self.t.click_submit()
		self.assertEqual("ISLI關聯標識符登記者（出版機構）注冊表",self.t.get_text(('css selector','.priH3')))
	
	def test_106(self):
		'''管理后台验证注册成功'''
		logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t.open(r'https://172.16.5.162:8443/mpr/mcrs-system/mvc/syslogin/login')
		self.t.inputaction(('id','userName'),'xuxuerlai')
		self.t.inputaction(('id','passWord'),'123456')
		self.t.inputaction(('id','codeCon'),'1234')
		self.t.click(('id','login'))
		time.sleep(2)
		self.t.click(('css selector','[title="出版者管理"]'))
		time.sleep(0.5)
		self.t.switch_iframe(('id','j_menu'))
		self.t.click(('css selector','.left-nav>[title="出版者申请管理"]'))
		self.t.switch_iframe2default()
		time.sleep(0.5)
		self.t.switch_iframe(('id','j_main'))
		time.sleep(0.5)
		self.assertEqual(self.data.read_cell(95,9),self.t.get_text(('css selector','tbody>tr:first-child>[name="publisherCn"]>span')))
	
	@classmethod
	def tearDownClass(cls):
		cls.driver.close()

if __name__=="__main__":
	unittest.main()
	# print(os.path.abspath('..\data\\')+'\ISLI_RA_signLCdata.xls')