from bs4 import BeautifulSoup

from elements.label import Label
from elements.multy_web_element import MultiWebElement
from elements.web_element import WebElement

from pages.base_page import BasePage


class ScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Infinite Scroll')]"
    TAB_ITEM_LOC = "(//div[contains(@class, 'jscroll-inner')]//div)[{}]"
    DATA_PANEL_LOC = "//div[contains(@class, 'jscroll-inner')]"
    CONTAINER_TAG = "div"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)
        self.tab_item = MultiWebElement(browser, self.TAB_ITEM_LOC)
        self.data_panel = WebElement(browser, self.DATA_PANEL_LOC)

    def get_count_tag(self):
        soup = BeautifulSoup(self.data_panel.get_attribute("innerHTML"), "html.parser")
        count_tags = len(soup.find_all(self.CONTAINER_TAG))

        return count_tags

    def scroll_to_tab_count_age(self, age):
        for element in self.tab_item:

            if self.get_count_tag() == age:
                break

            element.scroll_to_element()
