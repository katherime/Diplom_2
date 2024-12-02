import pytest
from methods.user_methods.create_new_user import CreateUser
from helpers import generate_new_user_data


@pytest.fixture
def create_new_user_and_return_data():
    create_user_methods = CreateUser()
    payload = generate_new_user_data()
    response = create_user_methods.create_new_user(payload)
    response_data = response.json()
    data = {
        "email": response_data["user"]["email"],
        "password": payload["password"],
    }
    yield data
    create_user_methods.delete_user(data)
