from datetime import datetime
from faker import Faker
from pytz import timezone

pst = timezone("Europe/Berlin")
email = None


class DataGenerator:

    @staticmethod
    def generate_email():
        global email
        email = "test_" + str(datetime.now(pst).strftime('%H%M%S-%d%m%y')) + "@caner.com"
        print("Generated email: {}".format(email))
        return email

    @staticmethod
    def generate_first_name():
        return Faker().first_name()

    @staticmethod
    def generate_last_name():
        return Faker().last_name()


def generate_random_integer(min_int, max_int):
    return Faker().random.randint(min_int, max_int)
