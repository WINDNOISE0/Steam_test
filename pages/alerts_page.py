from elements.button import Button
from elements.web_element import WebElement
from helpers.js_button import JsButton
from pages.base_page import BasePage


class AlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'JavaScript Alerts')]"
    RESULT_LABEL_LOC = "result"

    ALERT_BUTTON_LOC = "//button[@onclick='jsAlert()']"
    CONFIRM_BUTTON_LOC = "//button[@onclick='jsConfirm()']"
    PROMPT_BUTTON_LOC = "//button[@onclick='jsPrompt()']"

    def __init__(self, browser, faker_word):
        super().__init__(browser)

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC)
        self.result_label = WebElement(self.browser, self.RESULT_LABEL_LOC)

        self.current_button = None

        self.faker_word = faker_word

        self.buttons_elements = {
            JsButton.ALERT: Button(browser, self.ALERT_BUTTON_LOC),
            JsButton.CONFIRM: Button(browser, self.CONFIRM_BUTTON_LOC),
            JsButton.PROMPT: Button(browser, self.PROMPT_BUTTON_LOC)
        }

    def click_button(self, button_name: JsButton):
        self.buttons_elements[button_name].click()
        self.current_button = button_name

    def js_click_button(self, button_name: JsButton):
        self.buttons_elements[button_name].js_click()
        self.current_button = button_name

    def click_ok_alert_button(self):
        if self.current_button == JsButton.PROMPT:
            self.browser.send_keys_alert(self.faker_word)

        self.browser.switch_to_alert().accept()

    def js_click_ok_alert_button(self):
        if self.current_button == JsButton.PROMPT:
            self.browser.send_keys_alert(self.faker_word)

        self.browser.switch_to_alert().accept()

    @property
    def actual_result_text(self):
        return self.result_label.get_text()

    @property
    def actual_alert_text(self):
        return self.browser.get_alert_text()
