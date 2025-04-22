import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from browser.browser import Browser
from test_config import TestConfig


@pytest.fixture(scope="class")
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    browser = Browser(driver)

    yield browser

    browser.quit()
