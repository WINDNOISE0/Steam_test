from Base.BaseElement import BaseElement
from Helpers.asserts import Asserts
from types import SimpleNamespace
from Helpers.data_generator import DataGenerator


class BasePage:
    def __init__(self, driver, locators=None, elements_=None):
        self.driver = driver
        self.asserts = Asserts()
        self.data_generator = DataGenerator()

        self.locators = SimpleNamespace(**(locators or {}))
        self.elements = SimpleNamespace(**(elements_ or {}))

    def create_element_dct(self):
        for element_name, locator_name in self.locators.__dict__.items():
            setattr(self.elements, element_name, BaseElement(self.driver, locator_name))

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def current_link(self):
        return self.driver.current_url

    def get_locator(self, locator_name):
        return getattr(self.locators, locator_name)
