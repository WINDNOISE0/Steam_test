from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from helpers.enpoints_urn import URN
from helpers.helper_tools import HelperTools
from pages.base_page import BasePage


class UploadPage(BasePage):
    URL = HelperTools.create_url(URN.UPLOADS)

    UNIQUE_ELEMENT_LOC = "//div[@id='content']//*[contains(text(), 'File Uploader')]"

    SELECT_FILE_BUTTON_LOC = "file-upload"
    UPLOAD_FILE_BUTTON_LOC = "file-submit"
    LOAD_FILE_NAME_LOC = "uploaded-files"
    FILE_FOLDERS_PATH = r"C:\Users\1\Desktop\QA\Auto\Steam_test"
    DRAG_DROP_AREA_LOC = "drag-drop-upload"
    CHECK_MARK_LOC = "//div[@id='drag-drop-upload']//div[@class='dz-success-mark']//span"
    DRAG_DROP_INPUT_LOC = "//input[@class='dz-hidden-input']"

    ADD_FILE_SCRIPT = r"\simple_file_load"


    EXPECTED_CHECK_MARK_TEXT = "✔"

    def __init__(self, browser):
        super().__init__(browser)

        self.open_page(self.URL)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC)

        self.select_file_button = Input(browser, self.SELECT_FILE_BUTTON_LOC)
        self.upload_file_button = Button(browser, self.UPLOAD_FILE_BUTTON_LOC)
        self.drag_drop_area = Button(browser, self.DRAG_DROP_AREA_LOC)
        self.drag_drop_input = Input(browser, self.DRAG_DROP_INPUT_LOC)

        self.load_file_name = Label(browser, self.LOAD_FILE_NAME_LOC)

        self._actual_file_name = None
        self._file_name = None

        self._actual_check_mark_text = None

    def upload_file_from_select(self):
        random_file_path = HelperTools.get_random_file(self.FILE_FOLDERS_PATH)
        self._file_name = HelperTools.get_file_name(random_file_path)

        self.select_file_button.send_keys(random_file_path)
        self.upload_file_button.click()

    def upload_file_autoit_click(self):
        self.drag_drop_area.click()

        HelperTools.add_file_to_browser(self.ADD_FILE_SCRIPT)
        self._file_name = HelperTools.get_file_name_from_autoit_script(self.ADD_FILE_SCRIPT)

    def upload_file_drag_drop(self):
        random_file_path = HelperTools.get_random_file(self.FILE_FOLDERS_PATH)
        self._file_name = HelperTools.get_file_name(random_file_path)

        self.drag_drop_input.send_drag_drop_file_key(random_file_path)
        self.drag_drop_input.click_and_hold()

        self.drag_drop_input.move_to_element_release(self.drag_drop_area.get_element())


    def is_correct_file_load_dr_dr_click(self):
        self._actual_check_mark_text = WebElement(self.browser, self.CHECK_MARK_LOC).get_text()
        return self._actual_check_mark_text == self.EXPECTED_CHECK_MARK_TEXT

    def is_correct_file_load_name(self):
        self._actual_file_name = self.load_file_name.get_text()
        return self._file_name == self._actual_file_name

    @property
    def expected_file_name(self):
        return self._file_name

    @property
    def actual_file_name(self):
        return self._actual_file_name

    @property
    def expected_check_mark_text(self):
        return self.EXPECTED_CHECK_MARK_TEXT

    @property
    def actual_check_mark_text(self):
        return self._actual_check_mark_text

