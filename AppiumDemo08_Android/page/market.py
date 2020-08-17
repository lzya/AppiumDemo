from driver.Appium import Appium
from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

class Market(object):

    # _portfoliostockname

    def getMarketstocks(self):
        return Appium.getDriver().find_element_by_id("portfolio_stockName").text
