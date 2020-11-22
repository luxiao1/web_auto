from selenium import webdriver
from pages.login_page import Loginpage,locgin_url
import time
import unittest,ddt


testdates = [{'user':'admin','psw':'Li@12345','expect':'admin'},
             {'user':'admin','psw':'','expect':''},
             {'user':'admin123','psw':'1234','expect':''}]

@ddt.ddt()
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.longinp = Loginpage(cls.driver)
        cls.driver.get(locgin_url)

    def setUp(self):
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def login_case(self,user,psw,expect):
        self.longinp.login(user,psw)
        result = self.longinp.get_login_user()
        print("获取的登陆用户名 %s" % result)
        self.assertTrue(result == expect)

    @ddt.data(*testdates)
    def test_01(self,data):
        '''输入正确的账号、正确的密码，点击登陆'''
        print("测试数据 %s" %data)
        self.login_case(data['user'],data['psw'],data['expect'])


    def tearDown(self):
        self.longinp.is_alert()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__  == '__main__':
    unittest.main()