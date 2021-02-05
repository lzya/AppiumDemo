
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.login_page import LoginPage


class MinePage(BasePage):
    _mine_avatar = (By.ID, "mine_avatar")
    def login(self):
        """
        点击未登录头像进入登录页
        :return:
        """
        self.find_element(self._mine_avatar).click()
        return LoginPage(self.driver)


    _main_academy_circle_rb = (By.ID, "main_academy_circle_rb")
    def quit_mine(self):
        """
        若停留在我的页面，需点击学术圈，切换至学术圈
        :return:
        """
        self.find_element(self._main_academy_circle_rb).click()
        from page.main_page import MainPage
        return MainPage(self.driver)
