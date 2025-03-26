import pytest
from singeltone_driver.singleton_driver import SingletonDriver


@pytest.fixture()
def driver():
    driver = SingletonDriver()
    yield driver

    SingletonDriver.quit_driver()