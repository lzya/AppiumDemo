import unittest
import pytest
from appium import webdriver

class TestBrowser(unittest.TestCase):

    def setUp(self):
        print("setUp")
        desired_caps = {'platformName': 'Android',
                        'deviceName': 'APU0216720000191',
                        'browserName': 'Browser'
                        # 'appPackage': 'com.android.browser',
                        # 'appActivity': 'com.UCMobile.main.UCMobile'
                        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动浏览器
        self.driver.implicitly_wait(30)  # 隐式等待


    # 测试未通过，原因：
    # 1. Chromedriver 版本需调整，需下载；
    # 2. chrome://inspect/#devices 访问时，需被测app开启webDriver - 找开发开启或者测试包
    def test_main(self):
        self.driver.get("https://danjuanapp.com/my-money")
        self.driver.find_element_by_css_selector(".btns .blank").click()
