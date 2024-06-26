class User:
    user = {
        'firstname': 'Сергей',
        'lastname': 'Рычагов',
        'address': 'Москва',
        'metroStation': 191,
        'phone': '+78005553535',
        'deliveryDate': '2024-06-27',
        'rentTime': 1,
        'comment': '',
        'color': []
    }


class Endpoint:
    SCOOTER_URL = 'http://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = f'{SCOOTER_URL}/api/v1/courier'
    LOGIN_COURIER = f'{SCOOTER_URL}/api/v1/courier/login'
    CREATE_ORDER = f'{SCOOTER_URL}/api/v1/orders'
    ORDER_LIST = f'{SCOOTER_URL}/api/v1/orders'


class ResponseMessage:
    LOGING_COURIER = 'id'
    LOGING_COURIER_WITHOUT_DATA = '{"code":400,"message":"Недостаточно данных для входа"}'
    LOGIN_USER_NOT_EXIST = '{"code":404,"message":"Учетная запись не найдена"}'
    CREATE_COURIER = '{"ok":true}'
    CREATE_COURIER_WITHOUT_LOGIN = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    CREATE_USER_EXISTING = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    CREATE_ORDER = 'track'
    LIST_ORDERS = 'orders'
