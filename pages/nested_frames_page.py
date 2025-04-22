from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[@id='framesWrapper']//*[text()='Nested Frames']"

    PARENT_FRAME_LOC = "frame1"
    PARENT_FRAME_TEXT = "Parent frame"

    CHILD_IFRAME_LOC = "//iframe[@srcdoc='<p>Child Iframe</p>']"
    CHILD_IFRAME_TEXT = "Child Iframe"

    FRAMES_BUTTON_LOC = "//span[text() = 'Frames']"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)

        self.frames_button = Button(browser, self.FRAMES_BUTTON_LOC)

        self._actual_parent_frame_text = None
        self._actual_child_iframe_text = None


    def is_correct_parent_frame_text(self):
        parent_frame = WebElement(self.browser, self.PARENT_FRAME_LOC)
        self.browser.switch_to_frame(parent_frame)

        self._actual_parent_frame_text = WebElement(self.browser, "//body").get_text()

        return self._actual_parent_frame_text == self.PARENT_FRAME_TEXT

    def is_correct_child_frame_text(self):
        child_iframe = WebElement(self.browser, self.CHILD_IFRAME_LOC)
        self.browser.switch_to_frame(child_iframe)

        self._actual_child_iframe_text= WebElement(self.browser, "//body").get_text()

        return self._actual_child_iframe_text == self.CHILD_IFRAME_TEXT

    def select_frame(self):
        self.browser.switch_to_default_frame()
        self.frames_button.click()

    @property
    def expected_parent_text(self):
        return self.PARENT_FRAME_TEXT

    @property
    def expected_child_text(self):
        return self.CHILD_IFRAME_TEXT

    @property
    def actual_parent_text(self):
        return self._actual_parent_frame_text

    @property
    def actual_child_text(self):
        return self._actual_child_iframe_text
