from selenium import webdriver
from pages.login_page import Loginpage,locgin_url
import time
import unittest,ddt
from common.read_excel import ExcleUnil
import os

#获取当前路径上一层的上一层目录
webpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath = os.path.join(webpath,'common','datas.xlsx')
print(filepath)

#filepath = "D:\\Web_project\\common\\datas.xlsx"
data = ExcleUnil(filepath)
testdates = data.dict_data()
print(testdates)

@ddt.ddt()
class LoginTest(unittest.TestCase):
    '''用户登陆'''
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
        print("测试数据 %s" %data)
        self.login_case(data['user'],data['psw'],data['expect'])


    def tearDown(self):
        self.longinp.is_alert()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__  == '__main__':
    unittest.main()