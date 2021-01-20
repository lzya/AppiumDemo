from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from driver.Appium import Appium
from page.Search import Search

class Testxueqiu(unittest.TestCase):
    def setUp(self):
        Appium.initDriver()
        print(Appium.driver)

    def test_add_stock(self):
        self.driver.find_element_by_xpath("//*[@text='同意']").click()
        self.driver.find_element_by_id("home_search").click()
        self.driver.save_screenshot("screenshot/home_search.png")
        self.driver.find_element_by_id("search_input_text").send_keys("pdd")
        self.driver.save_screenshot("screenshot/search_input_text.png")
        sleep(5)
        self.driver.find_element_by_xpath(
            "//*[@text='拼多多' and contains(@resource-id,'name')]").click()
        # xpath定位
        # 元素定位：先找父窗体的ID，再找子窗体的className，就可以找到第1个满足它的条件
        self.driver.find_element_by_id("follow_btn")\
            .find_element_by_class_name("android.widget.TextView")\
            .get_attribute('resourceId')

        if len(self.driver.find_elements_by_id("follow_btn")) > 0:
            # self.driver.implicitly_wait(5)  # 隐式等待
            sleep(10)
            self.driver.find_element_by_id("follow_btn").click()
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()
            self.driver.save_screenshot("screenshot/follow_btn.png")