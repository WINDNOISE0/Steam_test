import time

from elements.button import Button
from elements.label import Label
from elements.multy_web_element import MultyWebElement
from pages.base_page import BasePage


class DynamicCPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Dynamic Content')]"

    UPDATE_BUTTON_LOC = "//a[contains(text(), 'click here')]"
    IMAGES_LOC = "(//div[contains(@class, 'large-2 columns')])"
    LINK_IMAGE_LOC = "(//div[contains(@class, 'large-2 columns')]/img)[{}]"

    ATTRIBUTE_NAME = "src"
    TIMEOUT_FIND_ELEMENT = 1
    TIMEOUT_STOP_FIND_ELEMENT = 20

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)
        self.update_button = Button(browser, self.UPDATE_BUTTON_LOC)
        self.images = MultyWebElement(browser, self.LINK_IMAGE_LOC, timeout=self.TIMEOUT_FIND_ELEMENT)

    def refresh_and_compare_two_images(self, find_timeout=TIMEOUT_STOP_FIND_ELEMENT):
        start = time.time()
        while time.time() - start < find_timeout:

            all_link_list = self.images.get_attributes_list(self.ATTRIBUTE_NAME)
            if len(all_link_list) < len(set(all_link_list)):
                break

            else:
                self.update_button.click()

    @property
    def count_images(self):
        return len(self.images.get_attributes_list(self.ATTRIBUTE_NAME))

    @property
    def count_primary_image(self):
        return len(set(self.images.get_attributes_list(self.ATTRIBUTE_NAME)))
