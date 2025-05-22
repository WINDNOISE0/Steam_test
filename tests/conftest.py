import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager  # НЕ нужно, если драйвер уже есть в образе

from browser.browser import Browser


@pytest.fixture()
def browser():
    load_dotenv()

    options = Options()
    options.add_argument("--headless")  # 🔹 Headless режим
    options.add_argument("--no-sandbox")  # 🔹 Безопасный режим — отключаем (нужно в Docker)
    options.add_argument("--disable-dev-shm-usage")  # 🔹 Для Docker: shared memory issue
    options.add_argument("--window-size=1920,1080")  # 🔹 Размер окна

    # Если ты внутри Docker и драйвер уже есть — не нужно ChromeDriverManager
    driver = webdriver.Chrome(options=options)

    browser = Browser(driver)
    yield browser
    browser.quit()
