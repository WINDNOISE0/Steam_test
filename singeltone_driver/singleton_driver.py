from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SingletonDriver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            options = webdriver.ChromeOptions()
            cls._instance = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )
        return cls._instance

    @classmethod
    def quit_driver(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None