import time

from bs4 import BeautifulSoup

from elements.base_element import BaseElement
from logger.logger import Logger


class MultyElement(BaseElement):
    FEATURES = "html.parser"

    def get_soup_multy_element(self, search_teg: str, parser: str = None):
        time.sleep(3)
        html = self.browser.get_page_source()

        if parser is None:
            parser = self.FEATURES

        try:
            Logger.info(f'{self} Start parsing HTML with selector: {search_teg}')
            soup = BeautifulSoup(html, parser)
            items = soup.select(search_teg)
        except Exception as err:
            raise Exception(f"Parsing HTML Error: {err}")

        Logger.info(f"{self} End parsing HTML")

        return items




