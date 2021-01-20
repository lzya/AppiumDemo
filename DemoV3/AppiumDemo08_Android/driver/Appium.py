# import pytest
# # noinspection PyUnresolvedReferences
# import unittest
# # import logging
from appium import webdriver

class Appium(object):
    """@type driver: WebDriver"""

    # 仅适用于python3.5以上
    # driver: WebDriver = None
    # driver = None

    @classmethod
    def getDriver(cls):
        return cls.driver

    @classmethod
    def initDriver(cls):
        print("setUp")
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '8.0.0',
                        'deviceName': 'APU0216720000191',
                        'appPackage': 'com.xueqiu.android',
                        'appActivity': '.view.WelcomeActivityAlias',
                        'automationName': 'UiAutomator2',
                        'autoGrantPermissions': True    # 解决权限问题
                        # 'unicodeKeyboard': True     # 使用Unicode编码方式发送字符串
                      }
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
        cls.driver.implicitly_wait(50)  # 隐式等待