from seleniumbase.common.exceptions import TimeoutException

from elements.button import Button
from elements.input import Input
from elements.label import Label
from pages.base_page import BasePage


class MainPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//span[@id='logo_holder']//img[@src]"
    LOGIN_BUTTON = "(//*[@id='global_actions']//a)[2]"
    FIND_INPUT = "//input[@id='store_nav_search_term']"
    FIND_BUTTON = "//a[@id='store_search_link']"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC)
        self.page_name = "Main Page"

        self.login_button = Button(self.browser, self.LOGIN_BUTTON, description="Main page -> Login page")
        self.find_input = Input(self.browser, self.FIND_INPUT, description="Main page -> Find Input")
        self.find_button = Button(self.browser, self.FIND_BUTTON, description="Main page -> Search page")


    def login_start(self):
        self.login_button.click()

    def find_game(self, game_name: str):
        self.find_input.send_keys(game_name)
        self.find_button.js_click()

