from faker import Faker
from elements.button import Button
from elements.web_element import WebElement
from helpers.data_class import AlertPageData
from helpers.enpoints_urn import URN
from helpers.helper_tools import HelperTools
from helpers.js_button import JsButton
from pages.base_page import BasePage


class AlertsPage(BasePage):
    faker_word = Faker().word()

    URL = HelperTools.create_url(URN.JS_ALERTS)

    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'JavaScript Alerts')]"
    RESULT_TEXT_LOC = "result"

    BUTTONS = {
        JsButton.ALERT: AlertPageData(button_locator="//button[@onclick='jsAlert()']",
                                      alert_expected_text="I am a JS Alert",
                                      result_expected_text="You subccessfuly clicked an alert"),
        JsButton.CONFIRM: AlertPageData(button_locator="//button[@onclick='jsConfirm()']",
                                        alert_expected_text="I am a JS Confirm",
                                        result_expected_text="You clicked: Ok"),
        JsButton.PROMPT: AlertPageData(button_locator="//button[@onclick='jsPrompt()']",
                                       alert_expected_text="I am a JS prompt",
                                       result_expected_text=f"You entered: {faker_word}")
    }

    def __init__(self, browser):
        super().__init__(browser)

        self.open_page(self.URL)
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC)
        self._alert_text = None
        self._result_text = None

        self.current_button = None

        self.buttons_elements = {
            JsButton.ALERT: Button(browser, self.BUTTONS[JsButton.ALERT].button_locator),
            JsButton.CONFIRM: Button(browser, self.BUTTONS[JsButton.CONFIRM].button_locator),
            JsButton.PROMPT: Button(browser, self.BUTTONS[JsButton.PROMPT].button_locator)
        }

    def click_button(self, button_name: JsButton):
        self.buttons_elements[button_name].click()
        self.current_button = button_name
        self._alert_text = self.browser.get_alert_text()


    def js_click_button(self, button_name: JsButton):
        self.buttons_elements[button_name].js_click()
        self.current_button = button_name
        self._alert_text = self.browser.get_alert_text()

    def click_ok_alert_button(self):
        if self.current_button == JsButton.PROMPT:
            self.browser.send_keys_alert(self.faker_word)

        self.browser.switch_to_alert().accept()
        self._result_text = WebElement(self.browser, self.RESULT_TEXT_LOC).get_text()

    def js_click_ok_alert_button(self):
        if self.current_button == JsButton.PROMPT:
            self.browser.send_keys_alert(self.faker_word)

        self.browser.switch_to_alert().accept()
        self._result_text = WebElement(self.browser, self.RESULT_TEXT_LOC).get_text()

    def is_alert_text_correctly(self, button_name: JsButton):
        actual_alert_text = self.browser.get_alert_text()
        expected_alert_text = self.BUTTONS[button_name].alert_expected_text
        return actual_alert_text == expected_alert_text

    def is_result_text_correctly(self, button_name: JsButton):
        actual_result_text = self._result_text
        expected_result_text = self.BUTTONS[button_name].result_expected_text
        return expected_result_text == actual_result_text

    @property
    def result_text(self):
        return self._result_text

    @property
    def alert_text(self):
        return self._alert_text
