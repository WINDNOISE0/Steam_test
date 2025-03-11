from faker import Faker


class DataGenerator:
    faker = Faker()

    @staticmethod
    def get_random_username():
        return DataGenerator.faker.user_name()

    @staticmethod
    def get_random_password():
        return DataGenerator.faker.password()
