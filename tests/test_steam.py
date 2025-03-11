from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestSteam:
    def test_authorization(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        assert main_page.is_opened(), "No open main page"
        main_page.login_start()
        assert login_page.is_exist_sing_in_label(), f'There is no sing_in_label in {str(login_page)}'

        login_page.authorize()
        assert login_page.is_exist_authorize_loader(), f'There is no authorize_loader_is_exist in {str(login_page)}'
        assert login_page.is_visible_error_login_text(), f'There is no error_login_text_is_exist in {str(login_page)}'
