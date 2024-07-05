"""
Задание
Напишите класс LegalAPI для взаимодействия с API, размещённым по адресу
https://legal-api.sirotinsky.com/.
Класс должен содержать в себе функционал для работы со всеми методами,
указанными в документации к API, которые размещены по адресу
https://legal-api.sirotinsky.com/docs
Метод инициализации экземпляра класса должен принимать в качестве аргумента
токен для авторизации.
Методы для получения данных из ЕФРСБ должны быть публичными и содержать
doc string
Данные для доступа:
 Token: 4123saedfasedfsadf4324234f223ddf23
"""

import requests


class LegalAPI:
    def __init__(self, token):
        """
        Инициализация экземпляра класса LegalAPI.

        :param token: Токен для авторизации.
        """
        self.base_url = "https://legal-api.sirotinsky.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def get_efrsb_debtors(self):
        """
        Получить список должников из ЕФРСБ.

        :return: Список должников.
        """
        endpoint = "/efrsb/debtors"
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
        response.raise_for_status()  # выбрасывает исключение для кодов ошибок HTTP
        return response.json()

    def get_efrsb_messages(self):
        """
        Получить сообщения из ЕФРСБ.

        :return: Список сообщений.
        """
        endpoint = "/efrsb/messages"
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_efrsb_cases(self):
        """
        Получить дела из ЕФРСБ.

        :return: Список дел.
        """
        endpoint = "/efrsb/cases"
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_efrsb_arbitr_managers(self):
        """
        Получить арбитражных управляющих из ЕФРСБ.

        :return: Список арбитражных управляющих.
        """
        endpoint = "/efrsb/arbitr-managers"
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_efrsb_trade_places(self):
        """
        Получить торговые площадки из ЕФРСБ.

        :return: Список торговых площадок.
        """
        endpoint = "/efrsb/trade-places"
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
        response.raise_for_status()
        return response.json()


# Пример использования
if __name__ == "__main__":
    token = "4123saedfasedfsadf4324234f223ddf23"
    api = LegalAPI(token)

    # Получение данных
    try:
        debtors = api.get_efrsb_debtors()
        print("Должники:", debtors)

        messages = api.get_efrsb_messages()
        print("Сообщения:", messages)

        cases = api.get_efrsb_cases()
        print("Дела:", cases)

        arbitr_managers = api.get_efrsb_arbitr_managers()
        print("Арбитражные управляющие:", arbitr_managers)

        trade_places = api.get_efrsb_trade_places()
        print("Торговые площадки:", trade_places)
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")