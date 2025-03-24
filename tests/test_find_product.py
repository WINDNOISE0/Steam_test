import pytest

from helpers.sort_filter import SortFilter
from helpers.test_data import FindTestData
from pages.main_page import MainPage
from pages.search_page import SearchPage


class TestFindProduct:
    @pytest.mark.parametrize("sort_filter_type, count_price_validate, sorted_param",
                             [
                                 (SortFilter.PRICE_ASC, 10, FindTestData.WITCHER),
                                 (SortFilter.PRICE_ASC, 20, FindTestData.FALLOUT),
                             ])
    def test_find_and_sort_witcher(self, browser, sort_filter_type, count_price_validate, sorted_param):
        main_page = MainPage(browser)
        search_page = SearchPage(browser)

        main_page.find_game(sorted_param)
        assert search_page.is_loaded(), "No open Search page"

        search_page.select_filter(sort_filter_type)
        assert search_page.is_sorted_product_list(count_price_validate,
                                                  reverse=True), f'{str(search_page)} no sorted with {sort_filter_type} teg'
