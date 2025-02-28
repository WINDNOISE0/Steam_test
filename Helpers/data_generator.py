from faker import Faker


class DataGenerator:
    faker = Faker()

    def get_random_username(self):
        return self.faker.user_name()

    def get_random_password(self):
        return self.faker.password()
