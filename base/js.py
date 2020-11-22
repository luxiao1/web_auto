from selenium import webdriver
import time
from pages.login_page import Loginpage
driver = webdriver.Chrome()
l = Loginpage(driver)
l.login()

document.getElementById('account').value='admin';
document.getElementsByName('password')[0].value='Li@12345';
document.getElementById('submit').click();

#处理富文本
js = "document.getElementsByClassName('ke-edit-iframe')[0].contentWindow.document.body.innerHTML='hello world'"
driver.execute_script(js)