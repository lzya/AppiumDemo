from appium import webdriver


from page.app import App


class TestDemo:

    def setup(self):
        self.search_page = App.start().to_search()

    def test_po(self):
        self.search_page.search("alibaba")
        assert self.search_page.get_current_price() > 10

    def test_dxypo(self):
        App.start().select_user_interest_area()


    def teardown(self):
        # sleep(20)
        App.quit()