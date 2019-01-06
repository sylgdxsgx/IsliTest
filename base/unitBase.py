
import unittest
from selenium import webdriver

class ParametrizedTestCase(unittest.TestCase):
    glb_driver = None
    glb_remote = None
    def __init__(self,methodName='runTest',driver=None,remote=False):
        super(ParametrizedTestCase,self).__init__(methodName)
        ParametrizedTestCase.glb_driver = driver		#传递驱动
        ParametrizedTestCase.glb_remote = remote		#传递运行方式（远程/本地）
    
    # def setUp(self):
        # if self.glb_remote:
            # self.driver = PTestCase.glb_driver
        # else:
            # self.driver = webdriver.Chrome()

    # def tearDown(self):
        # self.driver.close()
        
    @classmethod
    def setUpClass(self):
        if self.glb_remote:
            self.driver = ParametrizedTestCase.glb_driver	#远程执行,driver配置来自function
        else:
            # options = webdriver.ChromeOptions()
            # options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
            # self.driver = webdriver.Chrome(chrome_options=options)  	#本地调试时使用	
            self.driver = webdriver.Chrome()
            # profileDir = "C:\\Users\\shigx1219\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\phugd9za.default"
            # profile = webdriver.FirefoxProfile(profileDir)
            # self.driver = webdriver.Firefox(profile)  	#本地调试时使用	
            # self.driver = webdriver.Firefox()  	#本地调试时使用	
        
		
    @classmethod
    def tearDownClass(self):
        self.driver.close()  #关闭当前的浏览器窗口。若关闭驱动，退出WedDriver则用：self.driver.quit()

    @staticmethod
    def parametrize(testcase_klass,driver=None,remote=False):
        """该方法接收一个类，返回该类下的所有测试用例的测试集合"""
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name,driver=driver,remote=remote))
        return suite