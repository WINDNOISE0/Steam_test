from seleniumbase.common.exceptions import TimeoutException
import re

from elements.button import Button
from elements.multy_element import MultyElement
from elements.web_element import WebElement
from helpers.sort_filter import SortFilter
from logger.logger import Logger
from pages.base_page import BasePage


class SearchPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//a[@id='sort_by_trigger']"

    SORT_DROPDOWN = "//a[@id='sort_by_trigger']"
    DATA_PANEL = "//div[@id='search_resultsRows']"
    SORT_ITEM = {
        "relevance": "//a[@id='_ASC']",
        "release_data": "//a[@id='Released_DESC']",
        "name": "//a[@id='Name_ASC']",
        "price_desc": "//a[@id='Price_ASC']",
        "price_asc": "//a[@id='Price_DESC']",
        "user_reviews": "//a[@id='Reviews_DESC']",
    }

    CONTAINER_ITEM = "//div[@id='search_resultsRows']"
    PRICE_CONTAINER_TEG = "//div[@class='discount_final_price']"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="SearchPage -> Filter Dropdown U")

        self.sort_buttons = {
            filter_type: Button(browser, locator)
            for filter_type, locator in self.SORT_ITEM.items()
        }

        self.sort_dropdown = WebElement(self.browser, self.SORT_DROPDOWN, description="SearchPage -> Filter Dropdown")
        self.data_panel = MultyElement(self.browser, self.DATA_PANEL, self.CONTAINER_ITEM, self.PRICE_CONTAINER_TEG,
                                       description="SearchPage -> Data panel")


    def select_filter(self, filter_type: SortFilter):
        self.sort_dropdown.click()
        filter_button = self.sort_buttons[filter_type]
        filter_button.click()

    def is_sorted_product_list(self, price_count, reverse=False):
        try:
            self.is_loaded()
            price_list = self.data_panel.get_price_list()[:price_count + 1]
            return price_list == sorted(price_list, reverse=reverse)
        except TimeoutException:
            raise TimeoutException
