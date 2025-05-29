import math
import random

from faker import Faker


class RandomUtils:
    faker = Faker()

    @staticmethod
    def get_random_value_with_step(min_value, max_value, step=1.0):
        min_val = float(min_value)
        max_val = float(max_value)
        step = float(step)

        steps_count = int(math.floor((max_val - min_val) / step)) + 1
        random_index = random.randint(0, steps_count - 1)

        return round(min_val + step * random_index, 2)

    @staticmethod
    def get_random_username():
        return RandomUtils.faker.user_name()

    @staticmethod
    def get_random_password():
        return RandomUtils.faker.password()
