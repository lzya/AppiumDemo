# from selenium.webdriver.remote import webdriver
# from selenium import webdriver
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from page.main_page import MainPage
from appium import webdriver

from page.select_user_interest_area_page import SelectUserInterestArea


class App:
    driver: WebDriver
    @classmethod
    def start(cls):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '8.0.0',
                        'deviceName': 'APU0216720000191',
                        # 'appPackage': 'com.xueqiu.android',
                        'appPackage': 'cn.dxy.idxyer',
                        # 'appActivity': '.view.WelcomeActivityAlias',
                        'appActivity': '.startup.biz.StartupActivity',
                        'automationName': 'UiAutomator2',
                        'autoGrantPermissions': True  # 解决权限问题
                        # 'unicodeKeyboard': True     # 使用Unicode编码方式发送字符串
                        }

        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
        cls.driver.implicitly_wait(10)  # 隐式等待
        sleep(2)
        # cls.driver.tap([(723, 1331), (960, 1467)], 500)  # [使用雪球app时启用]通过uiautomortview 识别出坐标

        # return MainPage(cls.driver)
        return SelectUserInterestArea(cls.driver)

    def install(self):
        pass

    @classmethod
    def quit(cls):
        cls.driver.quit()