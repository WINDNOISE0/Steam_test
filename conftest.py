import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    url = "https://store.steampowered.com/"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    driver.get(url)
    driver.maximize_window()

    yield driver

    driver.quit()
