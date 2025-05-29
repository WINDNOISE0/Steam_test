from elements.button import Button
from elements.input import Input
from elements.label import Label
from helpers.autoit import AutoItUtils
from pages.base_page import BasePage


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//*[contains(text(), 'File Uploader')]"

    SELECT_FILE_BUTTON_LOC = "file-upload"
    UPLOAD_FILE_BUTTON_LOC = "file-submit"
    LOAD_FILE_NAME_LOC = "uploaded-files"

    DRAG_DROP_AREA_LOC = "drag-drop-upload"
    CHECK_MARK_LOC = "//*[@id='drag-drop-upload']//*[contains(@class, 'dz-success-mark')]//span"
    DRAG_DROP_INPUT_LOC = "//input[@class='dz-hidden-input']"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)

        self.select_file_button = Input(browser, self.SELECT_FILE_BUTTON_LOC)
        self.upload_file_button = Button(browser, self.UPLOAD_FILE_BUTTON_LOC)
        self.drag_drop_area = Button(browser, self.DRAG_DROP_AREA_LOC)
        self.drag_drop_input = Input(browser, self.DRAG_DROP_INPUT_LOC)

        self.check_mark = Label(self.browser, self.CHECK_MARK_LOC)
        self.load_file_name = Label(browser, self.LOAD_FILE_NAME_LOC)

    def upload_file_from_select(self, file_path: str):
        self.select_file_button.send_keys(file_path)
        self.upload_file_button.click()

    def upload_file_autoit_click(self, file_path: str, aut2exe_path: str):
        self.drag_drop_area.click()
        AutoItUtils.perform_load_autoit_script(file_path, aut2exe_path)

    def upload_file_hide_input(self, file_path: str):
        self.drag_drop_input.send_keys(file_path, hide_element=True)

    @property
    def file_name(self):
        return self.load_file_name.get_text()

    @property
    def check_mark_text(self):
        return self.check_mark.get_text()
