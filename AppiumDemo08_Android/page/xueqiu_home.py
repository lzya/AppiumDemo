from appium.webdriver.common.mobileby import MobileBy
from driver.Appium import Appium
from page.base_page import BasePage
from page.search import Search


class Xueqiu_home(BasePage):
    _homesearch=(MobileBy.ID, "home_search")
    _tab_name=(MobileBy.XPATH, "//*[@text='行情']")

    def toSearch(self):
        # Appium.getDriver().find_element_by_id("home_search").clcik()
        # 主搜索
        # Appium.getDriver().find_element_by_id("home_search").click()
        self.findBy(*self._homesearch).click()
        return Search()

    def switchBar(self):
        """
        导航栏切换
        """
        # Appium.getDriver().find_element_by_xpath("//*[@text='行情']").click()
        self.findBy(*self._tab_name).click()
        return self





