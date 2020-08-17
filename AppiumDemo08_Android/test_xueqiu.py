# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
import unittest
import logging
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Testxueqiu(unittest.TestCase):
    loader = False
    def setUp(self):
        print("setUp")
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '8.0.0',
                        'deviceName': 'APU0216720000191',
                        'appPackage': 'com.xueqiu.android',
                        'appActivity': '.view.WelcomeActivityAlias',
                        'automationName': 'UiAutomator2',
                        'autoGrantPermissions': True,  # 解决权限问题
                        'unicodeKeyboard': True  # 使用Unicode编码方式发送字符串
                        # 'resetKeyboard': True  # 隐藏键盘
                        # 以上2行增加后不能成功启动APP，反而每次运行程序都会自动启动需要安装Appium Android Input Manager for
                        }
        if True == Testxueqiu.loader:
            desired_caps['noReset'] = "True"

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动app
        self.driver.implicitly_wait(20)  # 隐式等待
        loader = True


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

    def test_check_stock(self):
        sleep(6)
        # self.driver.find_element_by_xpath("//*[@text='取消']").click()
        # 控件名称不规范时，采用双重定位，拿到唯一条件
        self.driver.find_element_by_xpath(
            "//*[@text='行情'and contains(@resource-id,'tab_name')]").click()
        # 断言
        assert 1 == len(self.driver.find_elements_by_xpath(
            "//*[contains(@resource-id,'portfolio_stockName') and @text='拼多多']"))


    def test_search_add(self):
        """
        作业1：进入自选，点击搜索，搜索alibaba,点击添加，让后回到自选，判断阿里巴巴已经在自选中。
        :return:
        """
        sleep(6)
        self.driver.find_element_by_xpath("//*[@text='同意']").click()
        self.driver.find_element_by_xpath(
            "//*[@text='行情'and contains(@resource-id,'tab_name')]").click()
        self.driver.find_element_by_id('action_search').click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@text='BABA' and contains(@resource-id,'code')]").click()
        if len(self.driver.find_elements_by_id("follow_btn")) > 0:
            # self.driver.implicitly_wait(5)  # 隐式等待
            sleep(10)
            self.driver.find_element_by_xpath("//*[@text='加自选' and contains(@resource-id,'follow_btn')]").click()
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()
        self.driver.find_element_by_id("action_close").click()
        # 断言
        assert 1 == len(self.driver.find_elements_by_xpath(
            "//*[contains(@resource-id,'portfolio_stockName') and @text='阿里巴巴']"))

    def test_mobile(self):
        self.driver.start_activity("com.android.bbkcalculator",".Calculator")
        #         print(self.driver.is_locked())
        #         self.driver.lock(5)
        #         self.driver.unlock()
        #         # self.driver.shake()

    def test_touch(self):
        # 进入自选， 长按阿里巴巴，弹出框内点击删除，列表内消失
        self.loaded()
        self.driver.find_element_by_xpath(
            "//*[@text='行情'and contains(@resource-id,'tab_name')]").click()
        element = self.driver.find_element_by_xpath("//*[@text='拼多多']")
        # from appium.webdriver.common.touch_action import TouchAction 需要用这个
        TouchAction(self.driver).long_press(element).perform()
        self.driver.find_element_by_xpath("//*[@text='删除']").click()


    def loaded(self):
        """
        循环查找行情，找到坐标一样的以后执行下一步操作
        :return:
        """
        sleep(3)
        locations = ["x", "y"]
        self.driver.find_element_by_xpath("//*[@text='同意']").click()
        while locations[-1] != locations[-2]:
            element = self.driver.find_element_by_xpath(
                "//*[@text='行情'and contains(@resource-id,'tab_name')]")
            locations.append(element.location)
            print(locations)


    def test_main_swipe(self):
        """
        需要独立执行
        1.开发者选项内开启location
        2.swipe - 滑动
        :return: 无
        """
        sleep(3)
        self.driver.find_element_by_xpath("//*[@text='同意']").click()
        # self.loaded()
        # 热门tab下滑动
        for i in range(1, 5):
            sleep(1)
            # 变化X轴，从左到右划
            self.driver.swipe(start_x=718, start_y=1404, end_x=500, end_y=500)
            # 斜着划
            self.driver.swipe(start_x=87, start_y=457, end_x=0, end_y=1056)
            # 滑动到最底部？

    def test_batter(self):
        # 获取电量信息
        self.driver.execute_script("mobile:batteryInfo")


    def test_shell(self):
        self.driver.execute_script("mobile:adb shell pm clear com.xueqiu.android")

        # 启动雪球
        self.driver.execute_script("mobile:shell", {"command" : "am", "args" : ["start -n", "com.xueqiu.android"]})

    def test_webview_sim_image(self):
        self.loaded()
        self.driver.find_element_by_xpath(
            "//*[@text='交易'and contains(@resource-id,'tab_name')]").click()
        # 点击图片
        self.driver.find_element_by_accessibility_id("16e172ee2be2a473fee98fc7").click()

    def test_webview_sim_h5(self):
        self.loaded()
        self.driver.find_element_by_xpath(
            "//*[@text='交易'and contains(@resource-id,'tab_name')]").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (MobileBy.ACCESSIBILITY_ID, "常见问题")))
        self.driver.switch_to.context("WEBVIEW_com.xueqiu.android")
        # print(self.driver.contexts)
        print(self.driver.current_context)
        print(self.driver.page_source)
        self.driver.find_element_by_css_selector(".trade_home_agu_3ki").click()


    # 作业3 - 交易 ->基金 -> 已有蛋卷基金账户登录 -> 使用密码登录 ->输入用户名密码，点击登录
    def test_webview_loader(self):
        self.loaded()
        self.driver.find_element_by_xpath(
            "//*[@text='交易'and contains(@resource-id,'tab_name')]").click()
        # self.driver.find_element_by_accessibility_id("16e172ee2be2a473fee98fc7").click()
        self.driver.find_element_by_xpath(
            "//*[@text='基金'and contains(@resource-id,'title_text')]").click()
        self.driver.find_element_by_xpath(
            "//*[@text='蛋卷基金安全开户'and contains(@resource-id,'btn_openaccount')]").click()
        self.driver.find_element_by_xpath(
            "//*[@text='请输入手机号'and contains(@resource-id,'et_telephone')]").send_keys("18000000023")
        self.driver.find_element_by_xpath(
            "//*[@text='请输入验证码'and contains(@resource-id,'et_password')]").send_keys("851422")
        self.driver.find_element_by_xpath(
            "//*[@text='下一步'and contains(@resource-id,'vg_login_btn')]").click()


    # def find_Element(self, type, value):
    #     """
    #     查找某个元素
    #     :param type:取值的类型包括：id\name\class_name...
    #     :param value:根据type的类型给值
    #     :return:
    #     """
    #
    #     logging.info("开始执行----find_element----查找元素方法")
    #     # noinspection PyBroadException
    #     try:
    #         if type == 'id':
    #             try:
    #                 return self.driver.find_element(By.ID, value)
    #             # noinspection PyBroadException
    #             except Exception as e:
    #                 logging.info("未找到%type -- %value" % (type, value))
    #                 return Flase
    #         elif type == "name":
    #             try:
    #                 return self.driver.find_element(By.NAME, value)
    #             except Exception as e:
    #                 logging.info("未找到%type -- %value" % (type, value))
    #                 return Flase
    #     except:
    #         logging.warning("此处抛异常 --- find_Element")
    #         assert "find_Element"

    # def click(self):
    #     self.find_Element(type, self.value).click()

    def wait(self, seconds):
        """
        隐式等待
        :param seconds:
        :return:
        """
        self.driver.implicitly_wait(seconds)


    def test_add_us(self):
        """
        作业3
        - 加一只美股，判断是否添加成功 test_add_us
        - 然后删除一只美股，判断删除成功 test_delete_us
        - 利用参数化或者数据驱动添加30只股票  test_add_touch
        - 添加10只美股，在全部股票>=2页的时候，断言某个股票同时存在于“美股”和“全部”分类中 test_exist_in_all
        """
        self.loaded()
        self.find_Element(type="")


    # def test_delete_us(self):
        pass

    # def test_add_touch(self):
        pass


    # def test_exist_in_all(self):
        pass

    # 作业1，封装一个滚动方法，swipe
    def return_element_swipe(self):
        pass

    def test_search_alibaba(self):
        """
        作业2：
        - 进入自选，点击搜索，搜索“阿里巴巴”，点击添加，判断添加按钮自动变化状态
        - 进入自选，判断“阿里巴巴”是否存在，不要使用Xpath定位判断阿里巴巴股票存在 test_alibaba_exist
        :return:
        """
        sleep(6)
        self.driver.find_element_by_xpath("//*[@text='同意']").click()
        self.driver.find_element_by_xpath(
            "//*[@text='行情'and contains(@resource-id,'tab_name')]").click()
        sleep(3)
        self.driver.find_element_by_id('action_search').click()
        self.driver.find_element_by_id("search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@text='BABA' and contains(@resource-id,'code')]").click()
        # 元素定位：先找父窗体的ID，再找子窗体的className，就可以找到第1个满足它的条件
        before = self.driver.find_element_by_id("follow_btn")\
            .find_element_by_class_name("android.widget.TextView")\
            .get_attribute("resourceId")
        if before == "com.xueqiu.android:id/follow_btn":
            self.driver.find_element_by_id("follow_btn").click()
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()  # 检测是否有评价弹窗，有则点击下次再说
            after = self.driver.find_element_by_id("followed_btn")\
                .find_element_by_class_name("android.widget.TextView")\
                .get_attribute("resourceId")
            assert before != after  # 通过按钮的ID判断状态是否变化

        self.driver.find_element_by_id("action_close").click()

        assert self.driver.find_element_by_id("portfolio_stockName")\
            .find_element_by_class_name("android.widget.TextView")\
            .get_attribute("text") == "阿里巴巴"

    def test_alibaba_exist(self):
        """
        作业2：
        - 进入自选，判断“阿里巴巴”是否存在，不要使用Xpath定位判断阿里巴巴股票存在 test_alibaba_exist
        :return:
        """
        sleep(5)
        self.driver.find_element_by_xpath("//*[@text='同意']").click()
        self.driver.find_element_by_xpath(
            "//*[@text='行情'and contains(@resource-id,'tab_name')]").click()
        # 断言
        assert self.driver.find_element_by_id("portfolio_stockName")\
            .find_element_by_class_name("android.widget.TextView")\
            .get_attribute("text") == "阿里巴巴"
    # test_search_alibaba & test_alibaba_exist一起跑的时候就会报错，单跑ok（已调整case,单条执行）

    def test_search(self):
        search_page = Search()
        search_page.search("pdd")
        assert search_page.getstocks() == "拼多多"

