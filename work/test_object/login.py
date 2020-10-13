from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from common.logger import log

log = log()
class loging(object):
    def __init__(self, url, browse):
        self.driver_browse(browse)
        log.info("打开浏览器")
        self.driver.get(url)
        log.info("打开url")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        # self.driver.quit()

    # 选择浏览器
    def driver_browse(self, browse):
        if browse == 'cc':
            self.driver = webdriver.Chrome()
        elif browse == 'ff':
            self.driver = webdriver.Firefox()
        elif browse == 'ie':
            self.driver = webdriver.Ie()

    # 元素定位
    def locats(self, locator):  # 这里的参数loactor传入的是一个元祖
        # （一个元祖就是一个参数，而不是元祖里一个元素就是一个参数）
        li = self.driver.find_element(*locator)  # 这里的*作用是解析，跟ddt的@unpage一样
        return li

    def Select(self,locat,value):
        Select(self.driver.find_element_by_id(locat)).select_by_value(value)

        # 文本输入
    def text_input(self, locator, text):
        li = self.locats(locator)
        li.send_keys(text)

    # 文本清空
    def text_clear(self, locator):
        li = self.locats(locator)
        li.clear()

    # 元素点击
    def click_element(self, locator):
        li = self.locats(locator)
        li.click()

    # 关闭浏览器
    def driver_quite(self):
        self.driver.quit()

    # 等待
    def driver_sleep(self, text):
        sleep(text)

    def driver_wait(self, locator):
        WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locats(locator), message="没找到")

    # 界面切换
    def element_ifram(self):
        self.driver.switch_to.frame()

    def browes_hands(self):
        hands = self.driver.window_handles
        self.driver.switch_to.window(hands[1])

    # 断言
    def element_urltry(self, locator):
        try:
            self.locats(locator)
            print("购物车加入成功")
        except Exception as e:
            print(e)
            print("购物车加入失败")

    # def element_text(self, locator):
    #     v = self.locats(locator)
    #     v.text
    #     return v
    #
    # def driver_access(self, locator, text):
    #     v = self.element_text(locator)
    #     if v != text:
    #         print("加入购物车失败")
    #     else:
    #         print("购物车加入成功")
