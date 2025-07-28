import pprint

from src.vacancy import Vacancy


def test_vacancy_init(vacancy1: Vacancy) -> None:
    assert vacancy1.vacancy_id == "122115665"
    assert vacancy1.name == "Начинающий макроэкономист"
    assert vacancy1.company == "Центральный банк Российской Федерации (Банк России)"
    assert vacancy1.url == "https://api.hh.ru/vacancies/122115665?host=hh.ru"
    assert vacancy1.salary_from == 50000
    assert vacancy1.salary_to == 70000
    assert vacancy1.description == "Построение структурных моделей российской экономики"
    assert vacancy1.requirements == "Требования: опыт работы от 3 лет"


def test_validate_atributes() -> None:
    vacancy_empty = Vacancy("", "", "", "", None, None, "", "")
    assert vacancy_empty.vacancy_id == "ID вакансии не указано"
    assert vacancy_empty.name == "Название вакансии не указано"
    assert vacancy_empty.company == "Название вакансии не указано"
    assert vacancy_empty.url == "URL не указан"
    assert vacancy_empty.salary_from == 0
    assert vacancy_empty.salary_to == 0
    assert vacancy_empty.description == "Описание вакансии не указано"
    assert vacancy_empty.requirements == "Требования вакансии не указаны"


def test_repr(vacancy1: Vacancy) -> None:
    expected = pprint.pformat(
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
    )
    assert str(vacancy1) == expected


def test_lt(vacancy1: Vacancy, vacancy2: Vacancy) -> None:
    assert vacancy1 < vacancy2


def test_cast_to_object_list(list_of_vacancies: list[dict]) -> None:
    vacancy0 = Vacancy.cast_to_object_list(list_of_vacancies)[0]
    assert vacancy0.vacancy_id == "121489042"
    assert vacancy0.name == "Backend-разработчик"
    assert vacancy0.company == "НЛ Континент"
    assert vacancy0.url == "https://api.hh.ru/vacancies/121489042?host=hh.ru"
    assert vacancy0.salary_from == 0
    assert vacancy0.salary_to == 0
    assert vacancy0.description == (
        "Разработка и поддержка backend-части "
        "внутренних систем компании на "
        "<highlighttext>Python</highlighttext> 2.7 и "
        "<highlighttext>Python</highlighttext> 3.9. "
        "Модернизация, оптимизация и "
        "масштабирование..."
    )

    assert vacancy0.requirements == (
        "MySQL- понимать зачем нужны индексы и "
        "транзакции. Django - опыт работы от 2-х лет. "
        "Опыт работы Django Rest Framework. "
    )
