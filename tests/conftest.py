import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from browser.browser import Browser


@pytest.fixture()
def browser():
    url = "https://store.steampowered.com/"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    browser = Browser(driver)
    browser.get(url)

    yield browser

    browser.quit()
