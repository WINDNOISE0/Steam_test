from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from settings import Settings


class BaseElement:
    timeout = Settings.get_timeout()
    locator_type = Settings.get_locator_type()

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def click_element(self, timeout=timeout):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((self.locator_type, self.locator))
        ).click()

    def get_viewed_element(self, timeout=timeout):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((self.locator_type, self.locator))
        )

    def input_text(self, text, auto_clean=True, timeout=timeout):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((self.locator_type, self.locator))
        )
        if auto_clean:
            element.clear()

        element.send_keys(text)

    def get_locator(self):
        return self.locator
