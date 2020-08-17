import unittest
import logging
from appium import webdriver
from driver.Appium import Appium
from page.search import Search
from page.xueqiu_home import Xueqiu_home
from page.market import Market
from time import sleep


class Testxueqiu(unittest.TestCase):

    def setUp(self):
        Appium.initDriver()
        print(Appium.driver)

    def test_search(self):
        """
        1.启动app，点击同意
        2.点击主搜索，并等待5s,待toast消失
        3.搜索框内输入「pdd」,出现搜索结果列表
        4.
        :return:
        """
        search_r = Search()
        sleep(10)
        search_r.popUp()  # 点击同意
        home = Xueqiu_home()
        home.toSearch()  # 点击主搜索
        assert search("pdd").getStocks() == "拼多多"

        # ？？ 请调整为链式调用

    # def test_search_user(self):
    #     search_page = Search()
    #     search_page.search("pdd")
    #     assert search_page.getstocks() == "拼多多"

    # def test_add_stock(self):
    #     """
    #     添加自选股，拼多多，并在行情页，可看到拼多多
    #     :return:
    #     """
    #     search_page = Search()
    #     sleep(10)
    #     search_page.popUp
    #     search = Xueqiu_home()
    #     search.toSearch()
    #     sleep(10)
    #     search_page.search("pdd")
    #     assert search_page.getStocks() == "拼多多"
    #     search_page.addStock()
    #     search_page.clickTouchadd()
    #     search_page.sorcePopup()
    #     search_page.actionClose()
    #     search.switchBar()
    #     market = Market()
    #     assert market.getMarketstocks() == "拼多多"






