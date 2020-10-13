from test_key.ox_key import oxshoping
from selenium.webdriver.common.by import By


class search(oxshoping):
    # 购物车
    el7 = (By.XPATH, '//*[@id="inputUserName"]')
    el8 = (By.XPATH, '//*[@id="inputPassword"]')
    el9 = (By.XPATH, '//*[@id="btnLogin"]')
    el10 = (By.XPATH, '//input[@id="text_box"]')
    el11 = (By.XPATH, '//button[@title="加入购物车"]')
    el12 = (By.XPATH, '//span[contains(text(),"购物车")]')
    # 断言
    el13 = (By.XPATH, '//a[@class="goods-title"]')
    def ox_search(self):
        # 加入购物车
        self.ox_login()
        self.ox_hands()
        self.ox_click(self.el7)
        self.ox_sleep(1)
        self.ox_click(self.el8)
        self.ox_sleep(1)
        self.ox_click(self.el9)
        self.ox_clear(self.el10)
        self.ox_input(self.el10, "10")
        self.ox_click(self.el11)
        self.ox_click(self.el12)
        self.element_urltry(self.el13)
        self.driver_quite()


