from src.processing import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, sort_vacancies


def test_filter_vacancies(list_of_vacancies_to_dict: list[dict]) -> None:
    assert filter_vacancies(list_of_vacancies_to_dict, ["тестировщик"]) == [
        {
            "vacancy_id": "121380408",
            "name": "Тестировщик ПО",
            "company": "NEXT Contact",
            "url": "https://api.hh.ru/vacancies/121380408?host=hh.ru",
            "salary_from": 50000,
            "salary_to": 70000,
            "description": "Функциональное, регрессионное, интеграционное, smoke-тестирование, приемочное (UAT).",
            "requirements": "Желателен опыт работы с Kubernetes и Docker. Будет плюсом: знание основ автоматизации",
        }
    ]
    assert filter_vacancies(list_of_vacancies_to_dict, ["hello"]) == []


def test_get_vacancies_by_salary(list_of_vacancies_with_None: list[dict]) -> None:
    assert get_vacancies_by_salary(list_of_vacancies_with_None, ["45000", "100000"]) == [
        {
            "vacancy_id": "121380408",
            "name": "Тестировщик ПО",
            "company": "NEXT Contact",
            "url": "https://api.hh.ru/vacancies/121380408?host=hh.ru",
            "salary_from": 50000,
            "salary_to": 70000,
            "description": "Функциональное, регрессионное, интеграционное, smoke-тестирование, приемочное (UAT).",
            "requirements": "Желателен опыт работы с Kubernetes и Docker. Будет плюсом: знание основ автоматизации",
        }
    ]


def test_sort_vacancies(list_of_vacancies_to_dict: list[dict], sorted_list_of_vacancies: list[dict]) -> None:
    assert sort_vacancies(list_of_vacancies_to_dict) == sorted_list_of_vacancies


def test_get_top_vacancies(sorted_list_of_vacancies: list[dict]) -> None:
    assert get_top_vacancies(sorted_list_of_vacancies, 1) == [
        {
            "vacancy_id": "121380408",
            "name": "Тестировщик ПО",
            "company": "NEXT Contact",
            "url": "https://api.hh.ru/vacancies/121380408?host=hh.ru",
            "salary_from": 50000,
            "salary_to": 70000,
            "description": "Функциональное, регрессионное, интеграционное, smoke-тестирование, приемочное (UAT).",
            "requirements": "Желателен опыт работы с Kubernetes и Docker. Будет плюсом: знание основ автоматизации",
        }
    ]
