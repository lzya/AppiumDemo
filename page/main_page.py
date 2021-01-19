from time import sleep
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.search_page import SearchPage


class MainPage(BasePage):


    _iv_close = (By.ID, "iv_close")
    def close(self):
        """
        首页广告弹框
        :return:
        """
        self.find_element(self._iv_close).click()
        return self

    _academic_circle_search = (By.ID, "academic_circle_search")
    # _home_search = (By.ID, "home_search") [xueqiu]
    def to_search(self):
        sleep(2)
        # self.find_element(self._home_search).click()  # 点击按钮进入主搜索[xueqiu]
        self.find_element(self._academic_circle_search).click()  # [dxy]

        return SearchPage(self.driver)
        # return self

