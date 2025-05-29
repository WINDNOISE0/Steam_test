from dataclasses import dataclass, field

from helpers.data_class import AlertPageData
from helpers.js_button import JsButton


@dataclass
class AlertPageExpectedRes:
    buttons: dict = field(default_factory=
                          lambda: {
                              JsButton.ALERT: AlertPageData(alert_expected_text="I am a JS Alert",
                                                            result_expected_text="You subccessfuly clicked an alert"),
                              JsButton.CONFIRM: AlertPageData(alert_expected_text="I am a JS Confirm",
                                                              result_expected_text="You clicked: Ok")

                          })


@dataclass
class ContextPageExpectedRes:
    alert_text = "You selected a context menu"


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
