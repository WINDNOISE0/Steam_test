import time

from elements.button import Button
from elements.label import Label
from elements.multy_web_element import MultyWebElement
from pages.base_page import BasePage


class DynamicCPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'Dynamic Content')]"

    UPDATE_BUTTON_LOC = "//a[contains(text(), 'click here')]"
    IMAGES_LOC = "//div[@class='large-2 columns']"
    LINK_IMAGE_LOC = "//div[@class='large-2 columns']/img"

    ATTRIBUTE_NAME = "src"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)
        self.update_button = Button(browser, self.UPDATE_BUTTON_LOC)
        self.images = MultyWebElement(browser, self.IMAGES_LOC)

        self._img_match_list = []
        self.index_same_element = None
        self._link_same_element = None

    def refresh_and_compare_two_images(self):
        count_image = self.images.get_count_item_teg()

        while True:
            for i in range(1, count_image + 1):
                current_img_link = Label(self.browser, f"({self.LINK_IMAGE_LOC}){[i]}").get_attribute(
                    self.ATTRIBUTE_NAME)
                if not current_img_link in self._img_match_list:
                    self._img_match_list.append(current_img_link)
                else:
                    self.index_same_element = self._img_match_list.index(current_img_link)
                    self._link_same_element = current_img_link
                    break

            self.update_button.click()
            time.sleep(1)
            self._img_match_list.clear()

    @property
    def first_same_element(self):
        return self._link_same_element

    @property
    def second_same_element(self):
        return self._img_match_list[self.index_same_element]
