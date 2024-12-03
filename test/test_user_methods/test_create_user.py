import pytest
from helpers import data_for_old_user
from methods.user_methods.create_new_user import CreateUser
from helpers import generate_new_user_data
from data import ResponseTexts
import allure


class TestCreateUser:

    @allure.title('Проверка создания нового пользователя')
    def test_create_new_user(self):
        create_user_methods = CreateUser()
        payload = generate_new_user_data()
        response = create_user_methods.create_new_user(payload)
        assert response.status_code == 200 and ResponseTexts.response_success in response.text

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    def test_create_already_exist_user(self):
        create_user_methods = CreateUser()
        payload = data_for_old_user
        response = create_user_methods.create_new_user(payload)
        assert response.status_code == 403 and response.json() == ResponseTexts.response_user_already_exist

    @pytest.mark.parametrize("email, password, name", [
        ('test@yandex.ru', '', 'Test'),
        ('test@yandex.ru', '123456', ''),
        ('', '123456', 'Test')])
    @allure.title('Проверка создания пользователя при незаполненном поле email/password/name')
    def test_create_user_with_empty_fields(self, email, password, name):
        create_user_methods = CreateUser()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = create_user_methods.create_new_user(payload)
        assert response.status_code == 403 and response.json() == ResponseTexts.response_empty_fields
