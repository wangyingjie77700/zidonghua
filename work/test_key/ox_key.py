from test_object.login import loging
from selenium.webdriver.common.by import By
from time import  sleep


class oxshoping(loging):
    
    # 登录
    el = (By.XPATH,'//*[@id="inputUserName"]')
    el1 = (By.XPATH,'//*[@id="inputPassword"]')
    el2 = (By.XPATH,'//*[@id="btnLogin"]')
    el3= (By.XPATH, '//*[@id="//*[@/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/h4"]')
    el4 = (By.XPATH, '// *[ @ id = "824436438342660096"] / td[16] / div / button')
    el5 = (By.XPATH, '// *[ @ id = "outAndOver"] / a')

    def ox_click(self,locator):
        self.locats(locator).click()
    # 输入
    def ox_input(self,locator,text):
        self.text_input(locator,text)
    def ox_clear(self,locator):
        self.text_clear(locator)
    #窗口切换
    def ox_hands(self):
        self.browes_hands()

    #等待
    def ox_sleep(self,text):
        self.driver_sleep(text)
    def ox_login(self):

        #登录
        self.ox_input(self.el,"032749")
        self.ox_input(self.el1,"111")
        # self.ox_click(self.el3)
        # #搜索
        # self.ox_input(self.el4,"苹果")
        # self.ox_click(self.el5)
        # # l.driver_wait(el6)
        # # print("显示等待已完成")
        self.ox_click(self.el2)
        sleep(5)
        # self.ox_click(self.el3)
        # sleep(5)
        # self.ox_click(self.el4)
        # sleep(5)
        self.ox_click(self.el5)



