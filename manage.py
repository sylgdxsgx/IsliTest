import os,sys,time,logging
sys.path.append('%s/projects'%sys.path[0])   #将projects添加到系统变量中
import importlib.util
import unittest
from selenium import webdriver
from base.testBase import ParametrizedTestCase as pt1
from base.testBase import PTestCase as pt
from base import function
from HTMLTestRunner import HTMLTestRunner
from configparser import ConfigParser
from multiprocessing import Pool
from threading import Thread

# suite = unittest.TestSuite()

def main():
	"""解析数据"""
	# test = sys.argv[1]
	# conf = ConfigParser()
	# conf_file = '/opt/proj/script/test_list.list'
	# conf.read(conf_file)
	# test_list = conf.get(test,'value')
	# test_list = eval(test_list)
	"""启用多进程"""
	# pool = Pool(2)
	# # for i in range(len(test_list)):
		# # pool.apply_async(sample_request,args=(test_list[i],))   #异步
		# # print(1)
	# pool.map(sample_request,test_list)  #并行
	# pool.close()
	# pool.join()

	"""启用多线程"""
	#按执行机来分开，及每个执行机一条线程(驱动在线程中生成)
	# threads = []
	# for i in range(len(test_list)):
		# t = Thread(target=sample_request,args=(test_list[i],))
		# threads.append(t)
	# for t in threads:
		# t.start()
	#无需t.join()，它会等待所有线程结束才结束(默认情况)


	"""单线程"""
	# for i in range(len(test_list)):
		# sample_request(test_list[i])
	test_on_node()
	
def test_on_node():
	"""开始分布式测试（多个节点同时运行。）"""
	test = sys.argv[1]
	conf = ConfigParser()
	conf_file = '/opt/proj/script/test_list.list'
	conf.read(conf_file)
	test_list = conf.get(test,'value')
	test_list = eval(test_list)
	
	threads = []
	
	for test in test_list:	#test= {'http://172.16.7.34:5555/wd/hub': [('projects/isli/case/RAlogin.py', 'chrome'),...]} 一台机器的测试项
		driver,mode_list,node = function.createDriver(test)
		if driver:
			t = Thread(target=sample_test,args=(driver,mode_list,node))
			threads.append(t)
			
	for t in threads:
		t.start()
		
	for t in threads:
		t.join()
		
	logging.info('分布式测试完毕')
	#无需t.join()，它会等待所有线程结束才结束(默认情况)	
	
def sample_test(driver,mode_list,node):
	"""单节点测试"""
	suite = unittest.TestSuite()
	ip,port = node.split('//')[1].split('/')[0].split(':')
	for mode in mode_list:
		
		#动态引入模块
        module = function.import_module_from_file(mode) 
        if not module is None: 
            #读取模块中的测试用例
            suite.addTest(get_suite_from_module(module,mode,driver))
				
	#测试套件已经准备好，开始测试
	#检查端口是否启动
	for i in range(5):
		if function.IsPortInUse(ip,port):
			break
		time.sleep(2)
	else:
		logging.info('远程node连接失败: http://%s:%s'%(ip,port))
	time.sleep(5)


	test_result_file = sys.path[0]+'/%s.html'%sys.argv[1]
	with open(test_result_file,'wb') as fp:
		runner = HTMLTestRunner(stream = fp,title = "自动化测试报告",description="测试机：%s:%s   测试模块：%s"%(ip,port,str(mode_list)))
		runner.run(suite)
	function.send_email(test_result_file,receivers)
	os.remove(test_result_file)

def get_suite_from_module(module,mode,devices):
    '''读取模块中的测试用例'''
    suite = unittest.TestSuite()
    classnames = function.get_className(mode)
    class_name = classnames[0]  #读取第一个用例类名称，为字符串
    if hasattr(module,class_name): #如果有该属性值(类)
        _class = getattr(module,class_name)    #获取这个类
        suite.addTest(pt.parametrize(_class,driver=devices,remote=True))   #为本地调试模式
    return suite  

if __name__== '__main__':
    function.logging_out('/opt/proj/script/logInfo.log') #设置日志
    logging.info('开始本轮测试：%s'%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    if len(sys.argv) < 2:
        logging.info('Usage: media_player.py <filename> [<filename> ...]')
        sys.exit(1)
    receivers = ["shigx@mpreader.com"]
    main()