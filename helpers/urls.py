from helpers.enpoints_urn import URN
from test_config import TestConfig

class UrlUtils:
    @staticmethod
    def get_protocol(secure=False):
        return "https://" if secure else "http://"

    @staticmethod
    def create_url(urn: URN):
        return f"{UrlUtils.get_protocol()}{TestConfig.HOST}/{urn}"

    @staticmethod
    def create_basic_auth_link(urn: URN, username="username", password="password"):
        return f"{UrlUtils.get_protocol()}{username}:{password}@{TestConfig.HOST}/{urn}"
