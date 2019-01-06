import os,sys,time,logging
import unittest
from base.unitBase import ParametrizedTestCase as pt
from base import function

sys.path.append('%s/projects'%sys.path[0])   #将projects添加到系统变量中

def main(module_dir):
    """基本设置
        ip:本机ip地址，测试机为本机"""
    
    #如果临时文件目录不存在，则创建临时文件目录
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        
    #设置日志文件目录
    function.logging_out(test_dir+'/logInfo.log') 
    logging.info('开始本轮测试：%s'%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    
    #创建测试节点（指定测试用例模块。若要修改浏览器，请在base/unitBase.py中第22行修改）
    devices = {'http://0.0.0.0:5555/wd/hub': [(module_dir, 'chrome')]}
    
    #执行该节点的测试工作
    sample_request(devices)
  

def sample_request(devices):
    """ 为该节点解析出测试套件（测试套件来自测试类的测试用例集合），并执行测试
        如：devices：{'http://172.16.7.34:5555/wd/hub': [('projects/isli/case/RAlogin.py', 'chrome')]}
        表示执行机 172.16.7.34 执行用例模块 projects/isli/case/RAlogin.py
    """
    suite = unittest.TestSuite()
    mode_list = function.test_conf(devices)
    ip,port = tuple(devices)[0].split('//')[1].split('/')[0].split(':')
    module_list = []    #传递到测试结果
    
    #通过循环测试用例模块，为每个测试机准备测试套件
    for mode,devices in mode_list:
        module_list.append(mode)

        #动态引入模块
        module = function.import_module_from_file(mode) 
        if not module is None: 
            #读取模块中的测试用例
            suite.addTest(get_suite_from_module(module,mode,devices))

    #开始测试
    function.run_test(suite,test_dir,ip,port,module_list,receivers)


def get_suite_from_module(module,mode,devices):
    '''读取模块中的测试用例'''
    suite = unittest.TestSuite()
    classnames = function.get_className(mode)
    class_name = classnames[0]  #读取第一个用例类名称，为字符串
    if hasattr(module,class_name): #如果有该属性值(类)
        _class = getattr(module,class_name)    #获取这个类
        suite.addTest(pt.parametrize(_class,driver=devices,remote=False))   #为本地调试模式
    return suite  

if __name__== '__main__':
    """ 
        该脚本用于本地调试脚本
        test_dir  保存临时调试文件，如日志，测试报告(若发送了邮件，测试报告会被自动删除)
        receivers 邮件接收者，序列类型,若为空（receivers=[]）则不发送邮件
        mode_dir  为你需要调试的测试类脚本目录 注意不可丢失前缀./projects
    """

    test_dir = r'D:/TEST_CASE/local_test'   #临时文件保存路径

    #receivers = ["shigx@mpreader.com"]
    receivers = []  #不发送邮件
    
    #要调试的用例文件
    mode_dir = r'./projects/isli_zh/isli_m_operate.py'  
    
    main(mode_dir)