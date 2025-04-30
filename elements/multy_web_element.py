from selenium.webdriver.support import expected_conditions

from elements.base_element import BaseElement
from logger.logger import Logger


class MultyWebElement(BaseElement):
    def wait_for_visible_all(self) -> list:
        return self._wait_for(expected_condition=expected_conditions.presence_of_all_elements_located)


    def get_count_item_teg(self):
        elements_list = self.wait_for_visible_all()
        Logger.info(f"{len(elements_list)}")
        return len(elements_list)