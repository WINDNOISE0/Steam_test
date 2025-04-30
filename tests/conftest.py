import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from browser.browser import Browser


@pytest.fixture(scope="class")
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    load_dotenv()

    browser = Browser(driver)

    yield browser

    browser.quit()
