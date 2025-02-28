from selenium.webdriver.common.by import By


class Settings:
    TIMEOUT = 20
    LOCATOR_FIND = By.XPATH

    @classmethod
    def get_timeout(cls):
        return cls.TIMEOUT

    @classmethod
    def get_locator_type(cls):
        return cls.LOCATOR_FIND
