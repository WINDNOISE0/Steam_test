from seleniumbase.common.exceptions import TimeoutException

from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class MainPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//span[@id='logo_holder']//img[@src]"
    LOGIN_BUTTON = "(//*[@id='global_actions']//a)[2]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC)
        self.page_name = "Main Page"

        self.login_button = Button(self.browser, self.LOGIN_BUTTON, description="Main page -> Login page")

    def is_opened(self):
        try:
            self.wait_for_open()
            return True
        except TimeoutException:
            return False

    def login_start(self):
        self.login_button.click()
