from elements.label import Label
from pages.base_page import BasePage


class NewTabHandlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div//*[contains(text(), 'New Window')]"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)

    def come_back_main_page(self):
        self.browser.switch_to_default_window()

    def close_tab(self):
        self.browser.close()
        self.come_back_main_page()

    @property
    def actual_title(self):
        return self.browser.get_window_title()
