import pytest
#import allure
from page.app import App
from time import sleep


class TestDemo:
    def setup(self):
        # self.select_user_interest_area = App.start().select_user_interest_area()
        # self.toSearch = App.start().select_user_interest_area().close()
        self.mainpage = App.start().select_user_interest_area().close()
        # self.mainpage.close_upgrade()
        # print("%s对象拿到driver" % self.toSearch)
        print("%s对象拿到driver" % self.mainpage)
        # return self.mainpage.to_search()

    #@allure.feature('搜索done,test_dxypo')
    @pytest.mark.parametrize("keyword, result", [
        ("amxl", "阿莫西林克拉维酸钾"),
        # ("gaoxueya", "原发性高血压")
    ])
    def test_dxypo(self, keyword, result):
        """
        搜索药品
        :return:
        """
        sleep(3)
        # aa = self.mainpage.to_search().dxy_search("amxl")  # 进入主搜索页,输入搜索内容
        aa = self.mainpage.to_search().dxy_search(keyword)
        # print(aa)
        # print(aa.get_search_text(keyword))
        if keyword == "amxl":
            assert result in aa.get_search_text(keyword)
            aa.dxy_aearch_discuss()
            assert result in aa.get_discuss_text()
            aa.dxy_aearch_real()
            assert result in aa.get_real_text()
            aa.dxy_aearch_drug()
            assert result in aa.get_drug_text()
            aa.dxy_aearch_user()
            assert result in aa.get_user_text()
            aa.dxy_classify_user()
        elif keyword == "gaoxueya":
            assert result in aa.get_search_text(keyword)

        print("搜索ui自动化已完成.....等待退出APP...")


    def teardown(self):
        sleep(10)
        App.quit()