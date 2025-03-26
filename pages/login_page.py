from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class LoginPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[contains(@style, 'display: flex')]//div"

    SIGN_IN_HEADER = "//div[contains(@style, 'display: flex')]//div"
    LOGIN_INPUT = "(//input[@type='text'])[1]"
    PASSWORD_INPUT = "//input[@type='password']"
    AUTHORIZE_BUTTON = "//button[@type='submit']"
    AUTHORIZE_LOADER = "(//button[@type='submit' and @disabled]//div)[1]",
    ERROR_LOGIN_TEXT = "(//form)//div[5][1]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Login page"
        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC)

        self.sing_in_label = Label(self.browser, self.SIGN_IN_HEADER)
        self.login_input = Input(self.browser, self.LOGIN_INPUT)
        self.password_input = Input(self.browser, self.PASSWORD_INPUT)
        self.authorize_button = Button(self.browser, self.AUTHORIZE_BUTTON)
        self.authorize_loader = WebElement(self.browser, self.AUTHORIZE_LOADER)
        self.error_login_text = WebElement(self.browser, self.ERROR_LOGIN_TEXT)

    def authorize(self, login, password):
        self.login_input.send_keys(login)
        self.password_input.send_keys(password)
        self.authorize_button.click()

    def is_exists_sing_in_label(self):
        return self.sing_in_label.is_exists()

    def is_exists_authorize_loader(self):
        return self.authorize_loader.is_exists()

    def is_visible_error_login_text(self):
        return self.error_login_text.is_visible()
