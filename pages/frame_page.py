from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement

from pages.base_page import BasePage


class FramePage(BasePage):
    URL = "https://demoqa.com/frames"

    UNIQUE_ELEMENT_LOC = "//div[@id='framesWrapper']//*[text()='Frames']"
    NESTED_FRAMES_BUTTON_LOC = "//span[contains(text(), 'Nested Frames')]"

    FRAME_TEXT_LOC = "sampleHeading"

    BIG_FRAME_LOC = "frame1"
    SMALL_FRAME_LOC = "frame2"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)
        self.nested_frames_button = Button(browser, self.NESTED_FRAMES_BUTTON_LOC)

        self.open_page(self.URL)

        self._actual_big_frame_text = None
        self._actual_small_frame_text = None

    def select_nested_frames(self):
        self.nested_frames_button.js_click()

    def is_match_frame_text(self):
        big_frame = WebElement(self.browser, self.BIG_FRAME_LOC)
        self.browser.switch_to_frame(big_frame)
        self._actual_big_frame_text = WebElement(self.browser, self.FRAME_TEXT_LOC).get_text()

        self.browser.switch_to_default_frame()

        small_frame = WebElement(self.browser, self.SMALL_FRAME_LOC)
        self.browser.switch_to_frame(small_frame)
        self._actual_small_frame_text = WebElement(self.browser, self.FRAME_TEXT_LOC).get_text()

        return self._actual_big_frame_text == self._actual_small_frame_text

    def select_frame_section(self):
        self.nested_frames_button.click()

    @property
    def actual_big_frame_text(self):
        return self._actual_big_frame_text

    @property
    def actual_small_frame_text(self):
        return self._actual_small_frame_text
