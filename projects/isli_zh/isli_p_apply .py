
# 此4条代码可以直接运行该脚本调试

import os,sys
base_path = "D:\共享\内部SVN\Test_Au\IsliTest"
base_path = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"..")	#获取当前文件的前两级目录
sys.path.append(base_path)

import time
import logging
from base.unitBase import ParametrizedTestCase as pt
from projects.isli_zh.page.isli_p_loginModular import Module as loginModule
from projects.isli_zh.page.isli_p_operateModular import Module as operateModule


class isli_p_apply(pt):
	'''中国ISLI业务系统申请测试'''

	@classmethod
	def setUpClass(cls):
		'''打开指定网页'''
		# logging.info('测试模块: %s (%s)'%(cls.__name__,cls.__doc__))
		super().setUpClass()
		cls.t_login = loginModule(cls.driver)
		cls.t_login.open(cls.t_login.base_url)  #浏览器打开URL
		cls.t_login.user_login_verify(username='xitest051@163.com', password='a123456', codecon='8888')	#成功登入
		time.sleep(1)
		cls.t_operate = operateModule(cls.driver)
		# cls.t_operate.book_audio_service()	#图书音像关联服务

	def test_01(self):
		'''全都不输入'''
		# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
		self.t_operate.book_audio_service()	#图书音像关联服务
		self.t_operate.apply_isli()			#点击“申请ISLI标志码”
		# self.t_operate.apply_isli()
		# self.t_operate.homepage()
		# self.t_operate.issue_news_service()
		self.t_operate.audio_apply_list()
		self.t_operate.apply_isli()
		time.sleep(2)
		# self.t_operate.news_apply_list()


	




if __name__=="__main__":
	import unittest
	unittest.main()