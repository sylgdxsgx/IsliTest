from time import sleep
from selenium.webdriver.common.by import By
from base.pageBase import BasePage

class Book_Module(BasePage):
	'''isli业务系统--登入操作'''
	isbn1_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[5]/input[1]')
	isbn2_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[5]/input[2]')
	isbn3_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[5]/input[3]')
	isbn4_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[5]/input[4]')
	isbn5_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[5]/input[5]')
	isbn6_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[6]/input[1]')
	isbn7_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[6]/input[2]')
	isbn8_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[6]/input[3]')
	isbn9_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[6]/input[4]')
	isbn10_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[6]/input[5]')

	bookNameCn_loc = (By.NAME,'bookNameCn')						#书名
	bookNamePinyin_loc = (By.NAME,'bookNamePinyin')				#拼音
	seriesName_loc = (By.NAME,'seriesName')								
	setsName_loc = (By.NAME,'setsName')

	productType_loc = (By.NAME,'productType')					#产品形式
	editing_loc = (By.NAME,'editing')							#责任编辑
	clcId_comb_loc = (By.XPATH,'//*[@id="s2id_autogen1"]/a/span[1]')		#中图分类法
	clcId_input_loc = (By.XPATH,'//*[@id="select2-drop"]/div/input')
	clcId_result_loc = (By.XPATH,'//*[@id="select2-drop"]/ul/li[1]/div')	#输入编号，此处读取第一个结果
	langId_loc = (By.NAME,'langId')											#语种
	publishCountry_loc = (By.NAME,'publishCountry')							#出版地
	author_loc = (By.NAME,'author')											#著作者
	publishing_loc = (By.NAME,'publishing')
	pulpwood_loc = (By.NAME,'pulpwood')
	printSum_loc = (By.NAME,'printSum')
	pages_loc = (By.NAME,'pages')				#页数
	wordage_loc = (By.NAME,'wordage')			#字数
	printerSum1_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[23]/div[1]/input[1]')
	printerSum2_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[23]/div[1]/input[2]')
	
	publishingDate_loc = (By.NAME,'publishingDate')					#出版日期
	iframe_date_loc = (By.XPATH,"//iframe[@hidefocus='true']")
	today_loc = (By.ID,'dpTodayInput')
	produceDate_loc = (By.NAME,'isliProduceDate')					#制作时间
	keywords_loc = (By.NAME,'keywords')
	mapSum_loc = (By.NAME,'mapSum')
	publishingFlag_loc = (By.NAME,'publishingFlag')
	printer_loc = (By.NAME,'printer')
	version_loc = (By.NAME,'version')
	versionType_loc = (By.NAME,'versionType')						
	category_loc = (By.NAME,'category')
	source_loc = (By.NAME,'source')
	bookformat_loc = (By.NAME,'bookformat')
	authority_loc = (By.NAME,'authority')
	publicationContentSummary_loc = (By.NAME,'publicationContentSummary')
	#版次
	editionCount_year_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[25]/input[1]')
	editionCount_month_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[25]/input[2]')
	editionCount_count_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[25]/input[3]')
	#印次
	printerCount_year_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[26]/input[1]')
	printerCount_month_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[26]/input[2]')
	printerCount_count_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[26]/input[3]')
	#开本
	format_1_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[27]/input[1]')
	format_2_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[27]/input[2]')
	format_3_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[27]/input[3]')

	cip_1_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[28]/input[1]')
	cip_2_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[28]/input[2]')

	price_loc = (By.XPATH,'//*[@id="dataForm"]/ul/li[29]/input')


	def isbn(self,n1,n2,n3,n4):
		'''*ISBN'''
		self.find_element(self.isbn1_loc).click()
		self.find_element(self.isbn1_loc).clear()
		self.find_element(self.isbn1_loc).send_keys(n1)
		self.find_element(self.isbn2_loc).click()
		self.find_element(self.isbn2_loc).clear()
		self.find_element(self.isbn2_loc).send_keys(n2)
		self.find_element(self.isbn3_loc).click()
		self.find_element(self.isbn3_loc).clear()
		self.find_element(self.isbn3_loc).send_keys(n1)
		self.find_element(self.isbn4_loc).click()
		self.find_element(self.isbn4_loc).clear()
		self.find_element(self.isbn4_loc).send_keys(n2)
		self.find_element(self.isbn5_loc).click()
		self.find_element(self.isbn5_loc).clear()
		self.find_element(self.isbn5_loc).send_keys(n2)

	def isbn_old(self,n1,n2,n3,n4,n5):
		'''原ISNB'''
		self.find_element(self.isbn6_loc).click()
		self.find_element(self.isbn6_loc).clear()
		self.find_element(self.isbn6_loc).send_keys(n1)
		self.find_element(self.isbn7_loc).click()
		self.find_element(self.isbn7_loc).clear()
		self.find_element(self.isbn7_loc).send_keys(n2)
		self.find_element(self.isbn8_loc).click()
		self.find_element(self.isbn8_loc).clear()
		self.find_element(self.isbn8_loc).send_keys(n1)
		self.find_element(self.isbn9_loc).click()
		self.find_element(self.isbn9_loc).clear()
		self.find_element(self.isbn9_loc).send_keys(n2)
		self.find_element(self.isbn10_loc).click()
		self.find_element(self.isbn10_loc).clear()
		self.find_element(self.isbn10_loc).send_keys(n2)


if __name__ =="__main__":
	pass