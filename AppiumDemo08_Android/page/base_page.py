from selenium.webdriver.common.by import By
from driver.Appium import Appium
import xml.etree.ElementTree as ET
from appium import webdriver


class BasePage(object):
    # driver = None
    black_words=["//*[@text='同意']"]
    def findBy(self, by=By.ID, value=None):
        # Appium.getDriver().find_element(locate)
        try:
            Appium.getDriver().find_element(by, value)
        except:
            for w in self.black_words:
                self.elements=Appium.getDriver().find_element(by, value)
                if len(elements) > 0:
                    elements[0].click()
                    self.elements=Appium.getDriver().find_element(by, value)
                    return self.elements
        #     print(page_source)
        #     black_words=ET.fromstring(page_source)

    def findBypass(self, by=By.ID, value=None):
        Appium.getDriver().find_element(by, value)



    def find(self, locate):
        # Appium.getDriver().find_element(locate)
        Appium.getDriver().find_element(*locate)
        # self.findBy(*locate)