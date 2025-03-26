import time

from bs4 import BeautifulSoup
from seleniumbase.common.exceptions import TimeoutException

from elements.button import Button
from elements.web_element import WebElement
from helpers.helper_tools import HelperTools
from helpers.sort_filter import SortFilter
from logger.logger import Logger
from pages.base_page import BasePage


class SearchPage(BasePage):
    UNIQUE_ELEMENT_LOC = "sort_by_trigger"
    SORT_DROPDOWN = "sort_by_trigger"
    DATA_PANEL = "search_resultsRows"

    SORT_ITEM = {
        "relevance": "_ASC",
        "release_data": "Released_DESC",
        "name": "Name_ASC",
        "price_desc": "Price_ASC",
        "price_asc": "Price_DESC",
        "user_reviews": "Reviews_DESC",
    }

    PRICE_CONTAINER_TEG = ".discount_final_price"

    def __init__(self, browser):
        super().__init__(browser)


        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="SearchPage -> Filter Dropdown U")
        self.sort_buttons = {
            filter_type: Button(browser, locator)
            for filter_type, locator in self.SORT_ITEM.items()
        }

        self.sort_dropdown = WebElement(self.browser, self.SORT_DROPDOWN, description="SearchPage -> Filter Dropdown")


        self.data_panel = WebElement(self.browser, self.DATA_PANEL, description="SearchPage -> Data panel")

    def select_filter(self, filter_type: SortFilter):
        self.sort_dropdown.click()
        filter_button = self.sort_buttons[filter_type]
        filter_button.click()

    def get_price_list(self, price_count: int) -> list:
        price_list = []

        try:
            self.is_loaded()
            soup = BeautifulSoup(self.data_panel.get_attribute("innerHTML"), "html.parser")
            prices = soup.select(self.PRICE_CONTAINER_TEG)

            for price_teg in prices[:price_count]:

                price_list.append(HelperTools.get_digit_price(price_teg.text))

        except TimeoutException:
            Logger.error(f"{self} {self.DEFAULT_TIMEOUT} sec. is expired for waiting")

        return price_list
