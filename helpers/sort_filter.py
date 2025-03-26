from enum import StrEnum


class SortFilter(StrEnum):
    RELEVANCE = "relevance"
    RELEASE_DATA = "release_data"
    NAME = "name"
    PRICE_DESC = "price_desc"
    PRICE_ASC = "price_asc"
    USER_REVIEWS = "user_reviews"
