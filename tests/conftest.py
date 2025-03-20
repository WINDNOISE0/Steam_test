import pytest


from singeltone_driver.singelton_driver import SingeltoneDriver


@pytest.fixture()
def driver():
    driver = SingeltoneDriver().get_driver()
    print(id(driver))
    yield driver

