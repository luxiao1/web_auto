import unittest
from common import HTMLTestRunner_cn

#用例路径
casePath ="D:\web_project\\case"

#测试用例匹配规则
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

#报告路径
reportPath = "D:\\web_project\\report\\"+"result.html"
fp =open(reportPath,"wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                       title="自动化测试报告",
                                       description="测试报告的描述",
                                       retry=1) #retry失败重跑的次数
runner.run(discover)

fp.close()