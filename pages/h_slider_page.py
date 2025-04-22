from random import randint

from elements.web_element import WebElement
from helpers.enpoints_urn import URN
from helpers.helper_tools import HelperTools
from pages.base_page import BasePage


class HSliderPage(BasePage):
    URL = HelperTools.create_url(URN.HORIZONTAL_SLIDER)
    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'Horizontal Slider')]"

    HOVER_LOC = "//input[@type='range']"
    ACTUAL_HOVER_STATE_LOC = "range"
    MIN_HOVER_VALUE = 1
    MAX_HOVER_VALUE = 4
    HOVER_STEP = 0.5

    def __init__(self, browser):
        super().__init__(browser)

        self.open_page(self.URL)

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC)
        self.hover = WebElement(browser, self.HOVER_LOC)

        self._actual_hover_state_value = None
        self._expected_hover_state_value = None

    def set_random_hover_value(self):
        
        randint_value = randint(self.MIN_HOVER_VALUE, self.MAX_HOVER_VALUE)
        random_chapter = randint(0, 1)
        if random_chapter:
            randint_value = float(randint_value) + 0.5


        slider = self.hover.get_element()
        self.browser.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", slider, randint_value)

        self._expected_hover_state_value = randint_value
        self._actual_hover_state_value = float(WebElement(self.browser, self.ACTUAL_HOVER_STATE_LOC).get_text())

    @property
    def expected_hover_state_value(self):
        return self._expected_hover_state_value

    @property
    def actual_hover_state_vale(self):
        return self._actual_hover_state_value