
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.login_page import LoginPage


class MinePage(BasePage):
    _mine_avatar = (By.ID, "mine_avatar")
    def login(self):
        self.find_element(self._mine_avatar).click()
        return LoginPage(self.driver)


