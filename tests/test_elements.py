import pytest

from helpers.js_button import JsButton
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
    @pytest.mark.parametrize("username, password", [
        (TestConfig.USERNAME, TestConfig.PASSWORD)
    ])
    def test_basic_auth(self, browser, username, password):
        authorize_page = AuthorizePage(browser)
        authorize_page.authorize(username, password)
        assert authorize_page.is_authorize_successful(), "Authorize not successful, header no visible"

    @pytest.mark.parametrize("button_name", [
        (JsButton.ALERT),
        (JsButton.CONFIRM),
        (JsButton.PROMPT),
    ])
    def test_click_alerts(self, browser, button_name):
        alerts_page = AlertsPage(browser)
        assert alerts_page.is_loaded(), "No open alerts page"

        alerts_page.click_button(button_name)
        assert alerts_page.is_alert_text_correctly(
            button_name), f"Expected alert text: '{alerts_page.BUTTONS[button_name].alert_expected_text}' not matched actual text: '{alerts_page.alert_text}'"

        alerts_page.click_ok_alert_button()
        assert alerts_page.is_result_text_correctly(
            button_name), f"Expected result text: '{alerts_page.BUTTONS[button_name].result_expected_text}' not matched actual text: '{alerts_page.result_text}'"

    @pytest.mark.parametrize("button_name", [
        (JsButton.ALERT),
        (JsButton.CONFIRM),
        (JsButton.PROMPT),
    ])
    def test_js_click_alerts(self, browser, button_name):
        alerts_page = AlertsPage(browser)
        assert alerts_page.is_loaded(), "No open alerts page"

        alerts_page.js_click_button(button_name)
        assert alerts_page.is_alert_text_correctly(button_name), \
            f"Expected alert text: '{alerts_page.BUTTONS[button_name].alert_expected_text}' not matched actual text: '{alerts_page.alert_text}'"

        alerts_page.js_click_ok_alert_button()
        assert alerts_page.is_result_text_correctly(button_name), \
            f"Expected result text: '{alerts_page.BUTTONS[button_name].result_expected_text}' not matched actual text: '{alerts_page.result_text}'"

    def test_select_context_menu(self, browser):
        context_page = ContexPage(browser)
        assert context_page.is_loaded(), "No open context page"

        context_page.right_hot_spot_click()
        assert context_page.actual_alert_text == context_page.expected_alert_text, \
            f"Expected alert text: '{context_page.actual_alert_text}' not matched actual text: '{context_page.expected_alert_text}'"

        context_page.click_ok_alert_button()
        assert context_page.is_alert_closed(), "Alert no close"

    def test_set_random_slider_value(self, browser):
        h_slider_page = HSliderPage(browser)
        assert h_slider_page.is_loaded(), "No open actions page"

        h_slider_page.set_random_hover_value()
        assert h_slider_page.expected_hover_state_value == h_slider_page.actual_hover_state_vale, \
            f"Expected hover state: {h_slider_page.expected_hover_state_value} not matched actual value: {h_slider_page.actual_hover_state_vale}"

    def test_hover_random_user(self, browser):
        hovers_page = HoversPage(browser)
        assert hovers_page.is_loaded(), "No open Hover page"

        hovers_page.hover_random_user()
        assert hovers_page.expected_user_name == hovers_page.actual_user_name, \
            f"Expected user name: {hovers_page.expected_user_name} not matched actual value: {hovers_page.actual_user_name}"

        hovers_page.click_view_profile()
        """Здесь при открытии страницы ошибка, поэтому можно только линку проверить"""
        assert hovers_page.expected_user_link == hovers_page.actual_user_link, \
            f"Expected user link: {hovers_page.expected_user_link} not matched actual link: {hovers_page.actual_user_link}"

    def test_switch_handlers(self, browser):
        main_handlers_page = HandlersPage(browser)
        assert main_handlers_page.is_loaded(), "No opem handlers page"

        first_tab = main_handlers_page.open_new_tab()

        assert first_tab.is_loaded(), "No open new handlers page"
        assert first_tab.is_correct_title_name(), \
            f"Expected window title: {first_tab.expected_title} no mathc actual: {first_tab.actual_title}"

        first_tab.come_back_main_page()
        assert main_handlers_page.is_loaded(), "No return to main handler page from first tab"

        second_tab = main_handlers_page.open_new_tab()

        assert second_tab.is_loaded(), "No open new handlers page"
        assert second_tab.is_correct_title_name(), \
            f"Expected window title: {second_tab.expected_title} no mathc actual: {second_tab.actual_title}"

        second_tab.come_back_main_page()
        assert main_handlers_page.is_loaded(), "No return to main handler page from second tab"

        first_tab.close_tab()
        assert main_handlers_page.is_closed_new_tab(first_tab.handle_id), "first tab is no close"

        second_tab.close_tab()
        assert main_handlers_page.is_closed_new_tab(second_tab.handle_id), "second tab is no close"

    def test_switch_frame(self, browser):
        frames_page = FramePage(browser)
        assert frames_page.is_loaded(), "No open frames page"

        frames_page.select_nested_frames()
        nested_frames_page = NestedFramesPage(browser)
        assert nested_frames_page.is_loaded(), "No open nested frames page"

        assert nested_frames_page.is_correct_parent_frame_text(), \
            f"Expected text:'{nested_frames_page.expected_parent_text}' not match actual '{nested_frames_page.actual_parent_text}'"
        assert nested_frames_page.is_correct_child_frame_text(), \
            f"Expected text:'{nested_frames_page.expected_child_text}' not match actual '{nested_frames_page.actual_child_text}'"

        nested_frames_page.select_frame()
        assert frames_page.is_loaded(), "No open frames page"
        assert frames_page.is_match_frame_text(), \
            f"text big frame: '{frames_page.actual_big_frame_text}' not match small frame:'{frames_page.actual_small_frame_text}'"

    def test_match_img_after_update(self, browser):
        dynamic_c_page = DynamicCPage(browser)
        assert dynamic_c_page.is_loaded(), "No open Dynamic c page"

        dynamic_c_page.update_page_until_two_img_mathc()
        assert dynamic_c_page.is_img_mathc(), \
            f"There is {dynamic_c_page.count_primary_img} primary img from {dynamic_c_page.count_img} on the page"

    def test_scroll_down_to_old(self, browser):
        scroll_page = ScrollPage(browser)
        assert scroll_page.is_loaded(), "No open scroll page"

        scroll_page.scroll_to_tab_count_old()
        assert scroll_page.is_count_tab_match_old(), \
            f"Expected tab: {scroll_page.old}, but got: {scroll_page.actual_count_tab}"

    def test_load_file_from_select(self, browser):
        upload_page = UploadPage(browser)
        assert upload_page.is_loaded(), "No open upload page"

        upload_page.upload_file_from_select()
        assert upload_page.is_correct_file_load_name(),\
            f"Expected file name: {upload_page.expected_file_name} not match {upload_page.actual_file_name}"

    def test_load_file_from_system_window(self, browser):
        upload_page = UploadPage(browser)
        assert upload_page.is_loaded(), "No open upload page"

        upload_page.upload_file_autoit_click()
        assert upload_page.is_correct_file_load_dr_dr_click(), \
            f"Expected mark text :{upload_page.expected_check_mark_text} not match {upload_page.actual_check_mark_text}"


    def test_load_file_drag_drop_action(self, browser):
        upload_page = UploadPage(browser)
        assert upload_page.is_loaded(), "No open upload page"

        upload_page.upload_file_drag_drop()
        assert upload_page.is_correct_file_load_dr_dr_click(), \
            f"Expected mark text :{upload_page.expected_check_mark_text} not match {upload_page.actual_check_mark_text}"


