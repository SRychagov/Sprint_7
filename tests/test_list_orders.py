import allure
import requests
from data import Endpoint, ResponseMessage


class TestListOrder:
    @allure.step('Получить список заказов')
    def test_list_order(self):
        response = requests.get(Endpoint.ORDER_LIST)
        assert response.status_code == 200
        assert ResponseMessage.LIST_ORDERS in response.text
