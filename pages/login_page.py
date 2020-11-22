from selenium import webdriver
from common.base import Base
import time
locgin_url = 'http://59.110.48.193/zentaopms/www/index.php'
class Loginpage(Base):
    # 定位登陆
    loc_user = ('id', 'account')
    loc_psw = ('name', 'password')
    loc_button = ('id', 'submit')
    loc_keep = ('id','keepLoginon')
    loc_forget_psw = ('link text','忘记密码')

    loc_get_user = ('css selector','.user-name')
    loc_forger_page = ('xpath',"//*[@class = 'alert alert-info']/h5[1]")

    def input_user(self,user):
        self.sendKeys(self.loc_user,user)

    def input_psw(self,psw):
        self.sendKeys(self.loc_psw,psw)

    def click_login_button(self):
        self.click(self.loc_button)

    def click_keep_login(self):
        self.click(self.loc_keep)

    def click_forget_psw(self):
        self.click(self.loc_forget_psw)

    def get_login_user(self):
        '''获取登陆后的账号名'''
        user= self.get_text(self.loc_get_user)
        return user

    def get_login_result(self,user):
        result = self.is_text_in_element(self.loc_get_user,user)
        return result

    def is_alert(self):
        '''判断alert是否存在，如果存在点击确定'''
        a = self.is_alert_present()
        if a:
            print(a.text)
            a.accept()
    def is_forget_page(self):
        '''判断忘记密码页面，某个字段是否存在'''
        r = self.get_text(self.loc_forger_page)
        return r

    def login(self,user='admin',psw='Li@12345'):
        '''登陆方法'''
        self.driver.get(locgin_url)
        self.input_user(user)
        self.input_psw(psw)
        self.click_login_button()


#只在当前脚本执行，其他模块调用的时候不执行该代码
if __name__ == '__main__':
    driver = webdriver.Chrome()
    longin_page = Loginpage(driver)
    longin_page.login()








