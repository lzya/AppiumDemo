from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.main_page import MainPage


class SelectUserInterestArea(BasePage):
    _agree = (By.XPATH, "//*[@text='同意']")
    _options = (By.XPATH, "//*[@text='神经']")
    _startusingdone = (By.XPATH, "//*[@text='开始使用']")

    def select_user_interest_area(self):
        self.find_element(self._agree).click()
        self.find_element(self._options).click()
        self.find_element(self._startusingdone).click()
        self.driver.tap([(481, 1443), (599, 1561)], 500)  # 通过uiautomortview 识别出坐标 ,点击同意弹框
        return MainPage(self.driver)

