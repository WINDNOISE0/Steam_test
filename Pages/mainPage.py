from Base.BasePage import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        locators = {
            "login_button": "(//*[@id='global_actions']//a)[2]"
        }
        super().__init__(driver, locators)

        self.create_element_dct()

    def login_start(self):
        self.elements.login_button.click_element()
