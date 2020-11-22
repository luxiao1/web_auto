from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

class Base():
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findelementNew(self,locator):
        '''判断方法，定位到元素，返回元素对象，没定位到Timeout异常'''
        element = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return element

    def findelement(self,locator):
        if not isinstance(locator, tuple):
            print("locator参数类型错误，必须传元组类型：loctor = ('id','value')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            element = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return element

    def findelements(self,locator):
        '''定位一组元素'''
        try:
            elements = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_elements(*locator))
            return elements
        except:
            return []

    def sendKeys(self,locator,text):
        element = self.findelement(locator)
        element.send_keys(text)

    def click(self,locator):
        element = self.findelement(locator)
        element.click()

    def clear(self,locator):
        element = self.findelement(locator)
        element.clear()

    def get_text(self, locator):
        try:
            t = self.findelement(locator).text
            return t
        except:
            print('获取text失败')
            return ''

    def get_attribute_(self, locator):
        try:
            element = self.findelement(locator)
            e =element.get_attribute('value')
            print(e)
        except:
            print("获取attribute失败")

    def is_title(self, _title):
        '''判断当前页面的title是否和预期字符串相等，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title):
        '''判断当前页面的title是否包含预期字符串，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text):
        '''判断元素中的text是否包含了预期字符串，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_alert_present(self):
        '''判断页面是否有alert，有返回alert(注意这里是返回alert,不是True)没有返回False'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def isSelected(self,locator):
        '''判断元素是否被选中，返回BOOL值'''
        element = self.findelement(locator)
        r = element.is_displayed()
        return r

    def isElementExist(self,locator):
        '''判断元素是否存在'''
        try:
            element = self.findelement(locator)
            return True
        except:
            return False

    def isElementExist2(self,locator):
        '''判断一组元素'''
        elements = self.findelements(locator)
        n = len(elements)
        if n ==0:
            return False
        elif n==1:
            return True
        else:
            print("定位到元素的个数：%s" %n)
            return True




    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        element = self.findelement(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def select_by_index(self, locator, index=0):
        '''通过索引,index是索引第几个，从0开始，默认选第一个'''
        element = self.findelement(locator)  # 定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element = self.findelement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.findelement(locator)
        Select(element).select_by_visible_text(text)

    def js_focus_element(self, locator):
        '''聚焦元素,滚动到元素出现的位置'''
        target = self.findelement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''回到顶部'''
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)

    def js_scroll_end(self,x=0):
        '''滚动到底部'''
        js = "window.scrollTo(%s, document.body.scrollHeight)"%x
        self.driver.execute_script(js)


