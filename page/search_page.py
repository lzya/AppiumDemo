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
    _tv_search_content = (By.XPATH, "//*[@text='阿莫西林克拉维酸钾']")  # 药品
    _tv_accurate_drug_title = (By.ID, "tv_accurate_drug_title")
    def dxy_search(self, keyword):
        self.find_element(self._search_input_met).send_keys(keyword)
        self.find_element(self._tv_search_content).click()
        return self.driver.find_element_by_xpath(self._tv_accurate_drug_title).text

    # # _tv_accurate_drug_title = (By.ID, "tv_accurate_drug_title")
    # def get_search_text(self):
    #     # print(self.driver.find_element_by_id(self._tv_accurate_drug_title).text)
    #     # return self.driver.find_element_by_id(self._tv_accurate_drug_title).text
    #     return self.driver.find_element_by_xpath("//*[@id='tv_accurate_drug_title']").text
