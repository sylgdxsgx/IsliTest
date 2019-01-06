import sys,os
# sys.path.append("..")
# print(sys.path)
from isli import run_all
from base.unitBase import ParametrizedTestCase as pt
from isli.page.LC_signinpage import Signpage
# from .common.read_excel import Read
from isli.common.read_excel import Read
import unittest,time


class Sign_flow(pt):
	'''LC注册'''
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.data = Read(run_all.fppath+r'/date/ISLI_RA_signLCdata.xls')
		cls.t = Signpage(cls.driver)
		cls.url_option =r'http://172.16.3.52:8080/irap/web/provider/toRegment?toFrom=/irap/web/navigation/toNavigation/4/15'
		cls.t.open(cls.url_option)

	def test_001(self):
		'''选择注册类型页面至注册协议页面之间跳转'''
		self.t.click(('css selector','.regBtnOk'))
		# self.t.switch_handle(self.t.get_handles()[1])

		self.assertIn("該郵箱用於",self.t.get_text(('css selector','#tips')))
		self.t.click((('css selector','.btnBackh')))
		self.assertEqual("同意",self.t.get_text(('css selector','.regBtnOk')))


	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		# pass
if __name__ =="__main__":
	unittest.main()
	# pass