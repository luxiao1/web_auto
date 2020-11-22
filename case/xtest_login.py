from selenium import webdriver
from pages.login_page import Loginpage,locgin_url
import time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.longinp = Loginpage(cls.driver)

    def setUp(self):
        self.driver.get(locgin_url)
        self.driver.maximize_window()
        self.longinp.is_alert()

    def test_01(self):
        '''登陆成功：输入账号、密码，点击登陆'''
        self.longinp.input_user('admin')
        self.longinp.input_psw('Li@12345')
        self.longinp.click_login_button()
        result = self.longinp.get_login_user()
        self.assertTrue(result == 'admin')

    def test_02(self):
        '''登陆失败：输入账号，点击登陆'''
        self.longinp.input_user('admin')
        self.longinp.click_login_button()
        result = self.longinp.get_login_user()
        self.assertTrue(result == '')

    def test_03(self):
        '''登陆成功：输入账号、密码、点击保持登陆、点击登陆'''
        self.longinp.input_user('admin')
        self.longinp.input_psw('Li@12345')
        self.longinp.click_keep_login()
        self.longinp.click_login_button()
        result = self.longinp.get_login_user()
        self.assertTrue(result == 'admin')

   # def test_04(self):
     #   self.longinp.click_forget_psw()
      #  result = self.longinp.is_forget_page()
      #  self.assertTrue(result == '普通用户请联系管理员重置密码')

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__  == '__main__':
    unittest.main()