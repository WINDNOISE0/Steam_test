import time

from bs4 import BeautifulSoup
from seleniumbase.common.exceptions import TimeoutException

from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class DynamicCPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Dynamic Content')]"

    UPDATE_BUTTON_LOC = "//a[contains(text(), 'click here')]"
    IMAGES_LOC = "(//div[contains(@class, 'large-2 columns')])"
    LINK_IMAGE_LOC = "(//div[contains(@class, 'large-2 columns')]/img)[{}]"
    DATA_PANEL_LOC = "content"
    CONTAINER_TAG = "img"

    ATTRIBUTE_NAME = "src"
    TIMEOUT_FIND_ELEMENT = 10
    TIMEOUT_STOP_FIND_ELEMENT = 20

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)
        self.update_button = Button(browser, self.UPDATE_BUTTON_LOC)
        self.data_panel = WebElement(browser, self.DATA_PANEL_LOC)

    def get_links_list(self) -> list:
        links_list = []

        try:
            self.is_loaded()

            soup = BeautifulSoup(self.data_panel.get_attribute("innerHTML"), "html.parser")
            tags_group = soup.find_all(self.CONTAINER_TAG)

            for tag in tags_group:
                value = tag.get(self.ATTRIBUTE_NAME)
                if value:
                    links_list.append(value)

            return links_list

        except TimeoutException as error:
            Logger.error(f"{self}: timeout after {self.DEFAULT_TIMEOUT}s while waiting for data panel content")
            raise error

    def refresh_and_compare_two_images(self, find_timeout=TIMEOUT_STOP_FIND_ELEMENT):
        start = time.time()
        while time.time() - start < find_timeout:

            all_link_list = self.get_links_list()
            if len(all_link_list) < len(set(all_link_list)):
                break
            else:
                self.update_button.click()

    @property
    def count_images(self):
        return len(self.get_links_list())

    @property
    def count_primary_image(self):
        return len(set(self.get_links_list()))
