from elements.base_element import BaseElement
from logger.logger import Logger


class Slider(BaseElement):
    def set_slider_value(self, value):
        slider = self.wait_for_presence()
        Logger.info(f"{self}: set slider value '{value}'")
        self.browser.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", slider,
            value)