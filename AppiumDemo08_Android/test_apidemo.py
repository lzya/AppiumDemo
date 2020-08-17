# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
import unittest
import logging
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

class TestApiDemo(unittest.TestCase):

    def setUp(self):
        print("setUp")
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '8.0.0',
                        'deviceName': 'APU0216720000191',
                        'appPackage': 'io.appium.android.apis',
                        'appActivity': '.ApiDemos',
                        'automationName': 'UiAutomator2',
                        'autoGrantPermissions': True,  # 解决权限问题
                        'unicodeKeyboard': True  # 使用Unicode编码方式发送字符串
                         }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
        self.driver.implicitly_wait(10)  # 隐式等待

# toast 定位方法
    def test_toast(self):
        for i in range(1, 2):
            sleep(1)
            self.driver.swipe(start_x=621, start_y=1746, end_x=824, end_y=971)


        self.driver.find_element_by_accessibility_id("Views").click()

        # 使用 uiautomator 定位 - 到instance（0），找到第一个可滑动的地方进行滑动后，查找到Popup Menu textView
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "Popup Menu")').click()
        self.driver.find_element_by_accessibility_id("Make a Popup!").click()
        self.driver.find_element_by_xpath("//*[@text='Search']").click()
        # toast仅xpath方法识别到 xpath定位的高级方法
        print(self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element_by_xpath("//*[@package='com.android.settings']").text)
        print(self.driver.find_element_by_xpath("//*[contains(@text,'Clicked')]").text)

        # toast使用 uiautomator方法不能被识别到
        # print(self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().className("android.widget.Toast")'
        # ).text)

    def test_toast_no_found(self):
        for i in range(1, 2):
            sleep(1)
            self.driver.swipe(start_x=621, start_y=1746, end_x=824, end_y=971)
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "Popup Menu")'
        ).click()
        self.driver.find_element_by_accessibility_id("Make a Popup!").click()
        self.driver.find_element_by_xpath("//*[@text='Search']").click()

    # 仅适用于简单场景，如果页面有个图片，就无法识别
    def test_webview_sim_simple(self):
        for i in range(1, 2):
            sleep(1)
            self.driver.swipe(start_x=621, start_y=1746, end_x=824, end_y=971)
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "WebView")'
        ).click()
        self.driver.find_element_by_xpath("//*[@text='i am a link']").click()


