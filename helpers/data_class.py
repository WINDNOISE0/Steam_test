from dataclasses import dataclass


@dataclass
class AlertPageData:
    button_locator: str
    alert_expected_text: str
    result_expected_text: str