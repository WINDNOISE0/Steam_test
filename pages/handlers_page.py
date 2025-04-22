from elements.button import Button
from elements.label import Label
from helpers.enpoints_urn import URN
from helpers.helper_tools import HelperTools
from pages.base_page import BasePage
from pages.new_tab_handlers_page import NewTabHandlersPage


class HandlersPage(BasePage):
    URL = HelperTools.create_url(URN.WINDOWS)

    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'Opening a new window')]"

    CLICK_HERE_BUTTON_LOC = "//a[contains(text(), 'Click Here')]"

    def __init__(self, browser):
        super().__init__(browser)

        self.open_page(self.URL)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)
        self.click_here_button = Button(browser, self.CLICK_HERE_BUTTON_LOC)

        self.new_page_index = []

    def open_new_tab(self):
        self.click_here_button.click()
        new_handle_id = self.browser.get_handle_id_list()[-1]
        new_page_object = NewTabHandlersPage(self.browser)
        new_page_object.handle_id = new_handle_id

        self.browser.switch_to_handle_window(new_page_object.handle_id)
        return new_page_object

    def is_closed_new_tab(self, handles_id: str):
        return handles_id not in self.browser.driver.window_handles







