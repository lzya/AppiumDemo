# from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
from driver.Appium import Appium
from page.base_page import BasePage
from appium import webdriver

class Search(BasePage):

    _tvagree=(MobileBy.XPATH, "//*[@text='同意']")
    _searchterms=(MobileBy.XPATH, "//*[@text='a']")
    _poplater=(MobileBy.XPATH, "//*[@text='下次再说']")
    _follow=(MobileBy.ID, "follow_btn")
    _canle=(MobileBy.ID, "action_close")
    _user=(MobileBy.XPATH, "//*[@text='用户']")
    _name=(MobileBy.ID, "name")
    _search=(MobileBy.ID, "search_input_text")

    # def search(self, keyword):
    #     # Appium.getDriver().find_element_by_id("//*[@text='用户']").send_keys(keyword)
    #     # Appium.getDriver().find_element(_search).send_keys(keyword)
    #     self.find(*self._search).send_keys(keyword)

    #     return self
    #
    # # def getStocks(self):
    #     # return Appium.getDriver().find_element_by_id("name").text
    #     # return Appium.getDriver().find_element(_name).text
    #     return self
    # self.basepage1 = BasePage ()
    def popUp(self):
        """
        处理首次启动，点击弹框上「同意」入口
        :return:
        """
        # b=self.basepage1.findBy(*self._tvagree)
        # b.click()
        # find_element_by_xpath("//*[@text='同意']")
        # Appium.getDriver().find_element_by_xpath("//*[@text='同意']").click()
        # return Appium.getDriver().find_element(*self._agree).click()
         # Appium.getDriver().find_element(*self._tvagree).click() #right
        # self.findBy(*self._tvagree).click()
        BasePage.findBypass(*self._tvagree).click()

        # BasePage.findBy(*self._tvagree).click()
        # return self

    def addStock(self):
        """
        搜索到股票,点击被选中股票
        :return:
        """
        # Appium.getDriver().find_element_by_xpath(_searchterms).click()
        # Appium.getDriver().find_element_by_xpath(_searchterms).click()
        self.find(self._searchterms).click()
        return self

    def clickTouchadd(self):
        # Appium.getDriver().find_element_by_id("follow_btn").click()
        # Appium.getDriver().find_element(_follow).click() # 第一次改造
        self.find(self._follow).click()  # 第2次改造
        return self

    def sorcePopup(self):
        """
        处理评价弹窗，点击下次再说
        :return:
        """
        # Appium.getDriver().find_element_by_xpath(_poplater).click()
        self.find(self._poplater).click()
        return self

    def actionClose(self):
        """
        搜索结束后，点击取消按钮
        :return:
        """
        # Appium.getDriver().find_element_by_id(_canle).click()
        self.find(self._canle).click()
        return self

