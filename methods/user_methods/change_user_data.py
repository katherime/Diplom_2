import requests
from data import base_url_stellar_burgers, data_about_user_endpoint
from methods.user_methods.login_user import LoginUser
import allure


class ChangeUserData:

    @allure.step('Изменение информации через PATCH запрос.')
    def change_data_about_user(self, payload, header):
        response = requests.patch(f"{base_url_stellar_burgers}{data_about_user_endpoint}",
                                  data=payload, headers=header)
        return response

    @allure.step('Метод изменения и ввода данных авторизованного пользователя')
    def change_fields_data_user_with_authorization(self, create_new_user_and_return_data, change_field, change_value):
        login_user_methods = LoginUser()
        change_methods = ChangeUserData()
        login_response = login_user_methods.login_user(create_new_user_and_return_data)
        header = {
            "Authorization": login_response.json()["accessToken"],
            change_field: change_value
        }
        response_change = change_methods.change_data_about_user(login_response, header)
        return response_change
