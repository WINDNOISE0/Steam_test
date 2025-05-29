from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='framesWrapper']//*[text()='Nested Frames']"

    PARENT_FRAME_LOC = "frame1"
    CHILD_IFRAME_LOC = "//iframe[@srcdoc='<p>Child Iframe</p>']"

    FRAMES_MENU_ITEM_LOC = "//span[text() = 'Frames']"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)

        self.frames_button = Button(browser, self.FRAMES_MENU_ITEM_LOC)

        self.parent_frame = WebElement(self.browser, self.PARENT_FRAME_LOC)
        self.parent_frame_body = WebElement(self.browser, "//body")

        self.child_iframe = WebElement(self.browser, self.CHILD_IFRAME_LOC)
        self.child_iframe_body = WebElement(self.browser, "//body")

    def switch_to_parent_frame(self):
        self.browser.switch_to_frame(self.parent_frame)

    def switch_to_child_frame(self):
        self.browser.switch_to_frame(self.child_iframe)

    def select_menu_item_frame(self):
        self.frames_button.click()

    @property
    def parent_text(self):
        return self.parent_frame_body.get_text()

    @property
    def child_text(self):
        return self.child_iframe_body.get_text()
