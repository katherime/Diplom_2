import requests
import allure
from data import base_url_stellar_burgers, create_user_endpoint, data_about_user_endpoint


class CreateUser:

    @allure.step('Создание нового пользователя через POST запрос.')
    def create_new_user(self, payload):
        response = requests.post(f"{base_url_stellar_burgers}{create_user_endpoint}", data=payload)
        return response

    @allure.step('Создание нового пользователя и получение accessToken при удачной авторизации')
    def create_new_user_and_return_accesstoken(self, payload):
        response = requests.post(f"{base_url_stellar_burgers}{create_user_endpoint}", data=payload)
        data = response.json()
        return {"Authorization": data["accessToken"]}

    @allure.step('Создание нового пользователя и получение refreshToken при удачной авторизации')
    def create_new_user_and_return_refreshtoken(self, payload):
        response = requests.post(f"{base_url_stellar_burgers}{create_user_endpoint}", data=payload)
        data = response.json()
        return data["refreshToken"]

    @allure.step('Удаление пользователя через DELETE запрос')
    def delete_user(self, payload):
        response = requests.delete(f"{base_url_stellar_burgers}{data_about_user_endpoint}", data=payload)
        return response
