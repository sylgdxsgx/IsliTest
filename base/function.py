import os
import sys
import socket
import smtplib
import logging
import unittest
import importlib.util
from configparser import ConfigParser
from functools import wraps
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner

	
def createDriver(dict_caps):
    """ dict_caps:{'http://172.16.7.34:5555/wd/hub': [('projects/isli/case/RAlogin.py', 'chrome'),...]}
		返回驱动(driver,mode_list,node)或者 False,False,False"""
    for node,tests in dict_caps.items():
        test_list = []
        for test,caps in tests:		#caps= 'firefox'	test= 'projects/isli/case/RAlogin.py'
            test_list.append(test)
            caps = eval('DesiredCapabilities.%s'%caps.upper())
        return webdriver.Remote(command_executor=node, desired_capabilities=caps),test_list,node
    return False,False,False

def class_log():
	'''打印类日志'''
	def _test(cls):
		@wraps(cls)
		def __test(*args,**kw):
			logging.info('---------- %s (%s)----------'%(cls.__name__,cls.__doc__))
			# logging.info('测试模块: %s (%s)'%(cls.__name__,cls.__doc__))
			# logging.info('%s %s'%(self.__dict__['_testMethodName'],self.__dict__['_testMethodDoc']))
			return cls(*args,**kw)
		return __test
	return _test

def conf_read(flag):
    conf = ConfigParser()
    conf.read('flag.list')
    try:
        flag = conf.get('TestFlag',flag)
        return flag
    except:
        return 'None'
    
def conf_write(testcase=None):
    '''把用例设置为Fail'''
    conf = ConfigParser()
    conf.read('TestFlag.list')
    if testcase == None:    #初始化TestFlag
        try:
            conf.add_section('Test_Rlt')
        except:
            pass
        for option in conf.options('Test_Rlt'):
            conf.set('Test_Rlt',option,'')
    else:
        conf.set('Test_Rlt',testcase,'Fail')
    with open('TestFlag.list','w') as f:
        conf.write(f)

def SkipIf_Fail(testcasename):
    """当testcasename失败时，则跳转"""
    def decorator(func):
        def wrapper(self,*args,**kwargs):
            for testrlt in self._outcome.result.failures:
                if testrlt[0]._testMethodName == testcasename:
                    raise unittest.SkipTest("{} do not excute because <{}> is FAILED".format(func.__name__,testcasename))
            func(self,*args,**kwargs)
        return wrapper
    return decorator
    
def SkipIf_NotPass(testcasename):
    """当testcasename:failures/skipped/errors时，则跳转"""
    def decorator(func):
        def wrapper(self,*args,**kwargs):
            # logging.info('result:'+str(self._outcome.result.result))
            # logging.info('failures:'+str(self._outcome.result.failures))
            # logging.info('skipped:'+str(self._outcome.result.skipped))
            # logging.info('errors:'+str(self._outcome.result.errors))
            # logging.info('expectedFailures:'+str(self._outcome.result.expectedFailures))
            # logging.info(vars(self._outcome.result))
            # logging.info('prevtestcase:'+str(self._outcome.result.result[-1][1]._testMethodName))
            # logging.info('------')
            #python3.4之后没有_resultForDoCleanups
            for testrlt in self._outcome.result.failures:
                if testrlt[0]._testMethodName == testcasename:
                    raise unittest.SkipTest("{} do not excute because <{}> is FAILED".format(func.__name__,testcasename))
            for testrlt in self._outcome.result.errors:
                if testrlt[0]._testMethodName == testcasename:
                    raise unittest.SkipTest("{} do not excute because <{}> is ERRORS".format(func.__name__,testcasename))
            for testrlt in self._outcome.result.skipped:
                if testrlt[0]._testMethodName == testcasename:
                    raise unittest.SkipTest("{} do not excute because <{}> is SKIPPED".format(func.__name__,testcasename))
            func(self,*args,**kwargs)
        return wrapper
    return decorator
    
def SkipIf_PrevNotPass():
    """当上一条用例没有PASS时，则跳转"""
    def decorator(func):
        def wrapper(self,*args,**kwargs):
            # logging.info('result:'+str(self._outcome.result.result))
            if self._outcome.result.result[-1][0] ==1:
                raise unittest.SkipTest("{} do not excute because prevtestcase <{}> is FAILED".format(func.__name__,self._outcome.result.result[-1][1]._testMethodName))
            elif self._outcome.result.result[-1][0] ==2:
                raise unittest.SkipTest("{} do not excute because prevtestcase <{}> is ERRORS".format(func.__name__,self._outcome.result.result[-1][1]._testMethodName))
            elif self._outcome.result.result[-1][0] ==3:
                raise unittest.SkipTest("{} do not excute because prevtestcase <{}> is SKIPPED".format(func.__name__,self._outcome.result.result[-1][1]._testMethodName))
            func(self,*args,**kwargs)
        return wrapper
    return decorator

def import_module_from_file(mode):
    '''通过py文件，动态引入模块'''
    module_path = sys.path[0]+'/'+mode     #获取测试模块的绝对路径（需要绝对路径）
    module_name = os.path.splitext(os.path.basename(module_path))[0]   #获取测试模块的名称，不含后缀
    module_spec = importlib.util.spec_from_file_location(module_name,module_path)  #返回模块的说明(第一个参数为模块名称，可以为空)

    if not module_spec is None:
        module = importlib.util.module_from_spec(module_spec)   #引入模块，返回引入的模块
        module_spec.loader.exec_module(module)      #引入后，要执行它
        # print(module)
        # print(type(module))
        # print(dir(module))
        return module
    return None

def function_log():
	'''打印函数日志'''
	def _test(func):
		@wraps(func)
		def __test(*args,**kw):
			logging.info('%s %s ...'%(func.__name__,func.__doc__))
			return func(*args,**kw)
			# logging.info('%s %s'%(func.__dict__['_testMethodName'],func.__dict__['_testMethodDoc']))
		return __test
	return _test
	
def get_className(mode):
    '''获取py文件下的测试用例类名'''
    name = []   #模块中可能有多个测试用例类，故保存为序列
    path = sys.path[0]+'/'+mode     #获取测试模块的绝对路径（需要绝对路径）
    with open(path,'rb') as file:
        pt = "unittest.TestCase"
        for i in file:
            i = i.decode('utf-8')
            if i.startswith('from') and 'unitBase' in i:
                pt = i.strip('\r\n').split(' ')
                # print(pt)
                try:
                    pt = pt[5]    #别名
                except:
                    pt = pt[3]    #原类名
                # print(pt)
            if i.startswith('class') and pt in i:
                i = i.split(' ')[1]
                i = i.split('(')[0]
                name.append(i)
    return name

def get_dir(path):
	'''根据相对路径，返回绝对路径'''
	# path为相对路径。上一级:'.',上二级:'..',上三级:'../..',上四级:'../../..'，依次类推
	return os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+path)


def grader_path():
	'''获取当前文件的前两级目录'''
	pwd = os.getcwd()
	grader_father=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
	return grader_father
	
def logging_out(logFilename):
    '''Output log to file and console'''
    #Define a Handler and set a format while output to file
    logging.basicConfig(
    level = logging.INFO,  #大于此级别的都被输出
    format= '%(asctime)s %(filename)-20s: [%(levelname)s] %(message)s',  #定义格式
    datefmt = '%Y-%m-%d %A %H:%M:%S',   #时间格式
    filename = logFilename, #log文件名
    filemode = 'a'
    )
	
def IsPortInUse(ip,port):
    """判断主机和远程端口是否被占用"""
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        #利用shutdown()函数使socket双向数据传输变为单向数据传输。shutdown()需要一个单独的参数，
        #该参数表示了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写。
        s.shutdown(2)
        return True
    except:
        return False
	
def run_test(suite,test_dir,ip,port,module_list,receivers):
    '''执行测试'''
    test_result_file = test_dir+'/test_result.html'
    with open(test_result_file,'wb') as fp:
        runner = HTMLTestRunner(stream = fp,title = "自动化测试报告",description="测试机：%s:%s   测试模块：%s"%(ip,port,str(module_list)))
        runner.run(suite)
    result = send_email(test_result_file,receivers)

    #unittest.TextTestRunner(verbosity=2).run(tests)  verbosity=2表示测试结果详细输出：https://www.jianshu.com/p/99ab2e4ca112
    
    if result:
        os.remove(test_result_file)
    logging.info('测试结束\n')	


def send_email(report_file,receivers):
    """---发送邮件---"""
    if not receivers:
	    return False	#如果接收邮件列表为空，则不发送邮件
    sender = "test_isli@163.com"
    receiver = ','.join(receivers)
    smtpserver = "smtp.163.com"
    #发送邮箱的账号密码,此处使用的是qq邮箱和第三方登录的授权码
    username = "test_isli@163.com"
    password = "a111111"

    #定义邮件正文
    file = open(report_file,"rb")
    mail_body = file.read()
    file.close()

    '''附件'''
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message["Subject"] = u"自动化测试报告"
    #添加正文
    message.attach(MIMEText(mail_body, _subtype="html", _charset="utf-8"))
    #添加附件
    att1 = MIMEApplication(open(report_file,'rb').read())
    att1.add_header('Content-Disposition', 'attachment', filename='test_result.html')
    message.attach(att1)

    #可以添加多份附件，像att1一样添加即可
    
    smtp = smtplib.SMTP_SSL("smtp.163.com")
    smtp.login(username, password)
    try:
        smtp.sendmail(sender, receiver, message.as_string())
        logging.info("Email has send out !")
    except:
        logging.info("Email has send failed !")
    smtp.quit()
    return True
  
	
def test_conf(td):
    """	对测试配置文件重新排列，按照用例模块来排列。
		接收一个字典dict={'http://172.16.7.34:5558/wd/hub': [('projects/mpr/testHome.py', 'firefox'), ..]}
		返回：[(mode,{'http://172.16.7.34:5555/wd/hub': DesiredCapabilities.CHROME}),...]
		且返回的该list，每个mode的ip都是一样的"""
    data_all = []
    for ip,items in td.items():   #items=[('projects/mpr/testHome.py', 'firefox'), ..]
        for mode,d in items:            #mode=  d='firefox'
            data = []   #[mode,devices]
            t_dict = {}
            t_dict[ip] = eval('DesiredCapabilities.%s'%d.upper())
            data.append(mode)
            data.append(t_dict)
            data_all.append(tuple(data))
    return data_all
	
def work_dir(path):
	'''切换工作目录'''
	os.chdir(path)
	