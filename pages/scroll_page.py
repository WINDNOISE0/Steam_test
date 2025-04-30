from elements.label import Label
from elements.multy_web_element import MultyWebElement
from pages.base_page import BasePage


class ScrollPage(BasePage):
    TAB_ITEM_LOC = "//div[@class='jscroll-inner']//div"

    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'Infinite Scroll')]"

    def __init__(self, browser):
        super().__init__(browser)

        self.tab_item = MultyWebElement(browser, self.TAB_ITEM_LOC)

        self.count_paragraph = None
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)

    def scroll_to_tab_count_age(self, age):
        while True:
            self._wait.until(
                lambda driver: driver.execute_script(
                    "return document.body.scrollHeight > window.innerHeight"
                )
            )

            self.browser.scroll_page_down()

            self.count_paragraph = self.tab_item.get_count_item_teg()

            if self.count_paragraph == age:
                break

    @property
    def actual_count_tab(self):
        return self.count_paragraph
