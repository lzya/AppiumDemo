import pytest
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class SearchPage(BasePage):
    _input_text = (By.ID, "search_input_text")
    _text_locator = (By.XPATH, "//*[@text='BABA']")
    def search(self, keyword):
        self.find_element(self._input_text).send_keys(keyword)
        self.find_element(self._text_locator).click()
        return self

    def get_current_price(self):
        return float(self.driver.find_element_by_id("current_price").text)


    _search_input_met = (By.ID, "search_input_met")
    _tv_search_content_amxl= (By.XPATH, "//*[@text='阿莫西林克拉维酸钾']")  # 药品
    _tv_search_content_gaoxueya = (By.XPATH, "//*[@text='高血压']")  # 疾病
    # @pytest.mark.parametrize("list", [("阿莫西林克拉维酸钾"), ("高血压")])
    def dxy_search(self, keyword):
        self.find_element(self._search_input_met).send_keys(keyword)
        print(self.find_element(self._search_input_met).send_keys(keyword))
        if keyword == "amxl":
            self.find_element(self._tv_search_content_amxl).click()
        elif keyword == "gaoxueya":
            self.find_element(self._tv_search_content_gaoxueya).click()
        # self.find_element(list).click()
        return self


    def get_search_text(self, keyword):
        if keyword == "amxl":
            dd = self.driver.find_element_by_id("tv_accurate_drug_title").text
        elif keyword == "gaoxueya":
            dd = self.driver.find_element_by_id("tv_accurate_disease_name").text
        return dd
