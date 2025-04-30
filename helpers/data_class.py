from dataclasses import dataclass


@dataclass
class AlertPageData:
    alert_expected_text: str
    result_expected_text: str