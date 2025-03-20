from seleniumbase.common.exceptions import TimeoutException
import re

from elements.button import Button
from elements.multy_element import MultyElement
from elements.web_element import WebElement
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
        "low_price": "//a[@id='Price_ASC']",
        "height_price": "//a[@id='Price_DESC']",
        "user_reviews": "//a[@id='Reviews_DESC']",
    }

    SORT_TEG = "#search_resultsRows a"
    PRICE_SORT_TEG = ".discount_final_price"


    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="SearchPage -> Filter Dropdown U")

        self.sort_dropdown = WebElement(self.browser, self.SORT_DROPDOWN, description="SearchPage -> Filter Dropdown")
        self.data_panel = MultyElement(self.browser, self.DATA_PANEL, description="SearchPage -> Data panel")


    def is_opened(self):
        try:
            self.wait_for_open()
            return True
        except TimeoutException:
            return False

    def select_sort_locator(self, locator_name:str):
        return self.SORT_ITEM[locator_name]

    def select_filter(self, filter_name):
        self.sort_dropdown.click()
        filter_locator = self.select_sort_locator(filter_name)
        filter_button = Button(self.browser, filter_locator)
        filter_button.click()

    def get_didgit_price(self, price:str) -> str:
        clean_price = ''.join(char for char in price if char.isdigit() or char in [",", "."])
        return clean_price.replace(",", ".")

    def is_sorted_product_list(self, price_count, reverse=False):
        prices = []

        items = self.data_panel.get_soup_multy_element(self.SORT_TEG)
        for i, item in enumerate(items):
            if i >= price_count:
                break

            price_element = item.select_one(self.PRICE_SORT_TEG)
            if price_element:

                price_text = price_element.get_text(strip=True)

                if not re.search(r'\d', price_text):
                    price = 0.0
                else:
                    price = float(self.get_didgit_price(price_text))

                Logger.info(f"{price}")
                prices.append(price)

        return prices == sorted(prices, reverse=reverse)

