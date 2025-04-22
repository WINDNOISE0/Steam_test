from selenium.common import NoAlertPresentException

from elements.web_element import WebElement
from helpers.enpoints_urn import URN
from helpers.helper_tools import HelperTools
from pages.base_page import BasePage


class ContexPage(BasePage):
    URL = HelperTools.create_url(URN.CONTEX_MENU)
    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'Context Menu')]"

    EXPECTED_ALERT_TEXT = "You selected a context menu"

    HOT_SPOT = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)

        self.open_page(self.URL)

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC)
        self.hot_spot = WebElement(browser, self.HOT_SPOT)

        self._alert_text = None


    def right_hot_spot_click(self):
        self.hot_spot.right_click()
        self._alert_text = self.browser.get_alert_text()


    def click_ok_alert_button(self):
        self.browser.switch_to_alert().accept()

    def is_alert_closed(self):
        try:
            self.browser.switch_to_alert(wait=False)
            return False
        except NoAlertPresentException:
            return True

    @property
    def expected_alert_text(self):
        return self.EXPECTED_ALERT_TEXT

    @property
    def actual_alert_text(self):
        return self._alert_text

