from elements.base_element import BaseElement
from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[@id='framesWrapper']//*[text()='Nested Frames']"

    PARENT_FRAME_LOC = "frame1"
    CHILD_IFRAME_LOC = "//iframe[@srcdoc='<p>Child Iframe</p>']"

    FRAMES_MENU_ITEM_LOC = "//span[text() = 'Frames']"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)

        self.frames_button = Button(browser, self.FRAMES_MENU_ITEM_LOC)

        self._parent_frame = WebElement(self.browser, self.PARENT_FRAME_LOC)
        self.parent_frame_body = WebElement(self.browser, "//body")

        self._child_iframe = WebElement(self.browser, self.CHILD_IFRAME_LOC)
        self.child_iframe_body = WebElement(self.browser, "//body")

    def switch_to_frame(self, frame: BaseElement):
        self.browser.switch_to_frame(frame)

    def select_menu_item_frame(self):
        self.browser.switch_to_default_frame()
        self.frames_button.click()

    @property
    def parent_frame(self):
        return self._parent_frame

    @property
    def child_iframe(self):
        return self._child_iframe

    @property
    def actual_parent_text(self):
        return self.parent_frame_body.get_text()

    @property
    def actual_child_text(self):
        return self.child_iframe_body.get_text()
