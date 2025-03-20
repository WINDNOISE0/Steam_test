from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading

class SingeltoneDriver:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(SingeltoneDriver, cls).__new__(cls)
                    cls._instance.driver = cls._create_driver()
        return cls._instance

    @staticmethod
    def _create_driver():
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            SingeltoneDriver._instance = None