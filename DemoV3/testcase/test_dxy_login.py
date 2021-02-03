from page.app import App
from time import sleep


class TestDemo:
    def setup(self):
        self.mainpage = App.start().select_user_interest_area().close()
        print("%s对象拿到driver" % self.mainpage)
        # return self.mainpage.to_search()
        # return self

    def test_dxy_login(self):
        """
        登录账号
        :return:
        """
        sleep(3)
        print("进入登录页")
        aa = self.mainpage.to_mine().login()
        dd = aa.username_password_login().quit_mine()
        dd.to_academic_circle_write()  # 进入学术圈发帖页
        # 点击学术圈发帖

        print("登录成功")


    def teardown(self):
        # sleep(20)
        App.quit()