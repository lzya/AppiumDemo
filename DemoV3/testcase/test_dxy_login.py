from page.app import App
from time import sleep


class TestDemo:
    def setup(self):
        self.mainpage = App.start().select_user_interest_area().close()
        print("%s对象拿到driver" % self.mainpage)
        # return self.mainpage.to_search()

    def test_dxy_login(self):
        """
        登录账号
        :return:
        """
        sleep(3)
        # aa = self.mainpage.to_search().dxy_search("amxl")  # 进入主搜索页,输入搜索内容
        print("进入登录页")
        aa = self.mainpage.to_mine().login()
        aa.username_password_login()
        print("登录成功")




    def teardown(self):
        # sleep(20)
        App.quit()