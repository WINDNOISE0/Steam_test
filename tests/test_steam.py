from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestSteam:
    def test_authorization(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        main_page.login_start()
        assert login_page.sing_in_label_is_exist(), f'There is no sing_in_label in {str(login_page)}'

        login_page.authorize()
        assert login_page.authorize_loader_is_exist(), f'There is no authorize_loader_is_exist in {str(login_page)}'
        assert login_page.error_login_text_is_exist(), f'There is no error_login_text_is_exist in {str(login_page)}'
