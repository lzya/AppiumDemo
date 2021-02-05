from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.mine_page import MinePage
from page.post_publish_center_title_page import PostPublishCenter
from page.search_page import SearchPage


class MainPage(BasePage):

    _iv_close_upgrade = (By.ID, "iv_close")
    def close_upgrade(self):
        """
        处理升级弹框
        :return: self
        """
        for i in range(2):
            try:
                self.find_element(self._iv_close_upgrade).click()
                WebDriverWait(self.driver, 1, 0.5).until(expected_conditions.
                                                         presence_of_element_located(self._iv_close_upgrade)).click()
            except:
                pass
        return self


    _iv_close = (By.ID, "iv_close")
    def close(self):
        """
        关闭首页广告弹框 & 升级弹框
        :return:
        """
        # self.find_element(self._iv_close).click()
        for i in range(2):
            try:
                # self.find_element(self._iv_close_upgrade).click()
                WebDriverWait(self.driver, 1, 0.5).until(expected_conditions.
                                                         presence_of_element_located(self._iv_close)).click()
            except:
                pass
        return self

    _academic_circle_search = (By.ID, "academic_circle_search")
    # _home_search = (By.ID, "home_search") [xueqiu]
    def to_search(self):
        """
        进入搜索页
        :return: SearchPage 搜索页的对象
        """
        sleep(2)
        # self.find_element(self._home_search).click()  # 点击按钮进入主搜索[xueqiu]
        self.find_element(self._academic_circle_search).click()  # [dxy]

        return SearchPage(self.driver)
        # return self

    _to_mine = (By.ID, "main_mine_rb")
    def to_mine(self):
        self.find_element(self._to_mine).click()
        return MinePage(self.driver)

    _academic_circle_write = (By.ID, "academic_circle_write")
    def to_academic_circle_write(self):
        self.find_element(self._academic_circle_write).click()
        # post_publish_center_title
        return PostPublishCenter(self.driver)