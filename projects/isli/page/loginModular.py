import sys,time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from projects.isli.page.base import Page
from time import sleep

class loginModular(Page):
    '''官网--登入操作'''
    url = r'http://172.16.3.52:8080/irap/web/navigation/toNavigationPage/1'
    username_loc = ('css selector','#username')
    password_loc = ('css selector','#password')
    codecon_loc = ('css selector','#vcode')                                         #验证码
    refreshCode_loc = ('css selector', 'span>#image')                               #刷新验证码
    login_btn_loc = ('css selector','[value="登入"]')
    login_loc = ('css selector','.men')
    login_popup_loc = ('css selector','.login_enter')								 #登入窗口弹窗
    error_hint_loc = (By.CSS_SELECTOR,'#error')                                     #登入错误提示
    login_success_loc = (By.CSS_SELECTOR, '')
    sp_title_loc = ('css selector','.header>p')                                     #SP登入成功检查点
    LC_title_loc = ('css selector','[title="中国ISLI注册中心-管理系统"]')

    def get_LCtitle(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url
        # return self.find_element(self.sp_title_loc).text()

    def swit_haead(self,num):
        time.sleep(2)
        hand =self.driver.window_handles
        self.driver.switch_to_window(hand[int(num)])

    def get_hand(self):
        return self.driver.window_handles


    def click_action(self):
        self.find_element(self.login_loc).click()
		
    def login_popup(self):
	    self.click_action()
	    try:
	        WebDriverWait(self.driver,10,1,'invisible').until(EC.visibility_of(self.driver.find_element(*self.login_popup_loc)),'none')
	        return True
	    except:
		    err = 'invisible'
		    logging.info('点击登入无弹窗')
		    return err
			
    def login_username(self,username):
        '''输入用户名'''
        self.find_element(self.username_loc).clear()
        self.find_element(self.username_loc).send_keys(username)

    def login_password(self,password):
        '''输入密码'''
        self.find_element(self.password_loc).clear()
        self.find_element(self.password_loc).click()
        sleep(0.5)
        self.find_element(self.password_loc).send_keys(password)

    def login_codecon(self,codecon='8888'):
        '''输入验证码'''
        self.find_element(self.codecon_loc).clear()
        self.find_element(self.codecon_loc).send_keys(codecon)

    def login_button(self):
        '''点击登入btn'''
        self.find_element(self.login_btn_loc).click()

    def user_login(self,username='username',password='password',codecon='codecon'):
        '''登入--有点不解'''
        # self.open()  #若是有他，则每次调用该函数都会刷新页面
        self.login_username(username)
        self.login_password(password)
        self.login_codecon(codecon)
        self.login_button()
        sleep(0.5)

    def user_login_verify(self,username='',password='',codecon=''):
        '''输入项为空登入'''
        self.user_login(username,password,codecon)


    def error_hint(self):
        '''获取登入错误提示'''
        return self.find_element(self.error_hint_loc).text
        

    
if __name__ =="__main__":
    pass