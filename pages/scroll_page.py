from elements.label import Label
from elements.web_element import WebElement
from helpers.enpoints_urn import URN
from helpers.helper_tools import HelperTools
from pages.base_page import BasePage


class ScrollPage(BasePage):
    URL = HelperTools.create_url(URN.INFINITE_SCROLL)
    OLD = 27
    COUNT_PIXEL_SCROLL = 200

    TAB_ITEM_LOC = "//div[@class='jscroll-inner']//div"

    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'Infinite Scroll')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.open_page(self.URL)

        self.tab_item = WebElement(browser, self.TAB_ITEM_LOC)

        self.count_paragraph = None
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)

    def scroll_to_tab_count_old(self):
        while True:
            self.wait_load_scroll_script()
            self.browser.scroll_down_page(self.COUNT_PIXEL_SCROLL)

            self.count_paragraph = self.tab_item.get_count_item_teg()

            if self.count_paragraph == self.OLD:
                break


    def is_count_tab_match_old(self):
        return self.count_paragraph == self.OLD

    @property
    def old(self):
        return self.OLD

    @property
    def actual_count_tab(self):
        return self.count_paragraph
