from elements.web_element import WebElement
from helpers import UrlUtils
from helpers.enpoints_urn import URN
from pages.base_page import BasePage


class AuthorizePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[@id='content']//p"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "basic_page -> page_header")

    def authorize(self, username, password):
        basic_auth_link = UrlUtils.create_basic_auth_link(URN.AUTHORIZE, username=username, password=password)
        self.browser.get(basic_auth_link)