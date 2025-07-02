import json

from _pytest.capture import CaptureFixture

from src.file_worker import JsonWorker
from src.vacancy import Vacancy


def test_open_empty_file(capsys: CaptureFixture) -> None:
    jsonworker0 = JsonWorker("test.json")
    jsonworker0.open_file()
    message = capsys.readouterr()
    assert message.out.strip() == "Файла не существует, для начала работы создайте файл с помощью метода write_data"


def test_write_data(list_of_vacancies_to_dict: list[dict], jsonworker1: JsonWorker) -> None:
    jsonworker1.write_data(list_of_vacancies_to_dict)
    assert jsonworker1.data_file == list_of_vacancies_to_dict


def test_add_vacancy(jsonworker1: JsonWorker, vacancy1: Vacancy, path_to_file: str) -> None:
    jsonworker1.add_vacancy(vacancy1)
    vacancy_dict = [
        {
            "vacancy_id": "122115665",
            "name": "Начинающий макроэкономист",
            "company": "Центральный банк Российской Федерации (Банк России)",
            "url": "https://api.hh.ru/vacancies/122115665?host=hh.ru",
            "salary_from": 50000,
            "salary_to": 70000,
            "description": "Построение структурных моделей российской экономики",
            "requirements": "Требования: опыт работы от 3 лет",
        }
    ]
    assert jsonworker1.data_file == vacancy_dict
    with open(path_to_file, encoding="utf-8") as f:
        assert json.load(f) == vacancy_dict


def test_delete_vacancy(jsonworker1: JsonWorker, vacancy1: Vacancy, path_to_file: str) -> None:
    jsonworker1.delete_vacancy(vacancy1)
    assert jsonworker1.data_file == []
    with open(path_to_file, encoding="utf-8") as f:
        assert json.load(f) == []
