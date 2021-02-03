from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.mine_page import MinePage


class LoginPage(BasePage):


    _tab_account = (By.XPATH, "//*[@text='用账号密码登录']")
    _sso_username = (By.ID, "sso_username")
    _sso_password = (By.ID, "sso_password")
    _sso_login = (By.ID, "sso_login")
    def username_password_login(self):
        self.find_element(self._tab_account).click()
        self.find_element(self._sso_username).send_keys("18500239087")
        self.find_element(self._sso_password).send_keys("dxy123456")
        self.find_element(self._sso_login).click()
        return MinePage(self.driver)

    def signout(self):

        pass





