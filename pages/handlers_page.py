from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage
from pages.new_tab_handlers_page import NewTabHandlersPage


class HandlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Opening a new window')]"

    CLICK_HERE_BUTTON_LOC = "//a[contains(text(), 'Click Here')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)
        self.click_here_button = Button(browser, self.CLICK_HERE_BUTTON_LOC)

    def open_new_tab(self) -> (NewTabHandlersPage, str):
        self.click_here_button.click()
        new_page_object = NewTabHandlersPage(self.browser)

        return new_page_object, self.browser.currency_window_handle_id