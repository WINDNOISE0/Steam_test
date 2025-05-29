from typing import Self

from browser.browser import Browser
from elements.web_element import WebElement
from logger.logger import Logger


class MultiWebElement:
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

    def __len__(self) -> int:
        count = 0
        for _ in self:
            count += 1
        Logger.info(f"{self}: count = {count}")
        return count
