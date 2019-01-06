说明：

1. base目录为公共基础脚本
	addSysPath.py	#添加路径到系统路径下（目前废弃了）
	testBase.py		#unittest测试框架的配置项 (配置驱动driver和创建测试套件)，
					#测试用例类使用unittest框架，会继承该模块里的ParametrizedTestCase类
	function.py		#一些函数功能
    basePage.py     #页面操作的封装类

2. projects目录存放各个项目，不同的项目用不同的目录，如：
		--projects		
		    --isli	（isli项目）
				--case
				--common
				--date
				--page
		    --isli_zh	（中国isli项目）
		    --mpr		（中国mpr项目）

3. test.bak 目录为备份目录(文件夹已保存到svn_copy/ISLITest.bak目录)
4. HTMLTestRunner.py 文件生成测试报告
5. manage.py 文件为分布式测试主文件
6. manage_local.py 文件为本地调试主文件