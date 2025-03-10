from types import SimpleNamespace

from browser.browser import Browser
from logger.logger import Logger


class BasePage:
    """
    Если правильно понял, нужен для проверки нахождения на конкретной странице? Сделал с симплнейсмейс,
    пока решил не удалять
    """
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, browser: Browser, locators: dict = None):
        self.browser = browser
        self.page_name = None
        self.unique_element = None

        self.locators = SimpleNamespace(**(locators or {}))

    def wait_for_open(self) -> None:
        Logger.info(f"{self}: wait for open")
        self.unique_element.wait_for_presence()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.page_name}]"

    def __repr__(self) -> str:
        return str(self)
