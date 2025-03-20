from singeltone_driver.singelton_driver import SingeltoneDriver


class TestOne:
    def test_one(self, driver):
        assert 1 == 1

    def test_two(self, driver):
        assert 1 == 1

    def test_three(self, driver):
        assert 1 == 1
        SingeltoneDriver().quit_driver()

    def test_four(self, driver):
        assert 1 == 1

    def test_five(self, driver):
        assert 1 == 1
