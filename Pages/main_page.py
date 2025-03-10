from elements.button import Button
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        locators = {
            "login_button": "(//*[@id='global_actions']//a)[2]"
        }
        super().__init__(browser, locators)

        self.login_button = Button(self.browser, self.locators.login_button, description="Main page -> Login page")

    def login_start(self):
        self.login_button.click()
