import pytest
from helpers import *
from data import Endpoint, ResponseMessage
import allure
import requests


class TestCreateCourier:
    @allure.step('Создать курьера')
    def test_create_courier(self):
        login, password, first_name = generate_data()
        payload = {
            'login': login,
            'password': password,
            'firstname': first_name
        }
        response = requests.post(Endpoint.CREATE_COURIER, data=payload)
        assert response.status_code == 201
        assert ResponseMessage.CREATE_COURIER == response.text


    @allure.step('Создать двух одинаковых курьеров')
    def test_create_existing_courier(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(Endpoint.CREATE_COURIER, data={
            'login': data[0],
            'password': data[1],
            'firstname': data[2]
        })
        assert response.status_code == 409
        assert ResponseMessage.CREATE_USER_EXISTING == response.text


    @allure.step('Создать курьера без логина/пароля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_one_field(self, field):
        payload = generate_data_payload()
        del payload[field]
        response = requests.post(Endpoint.CREATE_COURIER, data=payload)
        assert response.status_code == 400
        assert ResponseMessage.CREATE_COURIER_WITHOUT_LOGIN == response.text
