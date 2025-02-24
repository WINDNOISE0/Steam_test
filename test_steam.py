import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver_init():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def page(driver_init):
    new_page = NonPOMPage(driver_init)
    return new_page

@pytest.fixture(scope="session")
def url():
    url = "https://store.steampowered.com/"
    return url

class NonPOMPage:
    TIMEOUT = 5
    LOGIN = "adawdwd"
    PASSWORD = "12312w"

    login_global_button = "(//*[@id='global_actions']//a)[2]"
    login_url = "https://store.steampowered.com/login"

    login_input = "(//input[@type='text'])[1]"
    password_input = "//input[@type='password']"
    autorize_button = "//button[@type='submit']"
    autorize_loader = "(//button[@type='submit' and @disabled]//div)[1]"
    error_login_text = "(//form)//div[5][1]"


    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click_element(self, locator, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        ).click()

    def current_link(self):
        return self.driver.current_url

    def get_viewed_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )

    def input_text(self, locator, text, timeout=TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )
        element.clear()
        element.send_keys(text)


def test_login_steam(page, url):
    page.open_url(url)
    assert page.current_link() == url

    page.click_element(page.login_global_button)
    assert page.login_url in page.current_link()

    page.input_text(page.login_input, page.LOGIN)
    page.input_text(page.password_input, page.PASSWORD)
    page.click_element(page.autorize_button)
    page.get_viewed_element(page.autorize_loader)
    page.get_viewed_element(page.error_login_text)