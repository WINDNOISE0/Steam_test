from elements.button import Button
from elements.label import Label

from helpers.enpoints_urn import URN
from helpers.helper_tools import HelperTools
from pages.base_page import BasePage


class DynamicCPage(BasePage):
    URL = HelperTools.create_url(URN.DYNAMIC_CONTENT)

    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'Dynamic Content')]"

    UPDATE_BUTTON_LOC = "//a[contains(text(), 'click here')]"

    ATTRIBUTE_NAME = "src"
    COUNT_IMG = 3
    img_number = None

    def __init__(self, browser):
        super().__init__(browser)
        self.open_page(self.URL)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)
        self.update_button = Button(browser, self.UPDATE_BUTTON_LOC)
        self._img_match_set_len = None

    def update_page_until_two_img_mathc(self):
        while True:
            self.update_button.click()

            img_match_set = set()

            for i in range(1, self.COUNT_IMG + 1):

                self.img_number = i
                current_img_link = Label(self.browser, self.img_loc).get_attribute(self.ATTRIBUTE_NAME)
                img_match_set.add(current_img_link)

            if len(img_match_set) >= 1:
                self._img_match_set_len = len(img_match_set)
                break

    def is_img_mathc(self):
        return self._img_match_set_len >= 1

    @property
    def count_primary_img(self):
        return self._img_match_set_len

    @property
    def count_img(self):
        return self.COUNT_IMG

    @property
    def img_loc(self):
        return f"(//div[@id='content']//img)[{self.img_number}]"







