import random

from faker import Faker


class RandomUtils:
    faker = Faker()

    @staticmethod
    def get_random_value_with_step(min_value, max_value, step):
        randint_value = random.randint(min_value, max_value)
        if random.randint(0, 1):
            randint_value = float(randint_value) + step
        return randint_value

    @staticmethod
    def get_random_username():
        return RandomUtils.faker.user_name()

    @staticmethod
    def get_random_password():
        return RandomUtils.faker.password()
