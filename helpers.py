from faker import Faker
def generate_new_user_data():
        faker = Faker()
        data = {
                "email": faker.ascii_free_email(),
                "password": faker.password(),
                "name": faker.user_name()
        }
        return data

data_for_old_user = {
        "email": "test@yandex.ru",
        "password": "123456",
        "name": "test"
}

data_wrong_mew_user = {
        "email": "test1111111137111@yandex.ru",
        "password": "",
        "name": "test"
}