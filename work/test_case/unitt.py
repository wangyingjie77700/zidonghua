import unittest
from test_key.ox_key import oxshoping
from test_key.ox_search import search
from time import  sleep
from test_key.shenpiliucheng import shenpiliucheng
from selenium.webdriver.common.by import By
class oxcase(unittest.TestCase):
    el2 = (By.XPATH, '//*[@id="1"]/td[3]')
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_1(self):
        l = shenpiliucheng('http://124.225.222.184:90/xzsp/mainmanager.html', 'cc')
        l.shenpi()
        ss=l.locats(self.el2).text
        self.assertEqual(ss,'测试内容',"不一致")

if __name__ == '__main__':
    unittest.main()
