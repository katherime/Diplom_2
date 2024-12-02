import allure
from methods.order_methods.get_user_orders import GetUserOrders
from methods.user_methods.login_user import LoginUser
from data import ResponseTexts


class TestGetUserOrders:

    @allure.title('Проверка получения заказов авторизированного пользователя')
    def test_create_order_with_authorization_with_ingredients(self, create_new_user_and_return_data):
        get_user_methods = GetUserOrders()
        login_user_methods = LoginUser()
        login_response = login_user_methods.login_user(create_new_user_and_return_data)
        header = {"Authorization": login_response.json()["accessToken"]}
        response = get_user_methods.get_user_orders(header)
        assert response.status_code == 200 and ResponseTexts.response_success in response.text

    @allure.title('Проверка получения заказов неавторизированного пользователя')
    def test_create_order_no_authorization_with_ingredients(self, create_new_user_and_return_data):
        get_user_methods = GetUserOrders()
        header = {"Authorization": ''}
        response = get_user_methods.get_user_orders(header)
        assert response.status_code == 401 and response.json() == ResponseTexts.response_no_authorization
