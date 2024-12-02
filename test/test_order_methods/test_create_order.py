from methods.user_methods.login_user import LoginUser
import allure
from methods.order_methods.create_order import CreateOrder
from data import ResponseTexts, WrongTestData


class TestCreateOrder:

    @allure.title('Проверка cоздания заказа с авторизацией с ингредиентами')
    def test_create_order_with_authorization_with_ingredients(self, create_new_user_and_return_data):
        login_user_methods = LoginUser()
        create_order = CreateOrder()
        login_user_methods.login_user(create_new_user_and_return_data)
        list_ingredients = create_order.get_hash_of_three_random_ingredients()
        response = create_order.create_order(list_ingredients)
        assert response.status_code == 200 and ResponseTexts.response_success in response.text

    @allure.title('Проверка cоздания заказа с авторизацией без ингредиентов')
    def test_create_order_with_authorization_no_ingredients(self, create_new_user_and_return_data):
        login_user_methods = LoginUser()
        create_order = CreateOrder()
        login_user_methods.login_user(create_new_user_and_return_data)
        list_ingredients = ""
        response = create_order.create_order(list_ingredients)
        assert response.status_code == 400 and ResponseTexts.response_no_ingredient in response.text

    @allure.title('Проверка cоздания заказа с авторизацией с неверным хешем ингредиентов')
    def test_create_order_with_authorization_wrong_hash_ingredients(self, create_new_user_and_return_data):
        login_user_methods = LoginUser()
        create_order = CreateOrder()
        login_user_methods.login_user(create_new_user_and_return_data)
        list_ingredients = WrongTestData.wrong_hash_ingredients
        response = create_order.create_order(list_ingredients)
        assert response.status_code == 500 and ResponseTexts.response_internal_server_error in response.text

    @allure.title('Проверка cоздания заказа без авторизации с ингредиентами')
    def test_create_order_no_authorization_with_ingredients(self):
        create_order = CreateOrder()
        list_ingredients = create_order.get_hash_of_three_random_ingredients()
        response = create_order.create_order(list_ingredients)
        assert response.status_code == 200

    @allure.title('Проверка cоздания заказа без авторизации без ингредиентов')
    def test_create_order_no_authorization_no_ingredients(self):
        create_order = CreateOrder()
        list_ingredients = ""
        response = create_order.create_order(list_ingredients)
        assert response.status_code == 400 and ResponseTexts.response_no_ingredient in response.text

    @allure.title('Проверка cоздания заказа без авторизации без ингредиентов')
    def test_create_order_no_authorization_wrong_hash_ingredients(self):
        create_order = CreateOrder()
        list_ingredients = WrongTestData.wrong_hash_ingredients
        response = create_order.create_order(list_ingredients)
        assert response.status_code == 500 and ResponseTexts.response_internal_server_error in response.text
