import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from browser.browser import Browser
from settings import Settngs_


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    browser = Browser(driver)
    browser.get(Settngs_.URL)

    yield browser

    browser.quit()
