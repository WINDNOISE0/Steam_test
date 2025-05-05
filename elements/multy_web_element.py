from typing import Self

from browser.browser import Browser
from elements.web_element import WebElement
from logger.logger import Logger


class MultyWebElement:
    DEFAULT_TIMEOUT = 10

    def __init__(
            self,
            browser: Browser,
            formatable_xpath: str,
            description: str = None,
            timeout: int = DEFAULT_TIMEOUT
    ):
        self.index = 1

        self.browser = browser
        self.formatable_xpath = formatable_xpath
        self.timeout = timeout
        self.description = description if description else self.formatable_xpath.format("'i'")

    def __iter__(self) -> Self:
        self.index = 1
        return self

    def __next__(self) -> WebElement:
        current_element = WebElement(
            self.browser,
            self.formatable_xpath.format(self.index),
            f"{self.description}[{self.index}]",
            timeout=self.timeout)

        if not current_element.is_exists():
            raise StopIteration
        else:
            self.index += 1
            return current_element

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)

    def get_count_item_tag(self) -> int:
        count = 0
        for _ in self:
            count += 1
        Logger.info(f"{self}: count = {count}")
        return count

    def get_attributes_list(self, attribute_name: str) -> list:
        attributes_list = []
        for element in self:
            Logger.info(f"{self}: get list values of attribute: {attribute_name}")
            attributes_list.append(element.get_attribute(attribute_name))

        return attributes_list

    def scroll_into_view(self, count_element):
        for element in self:
            if self.index == count_element:
                break

            Logger.info(f"{self}: scroll element ")
            self.browser.execute_script("arguments[0].scrollIntoView();", element.get_selenium_element())
