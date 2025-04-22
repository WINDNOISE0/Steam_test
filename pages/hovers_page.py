from random import randint

from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from helpers.enpoints_urn import URN
from helpers.helper_tools import HelperTools
from logger.logger import Logger
from pages.base_page import BasePage
from test_config import TestConfig


class HoversPage(BasePage):
    URL = HelperTools.create_url(URN.HOVERS)
    USER_COUNT = 3

    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'Hovers')]"

    USER_CARD_LOC = "(//img[@alt='User Avatar'])["

    USER_LINK_LOC = "//a[@href='/users/"
    USERNAME_LOC =  "(//div[@class='figcaption'])//*[contains(text(), 'name: user"

    EXPECTED_CARD_TEXT = "name: user"
    EXPECTED_LINK = f"{HelperTools.get_http(secure=True)}{TestConfig.HOST}/users/"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC)
        self.open_page(self.URL)

        self._expected_user_name = None
        self._expected_user_link = None

        self.user_name_loc = None
        self.card_loc = None
        self.user_number = None


    def hover_random_user(self):
        self.user_number = randint(1, self.USER_COUNT)
        Logger.info(str(self.user_number))

        self._expected_user_name = f"{self.EXPECTED_CARD_TEXT}{self.user_number}"
        Logger.info(self._expected_user_name)

        self.card_loc = f"{self.USER_CARD_LOC}{self.user_number}]"
        Logger.info(self.card_loc)

        Label(self.browser, self.card_loc).move_to_element()

    def click_view_profile(self):
        self._expected_user_link = f"{self.USER_LINK_LOC}{self.user_number}']"
        Button(self.browser, self._expected_user_link).click()


    @property
    def expected_user_name(self):
        return self._expected_user_name

    @property
    def expected_user_link(self):
        return f"{self.EXPECTED_LINK}{self.user_number}"

    @property
    def actual_user_name(self):
        return Label(self.browser, f"{self.USERNAME_LOC}{self.user_number}')]").get_text()

    @property
    def actual_user_link(self):
        return self.get_current_link()

















