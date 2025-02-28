from Base.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        locators = {
            "sign_in_header" : "//div[contains(@style, 'display: flex')]//div",
            "login_input": "(//input[@type='text'])[1]",
            "password_input": "//input[@type='password']",
            "authorize_button": "//button[@type='submit']",
            "authorize_loader": "(//button[@type='submit' and @disabled]//div)[1]",
            "error_login_text": "(//form)//div[5][1]"
        }
        super().__init__(driver, locators)
        self.create_element_dct()

    def authorize(self):
        self.elements.login_input.input_text(self.data_generator.get_random_username())
        self.elements.password_input.input_text(self.data_generator.get_random_password())
        self.elements.authorize_button.click_element()



















