## тема "Тестирование API". Проект учебного сервиса Яндекс Самокат.

### Тестовые данные в файле data.py
- class User - Данные пользователя
- class Endpoint - url + конечная точка запроса
- class ResponseMessage - Ответы на запрос

### Создание курьера - test_create_courier.py
- test_create_courier - Проверка создания курьера
- test_create_existing_courier - Проверка создания двух одинаковых курьеров
- test_create_courier_without_one_field - Проверка создания курьера без логина/пароля

### Логин курьера - test_login_couries.py
- test_auth_courier - Проверка авторизации курьера
- test_auth_without_login - Проверка авторизации курьера без логина
- test_auth_without_password - Проверка авторизации курьера без пароля
- test_auth_not_existing_courier - Проверка авторизации несуществующего курьера
### Создание заказа - test_create_order.py
- test_create_order - Проверка создание заказа с (одним цветом, разными цветами, двумя цветами, без цвета) 
### Список заказов - test_list_orders.py
- test_list_order - Проверка получения списка заказов


#### Перед работой с репозиторием требуется установить зависимости 
``` shell
pip3 install -r requirements.txt
```
Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
Посмотреть отчет в веб версии пройденного прогона
``` shell
allure serve allure_results
```