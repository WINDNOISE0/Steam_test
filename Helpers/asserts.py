
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Helpers.logger import Logger
from settings import Settings


class Asserts:
    timeout = Settings.get_timeout()
    locator_type = Settings.get_locator_type()

    @staticmethod
    def item_validate_str(first_param, second_param):
        assert first_param == second_param, f'{first_param} !=  {second_param}'

    @classmethod
    def element_is_visible(cls, driver, locator_name, locator, current_url):
        Logger.info(f"Проверка отображения {locator_name} началась")

        element = WebDriverWait(driver, cls.timeout).until(
            EC.visibility_of_element_located((cls.locator_type, locator))
        ),
        try:
            assert element, f"Элемент {locator_name} не найден за {cls.timeout} секунд на странице {current_url}"
        except AssertionError:
            Logger.error(f"Проверка отображения {locator_name} провалена")
        else:
            Logger.info(f"Проверка отображения {locator_name} пройдена успешно")
