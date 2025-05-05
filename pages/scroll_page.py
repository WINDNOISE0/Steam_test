from elements.label import Label
from elements.multy_web_element import MultyWebElement
from pages.base_page import BasePage


class ScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Infinite Scroll')]"
    TAB_ITEM_LOC = "(//div[contains(@class, 'jscroll-inner')]//div)[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)
        self.tab_item = MultyWebElement(browser, self.TAB_ITEM_LOC)

    def scroll_to_tab_count_age(self, age):
        self.tab_item.scroll_into_view(age)

    @property
    def actual_count_tab(self):
        return self.tab_item.get_count_item_tag()
