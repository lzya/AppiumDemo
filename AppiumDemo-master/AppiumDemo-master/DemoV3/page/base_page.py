from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        print(locator)
        """
        找元素
        :param locator:
        :return:
        """
        return self.driver.find_element(*(locator))

    def find_element_and_click(self, locator):
        """
        找到元素并点击，暂未调用
        :param locator:
        :return:
        """
        print(locator)
        self.find_element(locator).click()