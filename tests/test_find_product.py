from helpers.test_data import FindTestData
from pages.main_page import MainPage
from pages.search_page import SearchPage



class TestFindProduct:
    def test_find_and_sort_witcher(self, browser):
        sort_filter_type = "low_price"
        count_price_validate = 10

        main_page = MainPage(browser)
        search_page = SearchPage(browser)

        main_page.find_game(FindTestData.WITCHER.value)
        assert search_page.is_opened(), "No open Search page"

        search_page.select_filter(sort_filter_type)
        assert search_page.is_sorted_product_list(count_price_validate, reverse=True)

    def test_find_and_sort_fallout(self, browser):
        sort_filter_type = "low_price"
        count_price_validate = 20

        main_page = MainPage(browser)
        search_page = SearchPage(browser)

        main_page.find_game(FindTestData.FALLOUT.value)
        assert search_page.is_opened(), "No open Search page"

        search_page.select_filter(sort_filter_type)
        assert search_page.is_sorted_product_list(count_price_validate, reverse=True)