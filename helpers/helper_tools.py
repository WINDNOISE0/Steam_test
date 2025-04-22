from helpers.enpoints_urn import URN
from test_config import TestConfig
import os
import random
import subprocess




class HelperTools:
    SCRIPTS_FOLDER = r"C:\Users\1\Desktop\QA\Auto\Steam_test\scripts"

    @staticmethod
    def get_digit_price(price: str) -> float:
        clean_price = ''.join(char for char in price if char.isdigit() or char in [",", "."])
        if not clean_price:
            return 0.0
        return float(clean_price.replace(",", "."))

    @staticmethod
    def get_http(secure=False):
        if secure:
            protocol = "https://"
        else:
            protocol = "http://"

        return protocol

    @staticmethod
    def create_url(urn: URN):
        protocol = HelperTools.get_http()
        return f"{protocol}{TestConfig.HOST}/{urn}"


    @staticmethod
    def create_basic_auth_link(urn: URN, username="username", password="password"):
        protocol = HelperTools.get_http()

        url = f"{protocol}{username}:{password}@{TestConfig.HOST}/{urn}"
        return url

    @staticmethod
    def get_random_file(path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        if not files:
            raise FileNotFoundError("No files found in the directory.")
        return os.path.join(path, random.choice(files))

    @staticmethod
    def get_file_name(file_path:str):
        return os.path.basename(file_path)

    @classmethod
    def get_file_name_from_autoit_script(cls, script_name):
        with open(f"{cls.SCRIPTS_FOLDER}{script_name}.au3", "r") as file:
            file_s = file.readlines()
            for line in file_s:
                if "\\" in line or "/" in line:
                    file_name = os.path.basename(line.strip())

        return file_name

    @classmethod
    def add_file_to_browser(cls, file_name):
        subprocess.call(f"{cls.SCRIPTS_FOLDER}{file_name}.exe")








