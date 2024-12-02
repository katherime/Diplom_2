import requests
import random
import allure
from data import base_url_stellar_burgers, create_order_endpoint, data_about_ingridients_endpoint


class CreateOrder:

    @allure.step('Получение данных об ингредиентах через GET-запрос')
    def get_info_about_ingredient(self):
        response = requests.get(f"{base_url_stellar_burgers}{data_about_ingridients_endpoint}")
        return response

    @allure.step('Создание заказа через POST-запрос')
    def create_order(self, payload):
        response = requests.post(f"{base_url_stellar_burgers}{create_order_endpoint}", data=payload)
        return response

    @allure.step('Получение хешей 3х рандомных ингредиентов из списка доступных')
    def get_hash_of_three_random_ingredients(self):
        create_order = CreateOrder()
        response = create_order.get_info_about_ingredient()
        ingredients = response.json()['data']
        random_ids = [ingredient['_id'] for ingredient in random.sample(ingredients, 3)]
        list_ingredients = {"ingredients": random_ids}
        return list_ingredients
