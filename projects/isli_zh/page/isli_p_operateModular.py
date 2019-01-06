from time import sleep
from selenium.webdriver.common.by import By
from base.pageBase import BasePage

class Module(BasePage):
	'''isli业务系统--操作'''
	homepage_loc = ('css selector','img[src="/mpr/resources/images/portal/logo.png"]')	#返回首页
	book_entry_loc = ('css selector','.book_entry')
	issu_entry_loc = ('css selector','.issu_entry')
	book_apply_loc = (By.ID,'4')
	book_manage_loc = (By.ID,'5')
	# audio_apply_loc = ('css selector','#10')
	audio_apply_loc = (By.ID,'10')				#css定位不到就用By方法
	audio_manage_loc = (By.ID,'12')
	issue_apply_loc = (By.ID,'6')
	issue_manage_loc = (By.ID,'7')
	news_apply_loc = (By.ID,'8')
	news_manage_loc = (By.ID,'9')
	addBookButton_loc = ('css selector','#addBookButton')	#申请ISLI按钮
	span_excel_loc = ('css selector','#span_excel')			#导出excel
	

	def homepage(self):
		'''进入首页'''
		self.find_element(self.homepage_loc).click()

	def book_audio_service(self):
		'''进入图书、音像制品关联服务'''
		self.find_element(self.book_entry_loc).click()
		
	def issue_news_service(self):
		'''进入连续出版物关联服务'''
		self.find_element(self.issu_entry_loc).click()
		
	def book_apply_list(self):
		'''图书申请列表'''
		self.find_element(self.book_apply_loc).click()
		
	def audio_apply_list(self):
		'''音像申请列表'''
		self.find_element(self.audio_apply_loc).click()
		
	def book_manage_list(self):
		'''图书管理列表'''
		self.find_element(self.book_manage_loc).click()
		
	def audio_manage_list(self):
		'''音像管理列表'''
		self.find_element(self.audio_manage_loc).click()
		
	def issue_apply_list(self):
		'''期刊申请列表'''
		self.find_element(self.issue_apply_loc).click()
		
	def news_apply_list(self):
		'''报纸申请列表'''
		self.find_element(self.news_apply_loc).click()
		
	def issue_manage_list(self):
		'''期刊管理列表'''
		self.find_element(self.issue_manage_loc).click()
		
	def news_manage_list(self):
		'''报纸管理列表'''
		self.find_element(self.news_manage_loc).click()
		
	def apply_isli(self):
		'''申请ISLI按钮'''
		self.find_element(self.addBookButton_loc).click()
		
	def span_excel(self):
		'''导出excel'''
		self.find_element(self.span_excel_loc).click()

			
	
        

    
if __name__ =="__main__":
    pass