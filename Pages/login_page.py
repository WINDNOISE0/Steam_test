from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from helpers.data_generator import DataGenerator
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        locators = {
            "sign_in_header": "//div[contains(@style, 'display: flex')]//div",
            "login_input": "(//input[@type='text'])[1]",
            "password_input": "//input[@type='password']",
            "authorize_button": "//button[@type='submit']",
            "authorize_loader": "(//button[@type='submit' and @disabled]//div)[1]",
            "error_login_text": "(//form)//div[5][1]"
        }
        super().__init__(browser, locators)

        self.sing_in_label = Label(self.browser, self.locators.sign_in_header)
        self.login_input = Input(self.browser, self.locators.login_input)
        self.password_input = Input(self.browser, self.locators.password_input)
        self.authorize_button = Button(self.browser, self.locators.authorize_button)
        self.authorize_loader = WebElement(self.browser, self.locators.authorize_loader)
        self.error_login_text = WebElement(self.browser, self.locators.error_login_text)

    def authorize(self):
        self.login_input.send_keys(DataGenerator.get_random_username())
        self.password_input.send_keys(DataGenerator.get_random_password())
        self.authorize_button.click()

    def sing_in_label_is_exist(self):
        return self.sing_in_label.is_exists()

    def authorize_loader_is_exist(self):
        return self.authorize_loader.is_exists()

    def error_login_text_is_exist(self):
        return self.error_login_text.is_exists()
