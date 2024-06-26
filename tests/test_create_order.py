import allure
import requests
import pytest
from data import Endpoint, ResponseMessage, User


class TestCreateOrder:
    @allure.step('Создать заказ с разными цветами самоката')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order(self, color):
        payload = User.user
        payload['color'] = color
        response = requests.post(Endpoint.CREATE_ORDER, json=payload)
        assert response.status_code == 201
        assert ResponseMessage.CREATE_ORDER in response.text
