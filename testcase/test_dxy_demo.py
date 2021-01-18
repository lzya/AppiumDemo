from page.app import App
from time import sleep
from page.search_page import SearchPage


class TestDemo:

    def setup(self):
        # self.select_user_interest_area = App.start().select_user_interest_area()
        self.toSearch = App.start().select_user_interest_area().close()
        print("%s对象拿到driver" % self.toSearch)


    def test_dxypo(self):
        """
        搜索药品
        :return:
        """
        sleep(3)
        # self.toSearch.to_search().dxy_search("amxl")  # 进入主搜索页,输入搜索内容
        assert "阿莫西林克拉维酸钾片 (珠海联邦制药)" in self.toSearch.to_search().dxy_search("amxl")  # 进入主搜索页,输入搜索内容
        print("DONE.....")

    def teardown(self):
        # sleep(20)
        App.quit()