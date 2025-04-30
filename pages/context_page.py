from elements.web_element import WebElement
from pages.base_page import BasePage


class ContexPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'Context Menu')]"
    HOT_SPOT = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC)
        self.hot_spot = WebElement(browser, self.HOT_SPOT)

    def right_hot_spot_click(self):
        self.hot_spot.right_click()

    def click_ok_alert_button(self):
        self.browser.switch_to_alert().accept()

    @property
    def actual_alert_text(self):
        return self.browser.get_alert_text()
