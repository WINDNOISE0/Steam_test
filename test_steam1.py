from Helpers.asserts import Asserts
from Helpers.logger import Logger
from Pages.loginPage import LoginPage
from Pages.mainPage import MainPage


class TestSteam:
    def test_authorization(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        Logger.add_start_step(driver,"test_authorization")

        main_page.login_start()
        Asserts.element_is_visible(
            driver,
            "sign_in_header",
            login_page.get_locator("sign_in_header"),
            main_page.current_link())

        login_page.authorize()
        Asserts.element_is_visible(
            driver,
            "authorize_loader",
            login_page.get_locator("authorize_loader"),
            login_page.current_link())
        Asserts.element_is_visible(
            driver,
            "error_login_text",
            login_page.get_locator("error_login_text"),
            login_page.current_link())

        Logger.add_end_step()
