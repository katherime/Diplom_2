import requests
import allure
from data import base_url_stellar_burgers, get_user_orders_endpoint


class GetUserOrders:

    @allure.step('Получение заказов конкретного пользователя через GET-запрос')
    def get_user_orders(self, header):
        response = requests.get(f"{base_url_stellar_burgers}{get_user_orders_endpoint}", headers=header)
        return response
