from base.unitBase import ParametrizedTestCase as pt
from isli.page.RA_SPManagePage import SPmanage
from isli.common.read_excel import Read
from isli import run_all
import unittest,time,os

class RASPmanage(pt):
	'''RA 后台管理sp账户管理'''

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.file_path = os.path.join(run_all.fppath,'date')
		cls.data = Read(cls.file_path+r'/ISLI_RA_MS.xls')
		cls.t = SPmanage(cls.driver)
		cls.t.login_success()
		# cls.driver.clickaction(cls.driver.sp_manageTop_loc)
		# cls.driver.clickaction(cls.driver.sp_manageleft_loc)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()

	def test_001(self):
		'''sp账户管理界面'''
		self.t.clickaction(self.t.sp_manageTop_loc)
		self.t.clickaction(self.t.sp_manageleft_loc)
		time.sleep(0.5)
		# self.assertEqual("SP帐户管理",self.t.get_about(self.t.sp_managetitle_loc))
		self.assertEqual("导出 Excel",self.t.get_about(self.t.sp_manage2excel_loc))

	def test_002(self):
		'''用户名搜索正常'''
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_managename_loc))

	def test_003(self):
		'''用户性质机构搜索正常'''
		self.t.clearaction(self.t.search_managename_loc)
		self.t.selecttext(self.t.search_managekind_loc,"机构")
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('机构',self.t.get_about(self.t.table_managekind_loc))

	def test_004(self):
		'''用户性质个人搜索成功'''
		self.t.selecttext(self.t.search_managekind_loc,"个人")
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('个人',self.t.get_about(self.t.table_managekind_loc))

	def test_005(self):
		'''状态正常搜索成功'''
		self.t.selecttext(self.t.search_managekind_loc,"- 全部 -")
		time.sleep(0.25)
		self.t.selecttext(self.t.search_managestatus_loc,'正常')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('正常',self.t.get_about(self.t.table_managestatus_loc))

	def test_006(self):
		'''状态冻结搜索成功'''
		self.t.selecttext(self.t.search_managestatus_loc,'冻结')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('冻结',self.t.get_about(self.t.table_managestatus_loc))

	def test_007(self):
		'''状态禁用搜索成功'''
		self.t.selecttext(self.t.search_managestatus_loc,'禁用')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('禁用',self.t.get_about(self.t.table_managestatus_loc))

	def test_008(self):
		'''查看操作成功'''
		self.t.selecttext(self.t.search_managestatus_loc,'- 全部 -')
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.t.clickaction(self.t.table_manageview_loc)
		time.sleep(0.5)
		self.assertEqual(self.data.read_cell(1,1),self.t.get_about(self.t.view_managename_loc))
		self.assertEqual("机构",self.t.get_about(self.t.view_managekind_loc))
		self.assertEqual(self.data.read_cell(1,4),self.t.get_about(self.t.view_manageorgname_loc))
		self.assertEqual(self.data.read_cell(1,5),self.t.get_about(self.t.view_manageorgadd_loc))
		self.assertEqual(self.data.read_cell(1,6),self.t.get_about(self.t.view_manageorgid_loc))
		self.assertEqual(self.data.read_cell(1,7),self.t.get_about(self.t.view_managewitsite_loc))
		self.assertEqual(self.data.read_cell(1,8),self.t.get_about(self.t.view_managelinkname_loc))
		self.assertEqual(self.data.read_cell(1,9),self.t.get_about(self.t.view_manageTel_loc))
		self.assertEqual(self.data.read_cell(1,13),self.t.get_about(self.t.view_managephone_loc))
		self.assertEqual(self.data.read_cell(1,15),self.t.get_about(self.t.view_manageps_loc))
		self.assertEqual(self.data.read_cell(1,16),self.t.get_about(self.t.view_managemail_loc))
		self.assertEqual(self.data.read_cell(1,17),self.t.get_about(self.t.view_manageadd_loc))
		self.assertEqual(self.data.read_cell(1,18),self.t.get_about(self.t.view_managezip_loc))

	def test_009(self):
		'''机构名称为空'''
		self.t.clickaction(self.t.view_managesubmit_loc)
		time.sleep(0.5)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))
		self.assertEqual(self.data.read_cell(1,1),self.t.get_about(self.t.alter_managename_loc))
		self.t.clearaction(self.t.alter_manageorgname_loc)
		self.t.inputaction(self.t.alter_manageaddress_loc,'深圳')
		time.sleep(0.25)
		self.assertIn('输入机构名称',self.t.get_about(self.t.error_altermanagename_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_010(self):
		'''机构名称已存在'''
		self.t.inputaction(self.t.alter_manageorgname_loc,self.data.read_cell(3,4))
		self.t.inputaction(self.t.alter_manageaddress_loc,'深圳')
		self.assertIn('机构名称已存在',self.t.get_about(self.t.error_altermanagename_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_011(self):
		'''注册地址为空'''
		self.t.clearaction(self.t.alter_manageaddress_loc)
		self.t.inputaction(self.t.alter_manageorgname_loc,self.data.read_cell(4,4))
		time.sleep(0.25)
		self.assertIn('输入注册地址',self.t.get_about(self.t.error_altermanageaddress_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_012(self):
		'''社会代码14位'''
		self.t.inputaction(self.t.alter_manageorgid_loc,self.data.read_cell(5,6))
		self.t.inputaction(self.t.alter_manageaddress_loc,self.data.read_cell(5,5))
		time.sleep(0.25)
		self.assertIn('输入15~18位数字和字母',self.t.get_about(self.t.error_altermanageorgid_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_013(self):
		'''社会代码非数字字母'''
		self.t.inputaction(self.t.alter_manageorgid_loc,self.data.read_cell(6,6))
		self.t.inputaction(self.t.alter_manageaddress_loc,self.data.read_cell(5,5))
		time.sleep(0.25)
		self.assertIn('输入15~18位数字和字母',self.t.get_about(self.t.error_altermanageorgid_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_014(self):
		'''联系姓名为空'''
		self.t.clearaction(self.t.alter_managelinkname_loc)
		self.t.inputaction(self.t.alter_manageorgid_loc,self.data.read_cell(7,6))
		self.assertIn('输入联系人',self.t.get_about(self.t.error_alterlinkname_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_015(self):
		'''固话区号错误'''
		self.t.inputaction(self.t.alter_manageTel1_loc,self.data.read_cell(8,10))
		self.t.inputaction(self.t.alter_manageorgid_loc,self.data.read_cell(7,6))
		self.assertIn('电话格式不正确',self.t.get_about(self.t.error_altermanageTel_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_016(self):
		'''固话区号为空'''
		self.t.inputaction(self.t.alter_managelinkname_loc,'测试')
		self.t.clearaction(self.t.alter_manageTel1_loc)
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))
		self.assertIn('电话格式不正确',self.t.get_about(self.t.error_altermanageTel_loc))

	def test_017(self):
		'''固话小于6位'''
		self.t.inputaction(self.t.alter_manageTel1_loc,self.data.read_cell(10,10))
		self.t.inputaction(self.t.alter_manageTel2_loc,self.data.read_cell(10,11))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))
		self.assertIn('电话格式不正确',self.t.get_about(self.t.error_altermanageTel_loc))

	def test_018(self):
		'''固话含有非数字'''
		# self.t.inputaction(self.t.alter_manageTel1_loc,self.data.read_cell(10,10))
		self.t.inputaction(self.t.alter_manageTel2_loc,self.data.read_cell(11,11))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))
		self.assertIn('电话格式不正确',self.t.get_about(self.t.error_altermanageTel_loc))

	def test_019(self):
		'''固话号码为空'''
		self.t.clearaction(self.t.alter_manageTel2_loc)
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))
		self.assertIn('电话格式不正确',self.t.get_about(self.t.error_altermanageTel_loc))

	def test_020(self):
		'''分机号含有特殊字符'''
		self.t.inputaction(self.t.alter_manageTel2_loc,self.data.read_cell(13,11))
		self.t.inputaction(self.t.alter_manageTel3_loc,self.data.read_cell(13,12))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))
		self.assertIn('电话格式不正确',self.t.get_about(self.t.error_altermanageTel_loc))

	def test_021(self):
		'''手机号为空'''
		self.t.clearaction(self.t.alter_managephone_loc)
		self.t.inputaction(self.t.alter_manageTel3_loc,self.data.read_cell(14,12))
		self.assertIn('输入联系人电话（手机）',self.t.get_about(self.t.error_altermanagephone_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_022(self):
		'''手机号小于6位'''
		self.t.inputaction(self.t.alter_managephone_loc,self.data.read_cell(15,14))
		self.t.inputaction(self.t.alter_manageTel3_loc,self.data.read_cell(14,12))
		self.assertIn('手机号码格式不对',self.t.get_about(self.t.error_altermanagephone_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_023(self):
		'''手机号含有非数字'''
		self.t.inputaction(self.t.alter_managephone_loc,self.data.read_cell(16,14))
		self.t.inputaction(self.t.alter_manageTel3_loc,self.data.read_cell(14,12))
		self.assertIn('手机号码格式不对',self.t.get_about(self.t.error_altermanagephone_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_024(self):
		'''电子邮箱为空'''
		self.t.clearaction(self.t.alter_manageemail_loc)
		self.t.inputaction(self.t.alter_managephone_loc,self.data.read_cell(17,14))
		self.assertIn('请输入电子邮箱',self.t.get_about(self.t.error_altermanagemail_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_025(self):
		'''邮箱格式错误'''
		self.t.inputaction(self.t.alter_manageemail_loc,self.data.read_cell(18,16))
		self.t.inputaction(self.t.alter_managephone_loc,self.data.read_cell(17,14))
		self.assertIn('输入正确的邮箱',self.t.get_about(self.t.error_altermanagemail_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_026(self):
		'''通讯地址为空'''
		self.t.clearaction(self.t.alter_managelinkadd_loc)
		self.t.inputaction(self.t.alter_manageemail_loc,self.data.read_cell(19,16))
		self.assertIn('输入通讯地址',self.t.get_about(self.t.error_altermanageadd_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_027(self):
		'''邮编格式错误'''
		self.t.inputaction(self.t.alter_managezip_loc,self.data.read_cell(20,18))
		self.t.inputaction(self.t.alter_managelinkadd_loc,self.data.read_cell(20,17))
		self.assertIn('邮政编码格式错误',self.t.get_about(self.t.error_altermanagezip_loc))
		self.t.clickaction(self.t.alter_managesubmit_loc)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))

	def test_028(self):
		'''机构logo格式错误'''
		self.t.find_element(self.t.alter_manageorglogo_loc).send_keys(self.file_path+r'\A_006.gif')
		time.sleep(0.5)
		self.t.inputaction(self.t.alter_managelinkadd_loc,self.data.read_cell(20,17))
		self.assertIn('上传jpg/png/bmp/jpeg格式图片',self.t.get_about(self.t.error_altermanageorglogo_loc))

	def test_029(self):
		'''机构信用证扫描格式错误'''
		self.t.find_element(self.t.alter_manageorgidlogo_loc).send_keys(self.file_path+r'\A_006.gif')
		time.sleep(0.5)
		self.t.inputaction(self.t.alter_managelinkadd_loc,self.data.read_cell(20,17))
		self.assertIn('上传jpg/png/bmp/jpeg格式图片',self.t.get_about(self.t.error_altermanageorgidlogo_loc))

	def test_030(self):
		'''正常修改'''
		self.t.inputaction(self.t.alter_manageorgname_loc,self.data.read_cell(21,4))
		self.t.inputaction(self.t.alter_manageaddress_loc,self.data.read_cell(21,5))
		self.t.inputaction(self.t.alter_manageorgid_loc,self.data.read_cell(21,6))
		self.t.inputaction(self.t.alter_managewebsite_loc,self.data.read_cell(21,7))
		self.t.inputaction(self.t.alter_managelinkname_loc,self.data.read_cell(21,8))
		self.t.inputaction(self.t.alter_manageTel1_loc,self.data.read_cell(21,10))
		self.t.inputaction(self.t.alter_manageTel2_loc,self.data.read_cell(21,11))
		self.t.inputaction(self.t.alter_manageTel3_loc,self.data.read_cell(21,12))
		self.t.inputaction(self.t.alter_managephone_loc,self.data.read_cell(21,14))
		self.t.inputaction(self.t.alter_manageps_loc,self.data.read_cell(21,15))
		self.t.inputaction(self.t.alter_manageemail_loc,self.data.read_cell(21,16))
		self.t.inputaction(self.t.alter_managelinkadd_loc,self.data.read_cell(21,17))
		self.t.inputaction(self.t.alter_managezip_loc,self.data.read_cell(21,18))
		time.sleep(0.25)
		self.t.clickaction(self.t.alter_managesubmit_loc)
		time.sleep(1)
		self.assertIn('信息修改成功',self.t.get_about(self.t.alter_alerttips_loc))
		time.sleep(1)
		self.t.click(self.t.alter_alertsubmit_loc)
		time.sleep(1)
		self.assertEqual("导出 Excel",self.t.get_about(self.t.sp_manage2excel_loc))
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_managename_loc))

	def test_031(self):
		'''验证修改成功'''
		self.t.clickaction(self.t.table_manageview_loc)
		time.sleep(0.5)
		self.assertEqual(self.data.read_cell(1,1),self.t.get_about(self.t.view_managename_loc))
		self.assertEqual("机构",self.t.get_about(self.t.view_managekind_loc))
		self.assertEqual(self.data.read_cell(21,4),self.t.get_about(self.t.view_manageorgname_loc))
		self.assertEqual(self.data.read_cell(21,5),self.t.get_about(self.t.view_manageorgadd_loc))
		self.assertEqual(self.data.read_cell(21,6),self.t.get_about(self.t.view_manageorgid_loc))
		self.assertEqual(self.data.read_cell(21,7),self.t.get_about(self.t.view_managewitsite_loc))
		self.assertEqual(self.data.read_cell(21,8),self.t.get_about(self.t.view_managelinkname_loc))
		self.assertEqual(self.data.read_cell(21,9),self.t.get_about(self.t.view_manageTel_loc))
		self.assertEqual(self.data.read_cell(21,13),self.t.get_about(self.t.view_managephone_loc))
		self.assertEqual(self.data.read_cell(21,15),self.t.get_about(self.t.view_manageps_loc))
		self.assertEqual(self.data.read_cell(21,16),self.t.get_about(self.t.view_managemail_loc))
		self.assertEqual(self.data.read_cell(21,17),self.t.get_about(self.t.view_manageadd_loc))
		self.assertEqual(self.data.read_cell(21,18),self.t.get_about(self.t.view_managezip_loc))

	def test_032(self):
		'''table修改成功'''
		self.t.clickaction(self.t.sp_manageleft_loc)
		time.sleep(0.25)
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_managename_loc))
		self.t.clickaction(self.t.table_manageedit_loc)
		time.sleep(0.5)
		self.assertEqual("修改",self.t.get_about(self.t.sp_managetitle_loc))
		self.assertEqual(self.data.read_cell(1,1),self.t.get_about(self.t.alter_managename_loc))
		self.t.inputaction(self.t.alter_manageorgname_loc,self.data.read_cell(1,4))
		self.t.inputaction(self.t.alter_manageaddress_loc,self.data.read_cell(1,5))
		self.t.inputaction(self.t.alter_manageorgid_loc,self.data.read_cell(1,6))
		self.t.inputaction(self.t.alter_managewebsite_loc,self.data.read_cell(1,7))
		self.t.inputaction(self.t.alter_managelinkname_loc,self.data.read_cell(1,8))
		self.t.inputaction(self.t.alter_manageTel1_loc,self.data.read_cell(1,10))
		self.t.inputaction(self.t.alter_manageTel2_loc,self.data.read_cell(1,11))
		self.t.inputaction(self.t.alter_manageTel3_loc,self.data.read_cell(1,12))
		self.t.inputaction(self.t.alter_managephone_loc,self.data.read_cell(1,14))
		self.t.inputaction(self.t.alter_manageps_loc,self.data.read_cell(1,15))
		self.t.inputaction(self.t.alter_manageemail_loc,self.data.read_cell(1,16))
		self.t.inputaction(self.t.alter_managelinkadd_loc,self.data.read_cell(1,17))
		self.t.inputaction(self.t.alter_managezip_loc,self.data.read_cell(1,18))
		time.sleep(0.25)
		self.t.clickaction(self.t.alter_managesubmit_loc)
		time.sleep(1)
		self.assertIn('SP帐户信息修改成功',self.t.get_about(self.t.alter_alerttips_loc))
		time.sleep(0.25)
		self.t.click(self.t.alter_alertsubmit_loc)
		time.sleep(1)
		self.assertEqual("导出 Excel",self.t.get_about(self.t.sp_manage2excel_loc))

	def test_033(self):
		'''验证修改成功'''
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_managename_loc))
		self.t.clickaction(self.t.table_manageview_loc)
		time.sleep(0.5)
		self.assertEqual(self.data.read_cell(1,1),self.t.get_about(self.t.view_managename_loc))
		self.assertEqual("机构",self.t.get_about(self.t.view_managekind_loc))
		self.assertEqual(self.data.read_cell(1,4),self.t.get_about(self.t.view_manageorgname_loc))
		self.assertEqual(self.data.read_cell(1,5),self.t.get_about(self.t.view_manageorgadd_loc))
		self.assertEqual(self.data.read_cell(1,6),self.t.get_about(self.t.view_manageorgid_loc))
		self.assertEqual(self.data.read_cell(1,7),self.t.get_about(self.t.view_managewitsite_loc))
		self.assertEqual(self.data.read_cell(1,8),self.t.get_about(self.t.view_managelinkname_loc))
		self.assertEqual(self.data.read_cell(1,9),self.t.get_about(self.t.view_manageTel_loc))
		self.assertEqual(self.data.read_cell(1,13),self.t.get_about(self.t.view_managephone_loc))
		self.assertEqual(self.data.read_cell(1,15),self.t.get_about(self.t.view_manageps_loc))
		self.assertEqual(self.data.read_cell(1,16),self.t.get_about(self.t.view_managemail_loc))
		self.assertEqual(self.data.read_cell(1,17),self.t.get_about(self.t.view_manageadd_loc))
		self.assertEqual(self.data.read_cell(1,18),self.t.get_about(self.t.view_managezip_loc))

	def test_034(self):
		'''冻结原因为空'''
		self.t.clickaction(self.t.sp_manageleft_loc)
		time.sleep(0.25)
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_managename_loc))
		self.assertEqual('正常',self.t.get_about(self.t.table_managestatus_loc))
		self.t.clickaction(self.t.table_managefrost_loc)
		time.sleep(1)
		self.t.inputaction(self.t.alert_frostinput_loc,'    ')
		self.t.clickaction(self.t.alert_frostsubmit_loc)
		time.sleep(0.25)
		self.assertIn('输入提交理由',self.t.get_about(self.t.alert_frosttips_loc))

	def test_035(self):
		'''冻结成功'''
		self.t.inputaction(self.t.alert_frostinput_loc,'测试冻结')
		time.sleep(0.75)
		self.t.clickaction(self.t.alert_frostsubmit_loc)
		time.sleep(1.5)
		self.t.refresh()
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.75)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_managename_loc))
		self.assertEqual('冻结',self.t.get_about(self.t.table_managestatus_loc))
		self.assertTrue(self.t.is_visibility(self.t.table_managestop_loc))
		self.assertTrue(self.t.is_visibility(self.t.table_managestart_loc))

	def test_036(self):
		'''禁用条件为空'''
		self.t.clickaction(self.t.table_managestop_loc)
		time.sleep(1)
		self.t.inputaction(self.t.alert_stopinput_loc,'    ')
		self.t.clickaction(self.t.alert_stopsubmit_loc)
		time.sleep(0.25)
		self.assertIn('输入提交理由',self.t.get_about(self.t.alert_stoptips_loc))

	def test_037(self):
		'''禁用成功'''
		self.t.inputaction(self.t.alert_stopinput_loc,'测试禁用')
		self.t.clickaction(self.t.alert_stopsubmit_loc)
		time.sleep(1.5)
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		time.sleep(0.5)
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_managename_loc))
		self.assertEqual('禁用',self.t.get_about(self.t.table_managestatus_loc))
		self.assertTrue(self.t.is_visibility(self.t.table_managestart_loc))

	def test_038(self):
		'''启用输入为空'''
		time.sleep(0.5)
		self.t.clickaction(self.t.table_managestart_loc)
		time.sleep(1)
		self.t.inputaction(self.t.alert_startinput_loc,'   ')
		self.t.clickaction(self.t.alert_startsubmit_loc)
		time.sleep(0.25)
		self.assertIn('输入提交理由',self.t.get_about(self.t.alert_starttips_loc))

	def test_039(self):
		'''禁用启用成功'''
		self.t.inputaction(self.t.alert_startinput_loc,'禁用启用')
		self.t.clickaction(self.t.alert_startsubmit_loc)
		time.sleep(1.5)
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		time.sleep(0.25)
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.75)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_managename_loc))
		self.assertEqual('正常',self.t.get_about(self.t.table_managestatus_loc))
		self.assertTrue(self.t.is_visibility(self.t.table_managefrost_loc))

	def test_040(self):
		'''冻结启用输入为空'''
		self.t.clickaction(self.t.table_managefrost_loc)
		time.sleep(1)
		self.t.inputaction(self.t.alert_frostinput_loc,'正常冻结')
		self.t.clickaction(self.t.alert_frostsubmit_loc)
		time.sleep(1.5)
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_managename_loc))
		self.assertEqual('冻结',self.t.get_about(self.t.table_managestatus_loc))
		self.assertTrue(self.t.is_visibility(self.t.table_managestop_loc))
		self.assertTrue(self.t.is_visibility(self.t.table_managestart_loc))
		self.t.clickaction(self.t.table_managestart_loc)
		time.sleep(1)
		time.sleep(1)
		self.t.inputaction(self.t.alert_startinput_loc,'   ')
		self.t.clickaction(self.t.alert_startsubmit_loc)
		time.sleep(0.25)
		self.assertIn('输入提交理由',self.t.get_about(self.t.alert_starttips_loc))

	def test_041(self):
		'''冻结启用成功'''
		self.t.inputaction(self.t.alert_startinput_loc,'冻结启用')
		self.t.clickaction(self.t.alert_startsubmit_loc)
		time.sleep(1.5)
		self.t.inputaction(self.t.search_managename_loc,'liuhongliang_33@163.com')
		time.sleep(0.25)
		self.t.clickaction(self.t.search_managebutton_loc)
		time.sleep(0.5)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_managename_loc))
		self.assertEqual('正常',self.t.get_about(self.t.table_managestatus_loc))
		self.assertTrue(self.t.is_visibility(self.t.table_managefrost_loc))



if __name__=="__main__":
	unittest.main()
