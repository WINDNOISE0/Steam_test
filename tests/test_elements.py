import os
from random import randint

import faker
import pytest

from expected_results.expected_results import AlertPageExpectedRes, ContextPageExpectedRes, HoversPageExpectedRes, \
    NewTabHandlersPageExpectedRes, NestedFramesPageExpectedRes, UploadPageExpectedRes
from helpers import UrlUtils, RandomUtils, FileUtils
from helpers.enpoints_urn import URN
from helpers.js_button import JsButton
from logger.logger import Logger
from pages.dynamic_c_page import DynamicCPage
from pages.frame_page import FramePage
from pages.h_slider_page import HSliderPage
from pages.alerts_page import AlertsPage
from pages.authorize_page import AuthorizePage
from pages.context_page import ContexPage
from pages.handlers_page import HandlersPage
from pages.hovers_page import HoversPage
from pages.nested_frames_page import NestedFramesPage
from pages.scroll_page import ScrollPage
from pages.upload_page import UploadPage
from test_config import TestConfig


class TestElements:
    AGE = 27
    FIND_TIMEOUT = 10

    @pytest.mark.parametrize("username, password", [
        (TestConfig.USERNAME, TestConfig.PASSWORD)
    ])
    def test_basic_auth(self, browser, username, password):
        authorize_page = AuthorizePage(browser)

        browser.get(UrlUtils.create_url(URN.AUTHORIZE))
        authorize_link = UrlUtils.create_basic_auth_link(URN.AUTHORIZE, username=username, password=password)

        browser.get(authorize_link)

        assert authorize_page.is_loaded(), "Authorize not successful, header no visible"

    @pytest.mark.parametrize("button_name", [
        (JsButton.ALERT),
        (JsButton.CONFIRM),
        (JsButton.PROMPT),
    ])
    def test_click_alerts(self, browser, button_name):
        test_word = None
        if button_name == JsButton.PROMPT:
            test_word = faker.Faker().word()

        alerts_page = AlertsPage(browser)
        browser.get(UrlUtils.create_url(URN.JS_ALERTS))
        assert alerts_page.is_loaded(), "No open alerts page"

        alerts_page.click_button(button_name)

        expected = AlertPageExpectedRes(button_name, test_word)

        assert expected.data.alert_expected_text == alerts_page.actual_alert_text, \
            f"Expected alert text: '{expected.data.alert_expected_text}' not matched actual text: '{alerts_page.actual_alert_text}'"

        alerts_page.click_ok_alert_button(test_word)

        assert expected.data.result_expected_text == alerts_page.actual_result_text, \
            f"Expected alert text: '{expected.data.result_expected_text}' not matched actual text: '{alerts_page.actual_result_text}'"

    @pytest.mark.parametrize("button_name", [
        (JsButton.ALERT),
        (JsButton.CONFIRM),
        (JsButton.PROMPT),
    ])
    def test_js_click_alerts(self, browser, button_name):
        test_word = None
        if button_name == JsButton.PROMPT:
            test_word = faker.Faker().word()

        alerts_page = AlertsPage(browser)
        browser.get(UrlUtils.create_url(URN.JS_ALERTS))
        assert alerts_page.is_loaded(), "No open alerts page"

        alerts_page.js_click_button(button_name)

        expected = AlertPageExpectedRes(button_name, test_word)

        assert expected.data.alert_expected_text == alerts_page.actual_alert_text, \
            f"Expected alert text: '{expected.data.alert_expected_text}' not matched actual text: '{alerts_page.actual_alert_text}'"

        alerts_page.js_click_ok_alert_button(test_word)

        assert expected.data.result_expected_text == alerts_page.actual_result_text, \
            f"Expected alert text: '{expected.data.result_expected_text}' not matched actual text: '{alerts_page.actual_result_text}'"

    def test_select_context_menu(self, browser):
        context_page = ContexPage(browser)
        browser.get(UrlUtils.create_url(URN.CONTEX_MENU))
        assert context_page.is_loaded(), "No open context page"

        expected = ContextPageExpectedRes()

        context_page.right_hot_spot_click()
        assert context_page.actual_alert_text == expected.alert_text, \
            f"Expected alert text: '{context_page.actual_alert_text}' not matched actual text: '{expected.alert_text}'"

        context_page.click_ok_alert_button()
        assert browser.is_alert_closed(), "Alert no close"

    def test_set_random_slider_value(self, browser):
        h_slider_page = HSliderPage(browser)
        browser.get(UrlUtils.create_url(URN.HORIZONTAL_SLIDER))
        assert h_slider_page.is_loaded(), "No open slider page"

        expected_value = RandomUtils.get_random_value_with_step(h_slider_page.min_hover_value,
                                                                h_slider_page.max_hover_value,
                                                                h_slider_page.hover_step_value)

        h_slider_page.set_hover_value(expected_value)
        assert expected_value == h_slider_page.actual_hover_state_vale, \
            f"Expected hover state: {expected_value} not matched actual value: {h_slider_page.actual_hover_state_vale}"

    def test_hover_random_user(self, browser):
        hovers_page = HoversPage(browser)
        browser.get(UrlUtils.create_url(URN.HOVERS))
        assert hovers_page.is_loaded(), "No open Hover page"

        expected_user_number = randint(1, hovers_page.user_count)
        hovers_page.hover_random_user(expected_user_number)

        assert expected_user_number == hovers_page.get_actual_user_number(expected_user_number), \
            f"Expected card name: {expected_user_number} not matched actual value: {hovers_page.get_actual_user_number(expected_user_number)}"

        hovers_page.click_view_profile(expected_user_number)
        """Здесь при открытии страницы ошибка, поэтому можно только линку проверить"""
        expected = HoversPageExpectedRes(expected_user_number)
        assert expected.user_link == hovers_page.actual_user_link, \
            f"Expected user link: {expected.user_link} not matched actual link: {hovers_page.actual_user_link}"

    def test_switch_handlers(self, browser):
        main_handlers_page = HandlersPage(browser)
        browser.get(UrlUtils.create_url(URN.HANDLERS))
        assert main_handlers_page.is_loaded(), "No opem handlers page"

        Logger.info("""\n\n    ======================== Open first page ==========================    \n\n""")

        first_window = main_handlers_page.open_new_tab()
        first_window_id = self.browser.current_window_handle
        browser.switch_to_handle_window(first_window_id)
        assert first_window.is_loaded(), "No open new handlers page"

        expected = NewTabHandlersPageExpectedRes()
        first_window_title = self.browser.get_window_title()
        assert expected.title == first_window_title, \
            f"Expected window title: {expected.title} no mathc actual: {first_window_title}"

        self.browser.switch_to_default_window()
        assert main_handlers_page.is_loaded(), "No return to main handler page from first tab"

        Logger.info("""\n\n    ======================== Open second page ==========================    \n\n""")

        second_window = main_handlers_page.open_new_tab()
        second_window_id = self.browser.current_window_handle
        assert second_window.is_loaded(), "No open new handlers page"

        second_window_title = self.browser.get_window_title()
        assert expected.title == second_window_title, \
            f"Expected window title: {expected.title} no mathc actual: {second_window_title}"

        self.browser.switch_to_default_window()
        assert main_handlers_page.is_loaded(), "No return to main handler page from second tab"

        browser.switch_to_handle_window(first_window_id)
        browser.close()
        assert first_window_id not in browser.window_handles, "first tab is no close"

        browser.switch_to_handle_window(second_window_id)
        browser.close()
        assert second_window_id not in browser.window_handles, "second tab is no close"

    def test_switch_frame(self, browser):
        frames_page = FramePage(browser)
        browser.get("https://demoqa.com/frames")
        assert frames_page.is_loaded(), "No open frames page"

        frames_page.select_nested_frames_menu_item()
        nested_frames_page = NestedFramesPage(browser)
        assert nested_frames_page.is_loaded(), "No open nested frames page"

        expected = NestedFramesPageExpectedRes()

        nested_frames_page.switch_to_parent_frame()
        assert expected.parent_frame_text == nested_frames_page.actual_parent_text, \
            f"Expected text:'{expected.parent_frame_text}' not match actual '{nested_frames_page.actual_parent_text}'"

        nested_frames_page.switch_to_child_frame()
        assert expected.child_frame_text == nested_frames_page.actual_child_text, \
            f"Expected text:'{expected.child_frame_text}' not match actual '{nested_frames_page.actual_child_text}'"

        self.browser.switch_to_default_frame()

        nested_frames_page.select_menu_item_frame()
        assert frames_page.is_loaded(), "No open frames page"

        assert frames_page.actual_big_frame_text == frames_page.actual_small_frame_text, \
            f"Text big frame: '{frames_page.actual_big_frame_text}' not match small frame:'{frames_page.actual_small_frame_text}'"

    def test_match_img_after_refresh(self, browser):
        dynamic_c_page = DynamicCPage(browser)
        browser.get(UrlUtils.create_url(URN.DYNAMIC_CONTENT))
        assert dynamic_c_page.is_loaded(), "No open Dynamic c page"

        dynamic_c_page.refresh_and_compare_two_images(find_timeout=self.FIND_TIMEOUT)
        assert dynamic_c_page.count_images != dynamic_c_page.count_primary_image, \
            f"There is no duplicate on the page for: {self.FIND_TIMEOUT} sec. page update"

    def test_scroll_down_to_age(self, browser):
        scroll_page = ScrollPage(browser)
        browser.get(UrlUtils.create_url(URN.INFINITE_SCROLL))
        assert scroll_page.is_loaded(), "No open scroll page"

        scroll_page.scroll_to_tab_count_age(self.AGE)
        assert self.AGE == scroll_page.count_tab, \
            f"Expected tab: {self.AGE}, but got: {scroll_page.count_tab}"

    def test_load_file_from_select(self, browser):
        upload_page = UploadPage(browser)
        browser.get(UrlUtils.create_url(URN.UPLOADS))
        assert upload_page.is_loaded(), "No open upload page"

        random_file_path = FileUtils.get_random_file(FileUtils.get_folder_path("files_folder"))
        expected_file_name = os.path.basename(random_file_path)

        upload_page.upload_file_from_select(random_file_path)
        assert expected_file_name == upload_page.actual_file_name, \
            f"Expected file name: {expected_file_name} not match {upload_page.actual_file_name}"

    def test_load_file_from_system_window(self, browser):
        upload_page = UploadPage(browser)
        browser.get(UrlUtils.create_url(URN.UPLOADS))
        assert upload_page.is_loaded(), "No open upload page"

        random_file_path = FileUtils.get_random_file(FileUtils.get_folder_path("files_folder"))
        aut2exe_path = os.getenv("AUT2EXE_PATH")
        expected = UploadPageExpectedRes()

        upload_page.upload_file_autoit_click(random_file_path, aut2exe_path)
        assert expected.check_mark == upload_page.actual_check_mark_text, \
            f"Expected mark text :{expected.check_mark} not match {upload_page.actual_check_mark_text}"

    def test_upload_file_hide_input(self, browser):
        upload_page = UploadPage(browser)
        browser.get(UrlUtils.create_url(URN.UPLOADS))
        assert upload_page.is_loaded(), "No open upload page"

        random_file_path = FileUtils.get_random_file(FileUtils.get_folder_path("files_folder"))
        expected = UploadPageExpectedRes()

        upload_page.upload_file_hide_input(random_file_path)
        assert expected.check_mark == upload_page.actual_check_mark_text, \
            f"Expected mark text :{expected.check_mark} not match {upload_page.actual_check_mark_text}"
