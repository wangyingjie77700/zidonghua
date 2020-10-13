from selenium.webdriver.common.by import By
from time import  sleep
from test_object.login import loging
from common.logger import log
log = log()
class shenpiliucheng(loging):
    el = (By.XPATH, '//*[@id="inputUserName"]')
    el1 = (By.XPATH, '//*[@id="inputPassword"]')
    el2 = (By.XPATH, '//*[@id="btnLogin"]')
    el3 = (By.XPATH, '// *[ @ id = "portalDropdown"] / span')

    el4 = (By.XPATH, '//*[@id="portalDropdown"]/ul/li[3]/a') #选择部门事项管理元素
    el5 = (By.XPATH, '// *[ @ id = "outAndOver"][6]')

    el6 = (By.XPATH, '// *[ @ id = "add"]')
    el7 =(By.XPATH, '//*[@id="sgItem11111111111111111"]/div[5]/div/div[2]/div/span/span')
    el8 =(By.XPATH, '// *[ @ id = "sgItem11111111111111111111111111111111111111111111111111111111111"] / div[5] / div / div[2] / div / input')

    def sp_input(self,locator,text):
        self.text_input(locator, text)   #调用父类text_input方法
    def sp_click(self,locat):
        self.locats(locat).click()

    def shenpi(self):
        self.sp_input(self.el, "032749")
        log.info("输入账号032749")
        self.sp_input(self.el1, "111")
        log.info("输入密码111")
        self.sp_click(self.el2)
        log.info("点击登录按钮")
        self.sp_click(self.el3)
        self.sp_click(self.el4)
        log.info("选择部门事项管理员")
        self.sp_click(self.el5)
        log.info("选择事项要素维护")
        self.sp_click(self.el6)
        log.info("新增事项")

        # self.sp_input(self.el8,"行政许可")







