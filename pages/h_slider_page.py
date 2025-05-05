from elements.slider import Slider
from elements.web_element import WebElement

from pages.base_page import BasePage


class HSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'Horizontal Slider')]"

    HOVER_LOC = "//input[@type='range']"
    ACTUAL_HOVER_STATE_LOC = "range"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC)
        self.slider = Slider(browser, self.HOVER_LOC)

        self.hover_state = WebElement(self.browser, self.ACTUAL_HOVER_STATE_LOC)

    def set_hover_value(self, value):
        self.slider.set_slider_value(value)

    @property
    def actual_hover_state_vale(self):
        return float(self.hover_state.get_text())

    @property
    def min_hover_value(self):
        return self.slider.get_attribute("min")

    @property
    def max_hover_value(self):
        return self.slider.get_attribute("max")

    @property
    def hover_step_value(self):
        return self.slider.get_attribute("step")
