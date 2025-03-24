from enum import Enum


class SortFilter(str, Enum):
    RELEVANCE = "relevance"
    RELEASE_DATA = "release_data"
    NAME = "name"
    PRICE_DESC = "price_desc"
    PRICE_ASC = "price_asc"
    USER_REVIEWS = "user_reviews"
