import requests
import allure
from data import base_url_stellar_burgers, login_user_endpoint


class LoginUser:

    @allure.step('Логин пользователя через POST запрос.')
    def login_user(self, payload):
        response = requests.post(f"{base_url_stellar_burgers}{login_user_endpoint}", data=payload)
        return response

    @allure.step('Логин пользователя через POST запрос.')
    def login_user(self, payload):
        response = requests.post(f"{base_url_stellar_burgers}{login_user_endpoint}", data=payload)
        return response
