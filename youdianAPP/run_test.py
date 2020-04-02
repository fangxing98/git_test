import unittest
import os
from common.handlepath import CASEDIR,REPORTDIR
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.handle_email import send_email
from BeautifulReport import BeautifulReport

import datetime


date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")


# 第一步：创建套件
suite = unittest.TestSuite()

# 第二步：加载用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR))

# report_file = os.path.join(REPORTDIR,date+"report1.html")

# 第三步：执行用例
# runner = HTMLTestRunner(stream=open(report_file, "wb"),
#                         description="星链友店app自动化测试结果",
#                         title="星链友店app自动化测试结果",
#                         tester="方兴"
#                         )
#
# runner.run(suite)

br = BeautifulReport(suite)

br.report("星链友店app", filename=date+"report.html", report_dir=REPORTDIR)

# send_email(report_file,"py26测试报告最终版")


