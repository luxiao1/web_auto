from selenium import webdriver
from common.base import Base
import time
class Add_bug_page(Base):

    #添加bug
    loc4 = ('link text','测试')
    loc5 = ('xpath','//*[@data-id="bug"]')
    loc6 = ('xpath','//*[@class="btn btn-primary"]/i')
    loc7 = ('xpath',"//*[@id='openedBuild_chosen']/ul/li/input")
    loc8 = ('xpath','//li[@title="主干"]')
    loc_title = ('id','title')
    #需切换iframe
    loc_input_message = ('class name','article-content')
    loc_save = ('id','submit')
    #新增的list标题
    loc_newlist = ('xpath',"//*[@id='bugList']/tbody/tr[1]/td[5]/a")

    def add_bug(self,title='添加BUG',text='bug复现步骤'):
        self.click(self.loc4)
        self.click(self.loc5)
        self.click(self.loc6)
        self.click(self.loc7)
        self.click(self.loc8)
        self.sendKeys(self.loc_title, title)
        self.driver.switch_to.frame(0)
        self.sendKeys(self.loc_input_message, text)
        self.driver.switch_to.default_content()
        self.click(self.loc_save)

    def is_add_bug_sucess(self,text='添加BUG'):
        '''获取新增的bug标题'''
        t = self.is_text_in_element(self.loc_newlist,text)
        return t

if __name__ == '__main__':
    driver = webdriver.Chrome()
    a = Add_bug_page(driver)
    from pages.login_page import Loginpage
    l = Loginpage(driver)
    l.login()
    a.add_bug()
    result = a.is_add_bug_sucess()
    print(result)

