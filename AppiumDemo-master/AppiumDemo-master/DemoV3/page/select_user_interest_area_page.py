from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.main_page import MainPage


class SelectUserInterestArea(BasePage):
    _agree = (By.XPATH, "//*[@text='同意并继续']")
    _options = (By.XPATH, "//*[@text='丁香热点']")
    # _startuser = (By.XPATH, "//*[@text='开始使用']")
    _startuser = (By.ID, "tv_start_user")

    def select_user_interest_area(self):
        self.find_element(self._agree).click()
        self.find_element(self._options).click()
        self.find_element(self._startuser).click()
        # self.driver.tap([(481, 1443), (599, 1561)], 500)  # 通过uiautomortview 识别出坐标 ,点击同意弹框
        return MainPage(self.driver)

    _haveaccount = (By.XPATH, "//*[@text='直接登录']")
    def click_login(self):
        """
        1、点击直接登录，进入登录页
        :return:
        """
        self.find_element(self._haveaccount).click()
        return MainPage(self.driver)