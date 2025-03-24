import re

from bs4 import BeautifulSoup

from browser.browser import Browser
from elements.base_element import BaseElement
from logger.logger import Logger


class MultyElement(BaseElement):
    """Как будто мультиэлемент нужно делать абстрактым и на его базе реализовывать подкалссы по типу
    PriceList(MultyElement) со своей особенностью реализации"""

    def __init__(
            self,
            browser: Browser,
            locator: str | tuple,
            container_locator: str,
            item_container_locator: str,
            description: str = None
    ):
        super().__init__(browser, locator, description)

        self.soup_item_list = self.create_soup_multy_element(container_locator)
        self.item_container_locator = item_container_locator

    def create_soup_multy_element(self, search_teg: str):
        html = self.browser.get_page_source()

        try:
            Logger.info(f'{self} Start parsing HTML with selector: {search_teg}')
            soup = BeautifulSoup(html, "html.parser")
            return soup.select(search_teg)
        except:
            Logger.error("Error parsing HTML")
            return []

    def get_price_list(self):
        price_list = []
        for item in self.soup_item_list:
            price_element = item.select_one(self.item_container_locator)
            if price_element:

                price_text = price_element.get_text(strip=True)

                if not re.search(r'\d', price_text):
                    price = 0.0
                else:
                    price = float(self.get_digit_price(price_text))

                Logger.info(f"{price}")
                price_list.append(price)

        return price_list
