from selenium.webdriver.support.wait import WebDriverWait
from seleniumbase.common.exceptions import TimeoutException

from browser.browser import Browser
from logger.logger import Logger


class BasePage:
    UNIQUE_ELEMENT_LOC = None
    DEFAULT_TIMEOUT = 10

    def __init__(self, browser: Browser, timeout: int = DEFAULT_TIMEOUT):
        self.browser = browser
        self.timeout = timeout
        self.page_name = self.__class__.__name__
        self._wait = WebDriverWait(self.browser.driver, self.timeout)

        self.unique_element = None

    def wait_for_open(self) -> None:
        Logger.info(f"{self}: wait for open")
        self.unique_element.wait_for_presence()

    def wait_for_spa_loaded(self) -> None:
        self._wait.until(lambda driver: self.browser.driver.execute_script("return document.readyState") == "complete")
        self.wait_for_open()

    def is_loaded(self) -> bool:
        try:
            self.wait_for_spa_loaded()
            return True
        except TimeoutException:
            return False


    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.page_name}]"

    def __repr__(self) -> str:
        return str(self)
