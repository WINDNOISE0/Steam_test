

from elements.label import Label
from pages.base_page import BasePage


class NewTabHandlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div//*[contains(text(), 'New Window')]"
    TITLE = "New Window"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)

        self._current_handle_id = None

    def come_back_main_page(self):
        self.browser.switch_to_default_window()

    def is_correct_title_name(self):
        return self.browser.get_window_title() == self.TITLE

    def close_tab(self):
        self.browser.driver.switch_to.window(self._current_handle_id)
        self.browser.close()
        self.come_back_main_page()

    @property
    def handle_id(self):
        return self._current_handle_id

    @handle_id.setter
    def handle_id(self, handel_id):
        self._current_handle_id = handel_id


    @property
    def expected_title(self):
        return self.TITLE

    @property
    def actual_title(self):
        return self.browser.get_window_title()

