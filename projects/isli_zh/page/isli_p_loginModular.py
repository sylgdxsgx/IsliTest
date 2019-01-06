from time import sleep
from base.pageBase import BasePage

class Module(BasePage):
    '''isli业务系统--登入操作'''
    base_url = r'https://172.16.5.25:18400/mpr/portal-mcrs-publisher/mvc/publisher/toLogin'
    username_loc = ('css selector','#userName')
    password_loc = ('css selector','#passWord')
    codecon_loc = ('css selector','#codeCon')                                         #验证码
    refreshCode_loc = ('css selector', '#validCodeImg')                               #刷新验证码
    login_btn_loc = ('css selector','.btn')												#登入按钮
    login_error_tips_loc = ('css selector', '#error_tips')
    login_error_errorUserName_loc = ('css selector','#errorUserName')
    login_error_errorPassWord_loc = ('css selector','#errorPassWord')
    login_error_errorCodeCon_loc = ('css selector','#errorCodeCon')



			
    def login_username(self,username):
        '''输入用户名'''
        self.find_element(self.username_loc).clear()
        self.find_element(self.username_loc).send_keys(username)

    def login_password(self,password):
        '''输入密码'''
        self.find_element(self.password_loc).clear()
        self.find_element(self.password_loc).click()
        # sleep(0.5)
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

    def error_tips(self):
        '''用户名或者密码错误提示'''
        return self.find_element(self.login_error_tips_loc).text
		
    def error_username(self):
        '''用户名提示语'''
        return self.find_element(self.login_error_errorUserName_loc).text
		
    def error_pwd(self):
        '''密码校验错误提示'''
        return self.find_element(self.login_error_errorPassWord_loc).text
		
    def error_codecon(self):
        '''验证码提示语'''
        return self.find_element(self.login_error_errorCodeCon_loc).text
        

    
if __name__ =="__main__":
    pass