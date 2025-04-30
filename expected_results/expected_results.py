from dataclasses import dataclass, field

from helpers import UrlUtils
from helpers.data_class import AlertPageData
from helpers.js_button import JsButton
from test_config import TestConfig


@dataclass
class AlertPageExpectedRes:
    button_name: str
    test_name: str
    buttons: dict = field(default_factory=
                          lambda: {
                              JsButton.ALERT: AlertPageData(alert_expected_text="I am a JS Alert",
                                                            result_expected_text="You subccessfuly clicked an alert"),
                              JsButton.CONFIRM: AlertPageData(alert_expected_text="I am a JS Confirm",
                                                              result_expected_text="You clicked: Ok"),
                              JsButton.PROMPT: AlertPageData(alert_expected_text="I am a JS prompt",
                                                             result_expected_text="You entered: {}")

                          })

    @property
    def data(self):
        if self.button_name == JsButton.PROMPT:
            self.buttons[self.button_name].result_expected_text = self.buttons[
                self.button_name].result_expected_text.format(self.test_name)

        return self.buttons[self.button_name]


@dataclass
class ContextPageExpectedRes:
    alert_text = "You selected a context menu"


@dataclass
class HoversPageExpectedRes:
    user_number: int
    user_link: str = field(init=False)

    def __post_init__(self):
        self.user_link = f"{UrlUtils.get_protocol(secure=True)}{TestConfig.HOST}/users/{str(self.user_number)}"


@dataclass
class NewTabHandlersPageExpectedRes:
    title = "New Window"


@dataclass
class NestedFramesPageExpectedRes:
    parent_frame_text = "Parent frame"
    child_frame_text = "Child Iframe"


@dataclass
class UploadPageExpectedRes:
    check_mark = "✔"
