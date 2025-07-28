import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Generator

from src.vacancy import Vacancy

BASE_DIR = Path(__file__).resolve().parent.parent
data_path = BASE_DIR / "data"


class FileWorker(ABC):
    """Класс для работы с файлами"""

    @abstractmethod
    def open_file(self) -> None:
        """Метод для открытия файла и чтение его содержимого"""
        pass

    @abstractmethod
    def write_data(self, data: list[dict]) -> None:
        """Метод для записи данных в файл"""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для добавления Вакансии в файл"""
        pass

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для удаления Вакансии из файл"""
        pass

    def search(self, keyword: str) -> Generator | None:
        """Метод для поиска Вакансии по ключевому слову"""
        pass


class JsonWorker(FileWorker):
    """Класс для работы с JSON файлами"""

    data_file: list[dict]

    def __init__(self, filename: str = "vacancy.json") -> None:
        """Конструктор для создания экзампляра класс JsonWorker"""

        self.__filename = data_path / filename
        self.data_file = []

    def open_file(self) -> None:
        """Метод для открытия файла и чтение его содержимого"""

        if not self.__filename.is_file():
            print("Файла не существует, для начала работы создайте файл с помощью метода write_data")
        else:
            with open(self.__filename, mode="r", encoding="utf-8") as file:
                self.data_file = json.load(file)

    def write_data(self, data: list[dict], file_mode: str = "w") -> None:
        """Метод для записи данных в файл"""

        with open(self.__filename, file_mode, encoding="utf-8") as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))
        self.data_file = data

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для добавления Вакансии в файл"""

        if isinstance(vacancy, Vacancy):
            existing_id = [vacancy["vacancy_id"] for vacancy in self.data_file]
            if vacancy.vacancy_id not in existing_id:
                self.data_file.append(vacancy.to_dict())
                self.write_data(self.data_file, "w")
        else:
            raise TypeError("Возможно занесение данных только класса Вакансия")

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии"""
        if isinstance(vacancy, Vacancy):
            for index, data in enumerate(self.data_file):
                if data["vacancy_id"] == vacancy.vacancy_id:
                    del self.data_file[index]
                    break
            self.write_data(self.data_file, "w")
        else:
            raise TypeError("Возможно удаление данных только класса Вакансия")

    def search(self, keyword: str) -> Generator | None:
        """Метод для поиска Вакансии по ключевому слову"""

        return (vacancy for vacancy in self.data_file if keyword in vacancy.values())
