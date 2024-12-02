base_url_stellar_burgers = 'https://stellarburgers.nomoreparties.site'
create_user_endpoint = '/api/auth/register'
login_user_endpoint = '/api/auth/login'
logout_user_endpoint = '/api/auth/logout'
data_about_user_endpoint = '/api/auth/user'
create_order_endpoint = '/api/orders'
data_about_ingridients_endpoint = '/api/ingredients'
get_user_orders_endpoint = '/api/orders'


class ResponseTexts:
    response_user_already_exist = {'message': 'User already exists', 'success': False}
    response_empty_fields = {"success": False, "message": "Email, password and name are required fields"}
    response_success = '"success":true'
    response_wrong_data_for_login = '{"success":false,"message":"email or password are incorrect"}'
    response_no_authorization = {"success": False, "message": "You should be authorised"}
    response_no_ingredient = '{"success":false,"message":"Ingredient ids must be provided"}'
    response_internal_server_error = 'Internal Server Error'

class WrongTestData:
    wrong_hash_ingredients = {"ingredients": ['test_wrong_hash']}