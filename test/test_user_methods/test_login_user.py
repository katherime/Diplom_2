from methods.user_methods.login_user import LoginUser
import pytest
import allure
from data import ResponseTexts


class TestLoginUser:

    @allure.title('Проверка авторизации пользователя')
    def test_login_user(self, create_new_user_and_return_data):
        login_user_methods = LoginUser()
        login_response = login_user_methods.login_user(create_new_user_and_return_data)
        assert login_response.status_code == 200 and ResponseTexts.response_success in login_response.text

    @pytest.mark.parametrize("email, password", [
        ('test@yandex.ru', ''),
        ('', '123456')])
    @allure.title('Проверка авторизации пользователя с неверным email/паролем')
    def test_login_user_with_wrong_data(self, email, password):
        login_user_methods = LoginUser()
        data_for_login = {
            "email": email,
            "password": password
        }
        login_response = login_user_methods.login_user(data_for_login)
        assert login_response.status_code == 401 and ResponseTexts.response_wrong_data_for_login in login_response.text
