import unittest
from HTMLTestRunner import HTMLTestRunner
import os
from test_case.unitt import oxcase
from jiekou.main import MyTestCase

s = unittest.TestSuite()
s.addTest(oxcase('test_1'))
# s.addTest(MyTestCase("test_01"))
unittest.TestLoader()
s.addTest(unittest.TestLoader().loadTestsFromTestCase(MyTestCase))
# s.addTest(loader.loadTestsFromTestCase(oxcase))
di = r'F:\接口和ui一体自动化\work\report'
report_file = di + r'\report2.html'
if not os.path.exists(di):
    os.mkdir(di)
else:
    pass
# t = TextTestRunner()  # 调用执行套件方法
# t.run(s)  # 执行套件
fp = open(report_file, 'wb')
text = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"测试结果如下")
text.run(s)
fp.close()