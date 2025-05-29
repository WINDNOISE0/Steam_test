from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement

from pages.base_page import BasePage


class FramePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='framesWrapper']//*[text()='Frames']"
    NESTED_FRAMES_BUTTON_LOC = "//span[contains(text(), 'Nested Frames')]"

    FRAME_TEXT_LOC = "sampleHeading"

    BIG_FRAME_LOC = "frame1"
    SMALL_FRAME_LOC = "frame2"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)
        self.nested_frames_button = Button(browser, self.NESTED_FRAMES_BUTTON_LOC)

        self.big_frame = WebElement(self.browser, self.BIG_FRAME_LOC)
        self.frame_text = WebElement(self.browser, self.FRAME_TEXT_LOC)

        self.small_frame = WebElement(self.browser, self.SMALL_FRAME_LOC)

    def select_nested_frames_menu_item(self):
        self.nested_frames_button.js_click()

    @property
    def big_frame_text(self):
        self.browser.switch_to_frame(self.big_frame)
        frame_text = self.frame_text.get_text()
        self.browser.switch_to_default_frame()
        return frame_text

    @property
    def small_frame_text(self):
        self.browser.switch_to_frame(self.small_frame)
        frame_text = self.frame_text.get_text()
        self.browser.switch_to_default_frame()
        return frame_text
