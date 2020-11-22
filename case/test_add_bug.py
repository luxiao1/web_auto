import unittest,time
from selenium import webdriver
from pages.login_page import Loginpage
from pages.add_bug_page import Add_bug_page


class Add_bugcase(unittest.TestCase):
    '''新增Bug'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.add = Add_bug_page(cls.driver)
        cls.l = Loginpage(cls.driver)
        cls.l.login()

    def test_add_bug(self):
        '''新增一个Bug'''
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = '添加BUG' + timestr
        self.add.add_bug(title)
        result = self.add.is_add_bug_sucess(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__  == '__main__':
    unittest.main()


