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
    # //搜索下各tab
    _tv_discuss = (By.XPATH, "//*[@text='讨论']")
    _tv_disease = (By.XPATH, "//*[@text='疾病']")
    _tv_real = (By.XPATH, "//*[@text='资讯']")
    _tv_drug = (By.XPATH, "//*[@text='药品']")
    _tv_uptodate = (By.XPATH, "//*[@text='UptoDate']")
    _tv_user = (By.XPATH, "//*[@text='用户']")
    _tv_classify = (By.ID, "iv_search_classify")
    _tv_search_menu = (By.ID, "search_menu_item_tv")
    _tv_search_back = (By.ID, "iv_search_back")

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

        # 以下是点击讨论
    def dxy_aearch_discuss(self):
        self.find_element(self._tv_discuss).click()  # 点击讨论
        #讨论做校验
    def get_discuss_text(self):
        abc = self.driver.find_element_by_xpath("//*[@text='阿莫西林克拉维酸钾'and contains(@resource-id,'tv_post_title')]").text
        return abc


        # 以下是点击资讯
    def dxy_aearch_real(self):
            self.find_element(self._tv_real).click()  # 点击资讯
        #资讯做校验
    def get_real_text(self):
            bcd = self.driver.find_element_by_xpath("//*[@text='阿莫西林克拉维酸钾一日两次还是一日三次？'and contains(@resource-id,'tv_info_title')]").text
            return bcd


        #以下是点击药品
    def dxy_aearch_drug(self):
        self.find_element(self._tv_drug).click()  # 点击药品

        # 药品做校验
    def get_drug_text(self):
        drug = self.driver.find_element_by_xpath(
            "//*[@text='力百汀 (阿莫西林克拉维酸钾片) 0.625g'and contains(@resource-id,'tvTitle')]").text
        return drug

        #以下是点击用户tab
    def dxy_aearch_user(self):
        self.find_element(self._tv_user).click()  # 点击药品

        # 用户tab做校验
    def get_user_text(self):
        user = self.driver.find_element_by_xpath(
            "//*[@text='阿莫西林克拉维酸钾'and contains(@resource-id,'tv_label_name')]").text
        return user

        #点击更多后点击综合
    def dxy_classify_user(self):
        self.find_element(self._tv_classify).click()  # 点击更多
        self.find_element(self._tv_search_menu).click() #点击综合
        self.find_element(self._tv_search_back).click() #点击返回
        self.find_element(self._tv_search_back).click()  #点击返回





