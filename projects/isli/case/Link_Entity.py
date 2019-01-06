import sys,random,string
# sys.path.append("..")
from base.unitBase import ParametrizedTestCase as pt
from projects.isli.page.RAMS_CreateTypePage import RamsCreateType
import unittest,time

class Link_Entity(pt):
	'''RA后台管理-服务管理-关联/实体类型'''
	@classmethod
	def setUpClass(self):
		'''登录系统'''
		logging.info('测试模块: %s (%s)'%(cls.__name__,cls.__doc__))
		super().setUpClass()
		self.t = RamsCreateType(self.driver)
		#self.driver = RamsCreateType()
		self.t.login_success()
		self.t.clickaction(self.t.severmanage_clickloc)
		self.entityname1 = "测试数据"+str(int(time.time()))						#实体类型名称1
		self.entityname2 = "测试数据"+str(int(time.time())+1)					#实体类型名称2
		self.assocname1 ="关联类型"+str(int(time.time()))						#关联类型名称1
		self.assocname2 ="关联类型"+str(int(time.time())+1)						#关联类型名称2


	def test_001(self):
		'''进入新增实体'''
		self.t.clickaction(self.t.entityType_clickloc)
		self.assertEqual("新增实体类型",self.t.get_about(self.t.entity_createbuttonloc))
		self.t.clickaction(self.t.entity_createbuttonloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_002(self):
		'''实体中文描述为空进行提交'''
		self.t.inputaction(self.t.create_entitynameCnloc,'测试输入')
		self.t.click(self.t.create_entityaboutCnloc)
		self.t.inputaction(self.t.create_entitynameEnloc,'测试输入')
		self.t.inputaction(self.t.create_entityaboutEnloc,'测试输入')
		# time.sleep(0.5)
		self.assertIn("请输入描述",self.t.get_about(self.t.create_entityaboutCnerrorloc))
		self.t.clickaction(self.t.create_submitbuttonloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_003(self):
		'''英文名为空'''
		self.t.inputaction(self.t.create_entityaboutCnloc,'测试输入')
		self.t.clearaction(self.t.create_entitynameEnloc)
		self.t.inputaction(self.t.create_entityaboutEnloc,'测试输入')
		time.sleep(0.5)
		self.assertIn("请输入实体类型名称",self.t.get_about(self.t.create_entitynameEnerrorloc))
		self.t.clickaction(self.t.create_submitbuttonloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_004(self):
		'''英文描述为空'''
		self.t.inputaction(self.t.create_entitynameEnloc,'测试输入')
		self.t.clearaction(self.t.create_entityaboutEnloc)
		self.t.inputaction(self.t.create_entityaboutCnloc,'测试输入')
		# time.sleep(0.5)
		self.assertIn("请输入描述",self.t.get_about(self.t.create_entityaboutEnerrorloc))
		self.t.clickaction(self.t.create_submitbuttonloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_005(self):
		'''中文名为空'''
		# str =''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2))
		self.t.clearaction(self.t.create_entitynameCnloc)
		self.t.inputaction(self.t.create_entityaboutEnloc,'测试输入')
		time.sleep(0.25)
		self.assertIn("请输入实体类型名称",self.t.get_about(self.t.create_entitynameCnerrorloc))
		self.t.clickaction(self.t.create_submitbuttonloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_006(self):
		'''新增时候取消'''
		self.t.inputaction(self.t.create_entitynameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_entityaboutCnloc,"测试中文描述")
		self.t.inputaction(self.t.create_entitynameEnloc,self.entityname1)
		self.t.inputaction(self.t.create_entityaboutEnloc,'测试英文描述')
		self.t.clickaction(self.t.create_abolishbuttonloc)
		self.assertEqual("新增实体类型",self.t.get_about(self.t.entity_createbuttonloc))

	def test_007(self):
		'''正常提交实体类型'''
		self.t.clickaction(self.t.entity_createbuttonloc)
		self.t.inputaction(self.t.create_entitynameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_entityaboutCnloc,"测试中文描述")
		self.t.inputaction(self.t.create_entitynameEnloc,self.entityname1)
		self.t.inputaction(self.t.create_entityaboutEnloc,'测试英文描述')
		self.t.clickaction(self.t.create_submitbuttonloc)
		time.sleep(0.5)
		self.assertEqual(self.entityname1,self.t.get_about(self.t.table_entitynameloc))

	def test_008(self):
		'''连续多次提交实体类型申请'''
		time.sleep(0.5)
		self.t.clickaction(self.t.entity_createbuttonloc)
		time.sleep(0.5)
		self.t.inputaction(self.t.create_entitynameCnloc,self.entityname2)
		self.t.inputaction(self.t.create_entityaboutCnloc,"测试中文描述")
		self.t.inputaction(self.t.create_entitynameEnloc,self.entityname2)
		self.t.inputaction(self.t.create_entityaboutEnloc,'测试英文描述')
		self.t.clickaction(self.t.create_savebuttonloc)
		self.assertEqual(self.entityname2,self.t.get_about(self.t.create_entitysubmittipsloc))
		time.sleep(1)
		self.t.click(self.t.create_entitysubmiloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))


	def test_009(self):
		'''新增实体中文名重复'''
		self.t.inputaction(self.t.create_entitynameCnloc,self.entityname2)
		self.t.inputaction(self.t.create_entityaboutCnloc,"测试中文描述")
		self.t.clickaction(self.t.create_submitbuttonloc)
		time.sleep(0.5)
		self.assertIn("名称已存在",self.t.get_about(self.t.entity_renameCnerrorloc))


	def test_010(self):
		'''新增实体英文名重复'''
		self.t.inputaction(self.t.create_entitynameEnloc,self.entityname2)
		self.t.inputaction(self.t.create_entityaboutEnloc,'测试英文描述')
		self.t.clickaction(self.t.create_submitbuttonloc)
		time.sleep(0.5)
		self.assertTrue(self.t.get_about(self.t.entity_renameEnerrorloc))
		self.t.clickaction(self.t.create_abolishbuttonloc)

	def test_011(self):
		'''查看'''
		self.t.click(self.t.table_entityviewloc)
		self.assertEqual("查看",self.t.get_about(self.t.create_titleloc))

	def test_012(self):
		'''修改的中文实体名为空'''
		self.t.click(('css selector','[value="修改"]'))
		self.t.clearaction(self.t.create_entitynameCnloc)
		self.t.inputaction(self.t.create_entityaboutEnloc,'测试输入')
		# time.sleep(0.5)
		self.assertIn("请输入实体类型名称",self.t.get_about(self.t.create_entitynameCnerrorloc))
		self.t.clickaction(self.t.create_submitbuttonloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_013(self):
		'''修改中文描述为空'''
		self.t.refresh()
		self.t.clearaction(self.t.create_entityaboutCnloc)
		self.t.inputaction(self.t.create_entitynameCnloc,'测试输入')
		self.assertIn("请输入描述",self.t.get_about(self.t.create_entityaboutCnerrorloc))
		self.t.clickaction(self.t.create_submitbuttonloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_014(self):
		'''修改英文名为空'''
		self.t.refresh()
		self.t.clearaction(self.t.create_entitynameEnloc)
		self.t.inputaction(self.t.create_entityaboutCnloc,'测试输入')
		time.sleep(0.25)
		self.assertIn("请输入实体类型名称",self.t.get_about(self.t.create_entitynameEnerrorloc))
		self.t.clickaction(self.t.create_submitbuttonloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_015(self):
		'''修改英文描述为空'''
		self.t.refresh()
		self.t.clearaction(self.t.create_entityaboutEnloc)
		self.t.inputaction(self.t.create_entitynameCnloc,'测试输入')
		# self.t.clickaction(self.t.create_submitbuttonloc)
		time.sleep(0.25)
		self.assertIn("请输入描述",self.t.get_about(self.t.create_entityaboutEnerrorloc))
		# self.t.clickaction(self.t.create_submitbuttonloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_016(self):
		'''修改已存在的中文名失败'''
		self.t.refresh()
		self.t.inputaction(self.t.create_entityaboutEnloc,"英文描述")
		self.t.inputaction(self.t.create_entitynameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_entityaboutCnloc,"测试中文描述")
		self.t.clickaction(self.t.create_submitbuttonloc)
		time.sleep(0.5)
		self.assertIn("名称已存在",self.t.get_about(self.t.entity_renameCnerrorloc))
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_017(self):
		'''修改已存在的英文名失败'''
		self.t.refresh()
		self.t.inputaction(self.t.create_entitynameCnloc,self.entityname1+'修改')
		self.t.inputaction(self.t.create_entitynameEnloc,self.entityname1)
		self.t.inputaction(self.t.create_entityaboutCnloc,"测试描述")
		self.t.clickaction(self.t.create_submitbuttonloc)
		time.sleep(0.5)
		self.assertTrue(self.t.get_about(self.t.entity_renameEnerrorloc))
		# self.assertTrue(self.t.get_about(self.t.create_entitynameEnerrorloc))
		self.t.clickaction(self.t.create_submitbuttonloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_018(self):
		'''正常修改成功'''
		self.t.refresh()
		time.sleep(0.5)
		self.t.inputaction(self.t.create_entitynameCnloc,self.entityname1+'修改')
		self.t.inputaction(self.t.create_entitynameEnloc,self.entityname1+'修改')
		self.t.clickaction(self.t.create_submitbuttonloc)
		time.sleep(0.5)
		self.t.refresh()
		time.sleep(0.25)
		self.assertEqual(self.entityname1+'修改',self.t.get_about(self.t.table_entitynameloc))

	def test_019(self):
		'''列表入口修改成功'''
		self.t.clickaction(self.t.table_entityeditloc)
		time.sleep(0.25)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))
		self.t.inputaction(self.t.create_entitynameCnloc,self.entityname2)
		self.t.inputaction(self.t.create_entitynameEnloc,self.entityname2)
		self.t.clickaction(self.t.create_submitbuttonloc)
		time.sleep(0.5)
		self.assertEqual(self.entityname2,self.t.get_about(self.t.table_entitynameloc))

	def test_020(self):
		'''实体类型搜索搜索		测试数据1515741699'''
		# self.t.clickaction(self.t.entityType_clickloc)
		self.t.inputaction(self.t.search_entityloc,self.entityname2)
		self.t.clickaction(self.t.search_buttonloc)
		self.assertTrue(self.t.get_about(self.t.table_entitynameloc))

	def test_021(self):
		'''停用加搜索'''
		self.t.clearelement(self.t.search_entityloc)
		self.t.clickaction(self.t.search_buttonloc)
		self.t.clickaction(self.t.table_entitystoploc)
		time.sleep(0.5)
		self.assertIn(self.entityname2,self.t.get_about(self.t.entity_stoptipsloc))
		time.sleep(0.5)
		self.t.clickaction(self.t.entity_stopsubmitloc)
		time.sleep(0.25)
		self.t.selectaction(self.t.search_statusloc,index =2)
		self.t.clickaction(self.t.search_buttonloc)
		self.assertEqual(self.entityname2,self.t.get_about(self.t.table_entitynameloc))
		self.assertTrue(self.t.is_exists(self.t.table_entitystartloc))

	def test_022(self):
		'''启用 加搜索'''
		time.sleep(0.25)
		self.t.clickaction(self.t.table_entitystartloc)
		time.sleep(0.5)
		self.assertIn(self.entityname2,self.t.get_about(self.t.entity_stoptipsloc))
		self.t.clickaction(self.t.entity_stopsubmitloc)
		self.t.refresh()
		time.sleep(0.25)
		self.t.selectaction(self.t.search_statusloc,index =1)
		self.t.clickaction(self.t.search_buttonloc)
		self.assertEqual(self.entityname2,self.t.get_about(self.t.table_entitynameloc))
		self.assertTrue(self.t.is_exists(self.t.table_entitystoploc))

	def test_023(self):
		'''进入新增关联类型页面'''
		self.t.clickaction(self.t.associationType_clickloc)
		self.assertEqual("新增关联类型",self.t.get_about(self.t.associationType_createbuttonloc))
		self.t.clickaction(self.t.associationType_createbuttonloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_024(self):
		'''操作中文源类型为空'''
		time.sleep(0.5)
		self.t.selecttext(self.t.create_sourcenameCnloc,self.entityname1)
		self.t.selecttext(self.t.create_targetnameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.t.inputaction(self.t.create_associationnameEnloc,self.assocname1)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.t.inputaction(self.t.create_associationnameCnloc,self.assocname1)
		self.t.selectaction(self.t.create_sourcenameCnloc,index=0)
		time.sleep(0.5)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		# self.assertIn("请选择源类型",self.t.get_about(self.t.error_sourcenameCnloc))
		self.assertIn("请选择源类型",self.t.get_about(self.t.error_sourcenameEnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_025(self):
		'''操作中文关联类型为空'''
		self.t.refresh()
		time.sleep(0.25)
		self.t.inputaction(self.t.create_associationnameCnloc,'  ')
		self.t.selecttext(self.t.create_sourcenameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		time.sleep(0.25)
		self.assertIn("请输入关联类型名称",self.t.get_about(self.t.error_associationnameCnloc))
		self.t.selecttext(self.t.create_targetnameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_associationnameEnloc,self.assocname1)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_026(self):
		'''操作中文目标类型为空'''
		self.t.selectaction(self.t.create_sourcenameCnloc,index=1)
		time.sleep(0.5)
		self.t.selectaction(self.t.create_targetnameCnloc,index=0)
		time.sleep(0.5)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		time.sleep(0.25)
		self.assertIn("请选择目标类型",self.t.get_about(self.t.error_targetnameCnloc))
		self.assertIn("请选择目标类型",self.t.get_about(self.t.error_targetnameEnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_027(self):
		'''中文描述为空'''
		self.t.selectaction(self.t.create_targetnameCnloc,index=1)
		self.t.clearaction(self.t.create_associationaboutCnloc)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.assertIn('请输入描述',self.t.get_about(self.t.error_associationaboutCnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_028(self):
		'''英文关联名为空'''
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.t.clearaction(self.t.create_associationnameEnloc)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.assertIn("请输入关联类型名称",self.t.get_about(self.t.error_associationnameEnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_029(self):
		'''操作英文源为空'''
		self.t.inputaction(self.t.create_associationnameEnloc,self.assocname1)
		self.t.selectaction(self.t.create_sourcenameEnloc,index=0)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn("请选择源类型",self.t.get_about(self.t.error_sourcenameCnloc))
		self.assertIn("请选择源类型",self.t.get_about(self.t.error_sourcenameEnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_030(self):
		'''操作英文目标类型为空'''
		self.t.selectaction(self.t.create_sourcenameEnloc,index=1)
		self.t.selectaction(self.t.create_targetnameEnloc,index=0)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn("请选择目标类型",self.t.get_about(self.t.error_targetnameCnloc))
		self.assertIn("请选择目标类型",self.t.get_about(self.t.error_targetnameEnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_031(self):
		'''英文描述为空'''
		self.t.selectaction(self.t.create_targetnameEnloc,index=1)
		self.t.clearaction(self.t.create_associationaboutEnloc)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn('请输入描述',self.t.get_about(self.t.error_associationaboutEnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_032(self):
		'''新增时取消并重新进入'''
		self.t.clickaction(self.t.association_abolishloc)
		self.assertEqual("新增关联类型",self.t.get_about(self.t.associationType_createbuttonloc))
		self.t.clickaction(self.t.associationType_createbuttonloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_033(self):
		'''正常提交注册'''
		self.t.inputaction(self.t.create_associationnameCnloc,self.assocname1)
		self.t.selecttext(self.t.create_sourcenameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.t.selecttext(self.t.create_targetnameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_associationnameEnloc,self.assocname1)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual(self.assocname1,self.t.get_about(self.t.table_associationnameloc))
		self.assertEqual(self.entityname1,self.t.get_about(self.t.table_sourceloc))
		self.assertEqual(self.entityname1,self.t.get_about(self.t.table_targetloc))

	def test_034(self):
		'''连续提交多次申请'''
		self.t.clickaction(self.t.associationType_createbuttonloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))
		self.t.inputaction(self.t.create_associationnameCnloc,self.assocname2)
		self.t.selecttext(self.t.create_sourcenameCnloc,self.entityname2)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.t.selecttext(self.t.create_targetnameCnloc,self.entityname2)
		self.t.inputaction(self.t.create_associationnameEnloc,self.assocname2)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.t.clickaction(self.t.association_savebuttonloc)
		time.sleep(0.5)
		self.assertIn(self.assocname2,self.t.get_about(self.t.association_savetipsloc))
		time.sleep(0.5)
		self.t.clickaction(self.t.association_framesubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_035(self):
		'''新增关联类型名称中文名重复'''
		self.t.refresh()
		time.sleep(0.25)
		self.t.inputaction(self.t.create_associationnameCnloc,self.assocname2)
		self.t.selecttext(self.t.create_sourcenameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		time.sleep(0.25)
		self.assertIn('名称已存在',self.t.get_about(self.t.error_associationnameOneCnloc))
		self.t.selecttext(self.t.create_targetnameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_associationnameEnloc,str(int(time.time())))
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))

	def test_036(self):
		'''新增关联类型名称英文名重复'''
		self.t.refresh()
		time.sleep(0.25)
		self.t.inputaction(self.t.create_associationnameCnloc,str(int(time.time())))
		self.t.selecttext(self.t.create_sourcenameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.t.selecttext(self.t.create_targetnameCnloc,self.entityname1)
		self.t.inputaction(self.t.create_associationnameEnloc,self.assocname2)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		time.sleep(0.5)
		self.assertTrue(self.t.get_about(self.t.error_associationnameOneEnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("新增",self.t.get_about(self.t.create_titleloc))
		self.t.clickaction(self.t.create_abolishbuttonloc)
		self.assertEqual("新增关联类型",self.t.get_about(self.t.associationType_createbuttonloc))

	def test_037(self):
		'''查看关联类型'''
		self.t.clickaction(self.t.table_assocviewloc)
		self.assertIn("查看",self.t.get_about(self.t.create_titleloc))

	def test_038(self):
		'''修改-关联名中文为空'''
		self.t.click(('css selector','[value="修改"]'))
		self.t.clearaction(self.t.association_renameCnloc)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn("输入关联类型名称",self.t.get_about(self.t.error_associationnameCnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_039(self):
		'''修改-中文关联名重复'''
		self.t.refresh()
		time.sleep(0.25)
		self.t.inputaction(self.t.association_renameCnloc,self.assocname1)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn("名称已存在",self.t.get_about(self.t.error_associationnameOneCnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_040(self):
		'''修改-中文描述为空'''
		self.t.refresh()
		time.sleep(0.25)
		self.t.inputaction(self.t.association_renameCnloc,self.assocname2+"修改")
		self.t.clearaction(self.t.create_associationaboutCnloc)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.assertIn('请输入描述',self.t.get_about(self.t.error_associationaboutCnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_041(self):
		'''修改-英文名为空'''
		self.t.refresh()
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.t.clearaction(self.t.association_renameEnloc)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.assertIn("请输入关联类型名称",self.t.get_about(self.t.error_associationnameEnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_042(self):
		'''修改-英文名重复'''
		self.t.refresh()
		self.t.inputaction(self.t.association_renameEnloc,self.assocname1)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		time.sleep(0.5)
		self.assertTrue(self.t.get_about(self.t.error_associationnameOneEnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_043(self):
		'''修改-英文描述为空'''
		self.t.refresh()
		self.t.inputaction(self.t.association_renameEnloc,self.assocname2+'修改')
		self.t.clearaction(self.t.create_associationaboutEnloc)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.assertIn('请输入描述',self.t.get_about(self.t.error_associationaboutEnloc))
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))

	def test_044(self):
		'''正常修改成功'''
		self.t.inputaction(self.t.association_renameCnloc,self.assocname2+'修改')
		self.t.selecttext(self.t.create_sourcenameCnloc,self.entityname2)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.t.selecttext(self.t.create_targetnameCnloc,self.entityname2)
		self.t.inputaction(self.t.association_renameEnloc,self.assocname2+'修改')
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.t.clickaction(self.t.association_createsubmitloc)
		self.assertEqual(self.assocname2+'修改',self.t.get_about(self.t.table_associationnameloc))
		self.assertEqual(self.entityname2,self.t.get_about(self.t.table_sourceloc))
		self.assertEqual(self.entityname2,self.t.get_about(self.t.table_targetloc))

	def test_045(self):
		'''列表修改成功'''
		self.t.clickaction(self.t.table_assoceditloc)
		self.assertEqual("修改",self.t.get_about(self.t.create_titleloc))
		self.t.inputaction(self.t.association_renameCnloc,self.assocname2)
		self.t.selecttext(self.t.create_sourcenameCnloc,self.entityname2)
		self.t.inputaction(self.t.create_associationaboutCnloc,"测试新增关联类型中文描述")
		self.t.selecttext(self.t.create_targetnameCnloc,self.entityname2)
		self.t.inputaction(self.t.association_renameEnloc,self.assocname2)
		self.t.inputaction(self.t.create_associationaboutEnloc,"测试新增关联类型英文描述")
		self.t.clickaction(self.t.association_createsubmitloc)
		time.sleep(1.5)
		self.assertEqual(self.assocname2,self.t.get_about(self.t.table_associationnameloc))
		self.assertEqual(self.entityname2,self.t.get_about(self.t.table_sourceloc))
		self.assertEqual(self.entityname2,self.t.get_about(self.t.table_targetloc))

	def test_046(self):
		'''停用+状态停用搜索'''
		time.sleep(0.5)
		self.t.clickaction(self.t.table_assocstoploc)
		self.assertIn(self.assocname2,self.t.get_about(self.t.association_savetipsloc))
		time.sleep(0.5)
		self.t.clickaction(self.t.association_submitloc)
		self.t.refresh()
		time.sleep(0.5)
		self.t.selectaction(self.t.search_statusloc,index=2)
		self.t.clickaction(self.t.search_buttonloc)
		self.assertEqual(self.assocname2,self.t.get_about(self.t.table_associationnameloc))
		self.assertTrue(self.t.is_exists(self.t.table_assocstartloc))

	def test_047(self):
		'''关联类型搜索'''
		self.t.selectaction(self.t.search_statusloc,index=0)
		self.t.inputaction(self.t.search_associationloc,self.assocname1)
		self.t.clickaction(self.t.search_buttonloc)
		self.assertEqual(self.assocname1,self.t.get_about(self.t.table_associationnameloc))
		self.assertTrue(self.t.is_exists(self.t.table_assocstoploc))

	def test_048(self):
		'''源类型搜索'''
		self.t.clearaction(self.t.search_associationloc)
		self.t.inputaction(self.t.search_sourceloc,self.entityname2)
		self.t.clickaction(self.t.search_buttonloc)
		time.sleep(1.5)
		self.assertEqual(self.entityname2,self.t.get_about(self.t.table_sourceloc))
		self.assertTrue(self.t.is_exists(self.t.table_assocstartloc))

	def test_049(self):
		'''目标类型搜索'''
		self.t.clearaction(self.t.search_sourceloc)
		self.t.inputaction(self.t.search_targetloc,self.entityname1)
		self.t.clickaction(self.t.search_buttonloc)
		self.assertEqual(self.entityname1,self.t.get_about(self.t.table_targetloc))
		self.assertTrue(self.t.is_exists(self.t.table_assocstoploc))

	def test_050(self):
		'''正常启用'''
		time.sleep(1)
		self.t.clearaction(self.t.search_targetloc)
		self.t.clickaction(self.t.search_buttonloc)
		self.t.clickaction(self.t.table_assocstartloc)
		self.assertIn(self.assocname2,self.t.get_about(self.t.association_savetipsloc))
		time.sleep(0.5)
		self.t.clickaction(self.t.association_submitloc)
		time.sleep(0.5)
		self.t.refresh()
		self.assertEqual(self.assocname2,self.t.get_about(self.t.table_associationnameloc))
		self.assertTrue(self.t.is_exists(self.t.table_assocstoploc))

	def test_051(self):
		'''停用新增关联'''
		self.t.inputaction(self.t.search_associationloc,self.assocname1)
		self.t.clickaction(self.t.search_buttonloc)
		self.t.clickaction(self.t.table_assocstoploc)
		self.assertIn(self.assocname1,self.t.get_about(self.t.association_savetipsloc))
		time.sleep(0.5)
		self.t.clickaction(self.t.association_submitloc)
		time.sleep(1)
		self.assertEqual(self.assocname1,self.t.get_about(self.t.table_associationnameloc))
		self.assertTrue(self.t.is_exists(self.t.table_assocstartloc))

		# self.t.inputaction(self.t.search_associationloc,self.assocname2)
		# self.t.clickaction(self.t.search_buttonloc)
		# self.t.clickaction(self.t.table_assocstoploc)
		# self.assertIn(self.assocname2,self.t.get_about(self.t.association_savetipsloc))
		# time.sleep(0.5)
		# self.t.clickaction(self.t.association_submitloc)
		# time.sleep(1)
		# self.assertEqual(self.assocname2,self.t.get_about(self.t.table_associationnameloc))
		# self.assertTrue(self.t.is_exists(self.t.table_assocstartloc))


	def test_052(self):
		'''停用新增实体'''
		self.t.clickaction(self.t.entityType_clickloc)
		time.sleep(0.75)
		self.t.inputaction(self.t.search_entityloc,self.entityname2)
		self.t.clickaction(self.t.search_buttonloc)
		self.t.clickaction(self.t.table_entitystoploc)
		time.sleep(0.5)
		self.assertIn(self.entityname2,self.t.get_about(self.t.entity_stoptipsloc))
		time.sleep(0.5)
		self.t.clickaction(self.t.entity_stopsubmitloc)
		self.assertEqual(self.entityname2,self.t.get_about(self.t.table_entitynameloc))
		self.assertTrue(self.t.is_exists(self.t.table_entitystartloc))

		self.t.inputaction(self.t.search_entityloc,self.entityname1)
		self.t.clickaction(self.t.search_buttonloc)
		self.t.clickaction(self.t.table_entitystoploc)
		time.sleep(0.5)
		self.assertIn(self.entityname1,self.t.get_about(self.t.entity_stoptipsloc))
		time.sleep(0.5)
		self.t.clickaction(self.t.entity_stopsubmitloc)
		time.sleep(0.25)
		self.assertEqual(self.entityname1,self.t.get_about(self.t.table_entitynameloc))
		self.assertTrue(self.t.is_exists(self.t.table_entitystartloc))




if __name__=="__main__":
	unittest.main()