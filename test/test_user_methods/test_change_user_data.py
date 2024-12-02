from methods.user_methods.login_user import LoginUser
import allure
import pytest
from data import ResponseTexts
from methods.user_methods.change_user_data import ChangeUserData


class TestChangeDataUser:

    @allure.title('Проверка изменение данных пользователя с авторизацией')
    def test_change_data_user_with_authorization(self, create_new_user_and_return_data):
        login_user_methods = LoginUser()
        change_methods = ChangeUserData()
        login_response = login_user_methods.login_user(create_new_user_and_return_data)
        header = {"Authorization": login_response.json()["accessToken"]}
        response_change = change_methods.change_data_about_user(login_response, header)
        assert response_change.status_code == 200

    @allure.title('Проверка изменения данных пользователя с авторизацией c изменением разных полей')
    @pytest.mark.parametrize("change_field, change_value", [
        ("email", "test1@mail.ru"),
        ("password", "a1a1a1a")
    ])
    def test_change_data_user(self, create_new_user_and_return_data, change_field, change_value):
        change_methods = ChangeUserData()
        response = change_methods.change_fields_data_user_with_authorization(create_new_user_and_return_data,
                                                                             change_field,
                                                                             change_value)
        assert response.status_code == 200

    @allure.title('Проверка изменение данных пользователя без авторизации')
    def test_change_data_user_no_authorization(self, create_new_user_and_return_data):
        login_user_methods = LoginUser()
        change_methods = ChangeUserData()
        login_response = login_user_methods.login_user(create_new_user_and_return_data)
        header = {"Authorization": ''}
        response_change = change_methods.change_data_about_user(login_response, header)
        assert response_change.status_code == 401 and response_change.json() == ResponseTexts.response_no_authorization
