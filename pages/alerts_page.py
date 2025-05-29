from elements.button import Button
from elements.web_element import WebElement
from helpers.js_button import JsButton
from pages.base_page import BasePage


class AlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'JavaScript Alerts')]"
    RESULT_LABEL_LOC = "result"

    ALERT_BUTTON_LOC = "//button[@onclick='jsAlert()']"
    CONFIRM_BUTTON_LOC = "//button[@onclick='jsConfirm()']"
    PROMPT_BUTTON_LOC = "//button[@onclick='jsPrompt()']"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC)
        self.result_label = WebElement(self.browser, self.RESULT_LABEL_LOC)

        self.buttons_elements = {
            JsButton.ALERT: Button(browser, self.ALERT_BUTTON_LOC),
            JsButton.CONFIRM: Button(browser, self.CONFIRM_BUTTON_LOC),
            JsButton.PROMPT: Button(browser, self.PROMPT_BUTTON_LOC)
        }

    def click_button(self, button_name: JsButton):
        self.buttons_elements[button_name].click()

    def click_prompt_button(self):
        self.buttons_elements[JsButton.PROMPT].click()

    def js_click_button(self, button_name: JsButton):
        self.buttons_elements[button_name].js_click()

    def js_click_prompt_button(self):
        self.buttons_elements[JsButton.PROMPT].js_click()

    def click_ok_alert_button(self):
        self.browser.switch_to_alert().accept()

    def click_ok_alert_prompt_button(self, test_word):
        self.browser.send_keys_alert(test_word)
        self.browser.switch_to_alert().accept()

    def js_click_ok_alert_button(self):
        self.browser.switch_to_alert().accept()

    def js_click_ok_alert_prompt_button(self, test_word):
        self.browser.send_keys_alert(test_word)
        self.browser.switch_to_alert().accept()

    @property
    def result_text(self):
        return self.result_label.get_text()

    @property
    def alert_text(self):
        return self.browser.get_alert_text()
