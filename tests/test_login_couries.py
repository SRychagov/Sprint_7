from data import Endpoint, ResponseMessage
from conftest import create_courier
from helpers import *
import allure
import requests


class TestAuthCourier:
    @allure.step('Авторизация курьера')
    def test_auth_courier(self, create_courier):
        login_pass = create_courier
        response = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': login_pass[0],
            'password': login_pass[1]
        })
        assert response.status_code == 200
        assert ResponseMessage.LOGING_COURIER in response.text


    @allure.step('Авторизация курьера без логина')
    def test_auth_without_login(self, create_courier):
        login_pass = create_courier
        response = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': '',
            'password': login_pass[1]
        })
        assert response.status_code == 400
        assert ResponseMessage.LOGING_COURIER_WITHOUT_DATA == response.text


    @allure.step('Авторизация курьера без пароля')
    def test_auth_without_password(self, create_courier):
        login_pass = create_courier
        response = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': login_pass[0],
            'password': ''
        })
        assert response.status_code == 400
        assert ResponseMessage.LOGING_COURIER_WITHOUT_DATA == response.text


    @allure.step('Авторизация несуществующего курьера')
    def test_auth_not_existing_courier(self):
        response = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': 'ksenia',
            'password': 'qwerty1234'
        })
        assert response.status_code == 404
        assert ResponseMessage.LOGIN_USER_NOT_EXIST == response.text
