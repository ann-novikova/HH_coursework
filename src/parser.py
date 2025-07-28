from abc import ABC, abstractmethod
from pprint import pprint

import requests


class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями."""

    @abstractmethod
    def _connect_to_api(self) -> bool:
        """
        Абстрактный метод для подключения к API.
        """
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list[dict]:
        """
        Абстрактный метод для получения вакансий.
        :param keyword: Ключевое слово для поиска вакансий.
        """
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Наследуется от абстрактного класса Parser.
    """

    __vacancies: list[dict]

    def __init__(self) -> None:
        """
        Инициализация класса.
        Устанавливает приватные атрибуты для URL, заголовков, параметров и списка вакансий.
        """
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: dict = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def _connect_to_api(self) -> bool:
        """
        Приватный метод для подключения к API hh.ru.
        Отправляет запрос на базовый URL и проверяет статус-код ответа.
        """
        try:
            response = requests.get(self.__url, headers=self.__headers)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to API: {e}")
            return False

    def load_vacancies(self, keyword: str) -> list[dict]:
        """Метод для получения вакансий."""

        if not self._connect_to_api():
            return []
        self.__params["text"] = keyword
        self.__params["page"] = 0  # Ensure page starts at 0
        self.__vacancies = []  # Clear previous vacancies
        try:
            while self.__params.get("page") != 20:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                response.raise_for_status()
                data = response.json()
                if "items" in data:
                    self.__vacancies.extend(data["items"])
                else:
                    print("Warning: No 'items' key found")
                    break
                self.__params["page"] += 1
            return self.__vacancies

        except requests.exceptions.RequestException as e:
            print(f"Error loading vacancies: {e}")
            return []


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.load_vacancies("Python")
    pprint(hh_vacancies)
