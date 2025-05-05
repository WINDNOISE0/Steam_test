from elements.web_element import WebElement
from pages.base_page import BasePage


class AuthorizePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//p"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "basic_page -> page_header")
