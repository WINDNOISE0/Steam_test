from elements.web_element import WebElement
from helpers.enpoints_urn import URN
from helpers.helper_tools import HelperTools
from pages.base_page import BasePage


class AuthorizePage(BasePage):
    URL = HelperTools.create_url(URN.AUTHORIZE)

    UNIQUE_ELEMENT_LOC = "//div[@id='content']//p"


    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "basic_page -> page_header")

    def authorize(self, username, password):
        self.open_page(self.URL)
        basic_auth_link = HelperTools.create_basic_auth_link(URN.AUTHORIZE, username=username, password=password)
        self.open_page(basic_auth_link)

    def is_authorize_successful(self):
        return self.is_loaded()







