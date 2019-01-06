from base.unitBase import ParametrizedTestCase as pt
from isli.page.RA_SPManagePage import SPmanage
from isli.common.read_excel import Read
from isli import run_all
import unittest,time,os


class RASPcheck(pt):
	'''Sp账户审核'''

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
		'''进入sp账户审核页面正常'''
		self.t.clickaction(self.t.sp_manageTop_loc)
		self.t.clickaction(self.t.sp_managecheckleft_loc)
		self.assertEqual("SP帐户审核",self.t.get_about(self.t.sp_managechecktitle_loc))
		self.assertEqual("导出 Excel",self.t.get_about(self.t.sp_manage2excel_loc))

	def test_002(self):
		'''用户名搜索功能正常'''
		self.t.inputaction(self.t.search_checkname_loc,"liuhongliang_33@163.com")
		self.t.clickaction(self.t.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_spcheckname_loc))

	def test_003(self):
		'''机构搜索正常'''
		self.t.clearaction(self.t.search_checkname_loc)
		self.t.selecttext(self.t.search_managekind_loc,'机构')
		self.t.clickaction(self.t.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('机构',self.t.get_about(self.t.table_spcheckkind_loc))

	def test_004(self):
		'''个人搜索成功'''
		self.t.selecttext(self.t.search_managekind_loc,'个人')
		self.t.clickaction(self.t.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('个人',self.t.get_about(self.t.table_spcheckkind_loc))

	def test_005(self):
		'''状态-待初审搜索成功'''
		self.t.selecttext(self.t.search_managekind_loc,'- 全部 -')
		self.t.selecttext(self.t.search_managestatus_loc,'待初审')
		self.t.clickaction(self.t.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('待初审',self.t.get_about(self.t.table_spcheckstatus_loc))

	def test_006(self):
		'''状态-待复审搜索成功'''
		self.t.selecttext(self.t.search_managekind_loc,'- 全部 -')
		self.t.selecttext(self.t.search_managestatus_loc,'待复审')
		self.t.clickaction(self.t.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('待复审',self.t.get_about(self.t.table_spcheckstatus_loc))

	def test_007(self):
		'''状态-未通过搜索成功'''
		self.t.selecttext(self.t.search_managestatus_loc,'未通过')
		self.t.clickaction(self.t.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('未通过',self.t.get_about(self.t.table_spcheckstatus_loc))

	def test_008(self):
		'''状态-已通过搜索成功'''
		self.t.selecttext(self.t.search_managestatus_loc,'已通过')
		self.t.clickaction(self.t.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('已通过',self.t.get_about(self.t.table_spcheckstatus_loc))

	def test_009(self):
		'''审核-拒绝-意见为空'''
		self.t.selecttext(self.t.search_managestatus_loc,'- 全部 -')
		self.t.inputaction(self.t.search_checkname_loc,"liuhongliang01@163.com")
		self.t.clickaction(self.t.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('待初审',self.t.get_about(self.t.table_spcheckstatus_loc))
		self.assertEqual('liuhongliang01@163.com',self.t.get_about(self.t.table_spcheckname_loc))
		self.t.clickaction(self.t.table_spcheck_loc)
		time.sleep(0.5)
		self.t.clickaction(self.t.alert_checkno_loc)
		self.t.clickaction(self.t.alert_checkbutton_loc)
		time.sleep(0.5)
		self.assertIn('请输入审批意见',self.t.get_about(self.t.alert_checktips_loc))
		self.t.clickaction(self.t.alert_checkclose_loc)

	def test_010(self):
		'''重发链接成功'''
		self.t.inputaction(self.t.search_checkname_loc,"xitest111@163.com")
		self.t.clickaction(self.t.search_checkbutton_loc)
		time.sleep(0.25)
		self.assertEqual('未通过',self.t.get_about(self.t.table_spcheckstatus_loc))
		self.assertEqual('xitest111@163.com',self.t.get_about(self.t.table_spcheckname_loc))
		self.t.clickaction(self.t.table_spcheckagain_loc)
		time.sleep(1)
		self.assertIn('恭喜您！已成功发送新的注册链接',self.t.get_about(self.t.alert_checkagaintips_loc))
		self.t.clickaction(self.t.alert_checkagainbutton_loc)
		time.sleep(0.5)

	def test_011(self):
		'''查看成功'''
		self.t.inputaction(self.t.search_checkname_loc,'liuhongliang_33@163.com')
		self.t.clickaction(self.t.search_checkbutton_loc)
		time.sleep(0.5)
		self.assertEqual('已通过',self.t.get_about(self.t.table_spcheckstatus_loc))
		self.assertEqual('liuhongliang_33@163.com',self.t.get_about(self.t.table_spcheckname_loc))
		self.t.clickaction(self.t.table_manageview_loc)
		time.sleep(0.5)
		self.assertEqual(self.data.read_cell(1,1),self.t.get_about(self.t.view_managename_loc))
		self.assertEqual('已通过',self.t.get_about(self.t.view_managestatus_loc))
		self.assertEqual('2017-11-06',self.t.get_about(self.t.view_manamgedate_loc))
		self.assertEqual('阿尔巴尼亚',self.t.get_about(self.t.view_managearea_loc))
		self.assertEqual("机构",self.t.get_about(self.t.view_managekind_loc))
		self.assertEqual('测试数据-HLLiu',self.t.get_about(self.t.view_manageorgname_loc))
		self.assertEqual(self.data.read_cell(1,5),self.t.get_about(self.t.view_manageorgadd_loc))
		self.assertEqual('1251241211',self.t.get_about(self.t.view_manageorgid_loc))
		self.assertEqual('',self.t.get_about(self.t.view_managewitsite_loc))
		self.assertEqual('测试数据-HLLiu',self.t.get_about(self.t.view_managelinkname_loc))
		self.assertEqual('-',self.t.get_about(self.t.view_manageTel_loc))
		self.assertEqual('86-18513519528',self.t.get_about(self.t.view_managephone_loc))
		self.assertEqual('',self.t.get_about(self.t.view_manageps_loc))
		self.assertEqual('liuhongliang_35@163.com',self.t.get_about(self.t.view_managemail_loc))
		self.assertEqual('深圳',self.t.get_about(self.t.view_manageadd_loc))
		self.assertEqual('',self.t.get_about(self.t.view_managezip_loc))


if __name__ =="__mian__":
	unittest.main()















