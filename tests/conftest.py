import pytest

from src.file_worker import JsonWorker, data_path
from src.parser import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture()
def vacancy1() -> Vacancy:
    return Vacancy(
        "122115665",
        "Начинающий макроэкономист",
        "Центральный банк Российской Федерации (Банк России)",
        "https://api.hh.ru/vacancies/122115665?host=hh.ru",
        50000,
        70000,
        "Построение структурных моделей российской экономики",
        "Требования: опыт работы от 3 лет",
    )


@pytest.fixture()
def vacancy2() -> Vacancy:
    return Vacancy(
        "122115666",
        "Python developer",
        "Some company",
        "https://api.hh.ru/vacancies/122115666?host=hh.ru",
        75000,
        100000,
        "Write code",
        "Python knowledge",
    )


@pytest.fixture()
def jsonworker1() -> JsonWorker:
    return JsonWorker("vacancy_test.json")


@pytest.fixture
def init_hh() -> HeadHunterAPI:
    return HeadHunterAPI()


@pytest.fixture()
def path_to_file() -> str:
    return str(data_path / "vacancy_test.json")


@pytest.fixture()
def list_of_vacancies_to_dict() -> list[dict]:
    return [
        {
            "vacancy_id": "122237214",
            "name": "Frontend-разработчик",
            "company": "Облачные Квантовые Технологии",
            "url": "https://api.hh.ru/vacancies/122237214?host=hh.ru",
            "salary_from": 0,
            "salary_to": 0,
            "description": "Разработка пользовательского интерфейса облачной операционной системы.",
            "requirements": "Опыт использования в работе TDD, CI/CD. Опыт работы в Linux, CLI.",
        },
        {
            "vacancy_id": "121380408",
            "name": "Тестировщик ПО",
            "company": "NEXT Contact",
            "url": "https://api.hh.ru/vacancies/121380408?host=hh.ru",
            "salary_from": 50000,
            "salary_to": 70000,
            "description": "Функциональное, регрессионное, интеграционное, smoke-тестирование, приемочное (UAT).",
            "requirements": "Желателен опыт работы с Kubernetes и Docker. Будет плюсом: знание основ автоматизации",
        },
    ]


@pytest.fixture()
def sorted_list_of_vacancies() -> list[dict]:
    return [
        {
            "vacancy_id": "121380408",
            "name": "Тестировщик ПО",
            "company": "NEXT Contact",
            "url": "https://api.hh.ru/vacancies/121380408?host=hh.ru",
            "salary_from": 50000,
            "salary_to": 70000,
            "description": "Функциональное, регрессионное, интеграционное, smoke-тестирование, приемочное (UAT).",
            "requirements": "Желателен опыт работы с Kubernetes и Docker. Будет плюсом: знание основ автоматизации",
        },
        {
            "vacancy_id": "122237214",
            "name": "Frontend-разработчик",
            "company": "Облачные Квантовые Технологии",
            "url": "https://api.hh.ru/vacancies/122237214?host=hh.ru",
            "salary_from": 0,
            "salary_to": 0,
            "description": "Разработка пользовательского интерфейса облачной операционной системы.",
            "requirements": "Опыт использования в работе TDD, CI/CD. Опыт работы в Linux, CLI.",
        },
    ]


@pytest.fixture()
def list_of_vacancies_with_None() -> list[dict]:
    return [
        {
            "vacancy_id": "121380408",
            "name": "Тестировщик ПО",
            "company": "NEXT Contact",
            "url": "https://api.hh.ru/vacancies/121380408?host=hh.ru",
            "salary_from": 50000,
            "salary_to": 70000,
            "description": "Функциональное, регрессионное, интеграционное, smoke-тестирование, приемочное (UAT).",
            "requirements": "Желателен опыт работы с Kubernetes и Docker. Будет плюсом: знание основ автоматизации",
        },
        {
            "vacancy_id": "122237214",
            "name": "Frontend-разработчик",
            "company": "Облачные Квантовые Технологии",
            "url": "https://api.hh.ru/vacancies/122237214?host=hh.ru",
            "salary_from": None,
            "salary_to": None,
            "description": "Разработка пользовательского интерфейса облачной операционной системы.",
            "requirements": "Опыт использования в работе TDD, CI/CD. Опыт работы в Linux, CLI.",
        },
    ]


@pytest.fixture()
def list_of_vacancies() -> list[dict]:
    return [
        {
            "accept_incomplete_resumes": False,
            "accept_temporary": False,
            "address": {
                "building": "53/1",
                "city": "Новосибирск",
                "description": None,
                "id": "2792399",
                "lat": 55.039863,
                "lng": 82.9358,
                "metro": {
                    "lat": 55.043634,
                    "line_id": "53",
                    "line_name": "Дзержинская",
                    "lng": 82.935566,
                    "station_id": "53.304",
                    "station_name": "Маршала Покрышкина",
                },
                "metro_stations": [
                    {
                        "lat": 55.043634,
                        "line_id": "53",
                        "line_name": "Дзержинская",
                        "lng": 82.935566,
                        "station_id": "53.304",
                        "station_name": "Маршала Покрышкина",
                    }
                ],
                "raw": "Новосибирск, улица Ломоносова, 53/1",
                "street": "улица Ломоносова",
            },
            "adv_context": None,
            "adv_response_url": None,
            "alternate_url": "https://hh.ru/vacancy/121489042",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=121489042",
            "archived": False,
            "area": {"id": "4", "name": "Новосибирск", "url": "https://api.hh.ru/areas/4"},
            "branding": {"tariff": None, "type": "MAKEUP"},
            "contacts": None,
            "created_at": "2025-06-09T18:15:13+0300",
            "department": None,
            "employer": {
                "accredited_it_employer": False,
                "alternate_url": "https://hh.ru/employer/706928",
                "employer_rating": None,
                "id": "706928",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/7178152.png",
                    "90": "https://img.hhcdn.ru/employer-logo/7178151.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1389591.png",
                },
                "name": "НЛ Континент",
                "trusted": True,
                "url": "https://api.hh.ru/employers/706928",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=706928",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "fly_in_fly_out_duration": [],
            "has_test": False,
            "id": "121489042",
            "insider_interview": None,
            "internship": False,
            "is_adv_vacancy": False,
            "name": "Backend-разработчик",
            "night_shifts": False,
            "premium": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "published_at": "2025-06-09T18:15:13+0300",
            "relations": [],
            "response_letter_required": False,
            "response_url": None,
            "salary": None,
            "salary_range": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_contacts": True,
            "show_logo_in_search": True,
            "snippet": {
                "requirement": "MySQL- понимать зачем нужны индексы и "
                "транзакции. Django - опыт работы от 2-х лет. "
                "Опыт работы Django Rest Framework. ",
                "responsibility": "Разработка и поддержка backend-части "
                "внутренних систем компании на "
                "<highlighttext>Python</highlighttext> 2.7 и "
                "<highlighttext>Python</highlighttext> 3.9. "
                "Модернизация, оптимизация и "
                "масштабирование...",
            },
            "sort_point_distance": None,
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/121489042?host=hh.ru",
            "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "working_days": [],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
        {
            "accept_incomplete_resumes": False,
            "accept_temporary": False,
            "address": {
                "building": "42",
                "city": "Москва",
                "description": None,
                "id": "7101916",
                "lat": 55.783681,
                "lng": 37.630517,
                "metro": {
                    "lat": 55.779584,
                    "line_id": "5",
                    "line_name": "Кольцевая",
                    "lng": 37.633646,
                    "station_id": "5.119",
                    "station_name": "Проспект Мира",
                },
                "metro_stations": [
                    {
                        "lat": 55.779584,
                        "line_id": "5",
                        "line_name": "Кольцевая",
                        "lng": 37.633646,
                        "station_id": "5.119",
                        "station_name": "Проспект Мира",
                    }
                ],
                "raw": "Москва, улица Щепкина, 42",
                "street": "улица Щепкина",
            },
            "adv_context": None,
            "adv_response_url": None,
            "alternate_url": "https://hh.ru/vacancy/122160167",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=122160167",
            "archived": False,
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "contacts": None,
            "created_at": "2025-07-02T10:06:13+0300",
            "department": None,
            "employer": {
                "accredited_it_employer": True,
                "alternate_url": "https://hh.ru/employer/4808331",
                "employer_rating": None,
                "id": "4808331",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/4204937.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/4204936.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/941099.jpg",
                },
                "name": "РК-ЦИФРА",
                "trusted": True,
                "url": "https://api.hh.ru/employers/4808331",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=4808331",
            },
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "fly_in_fly_out_duration": [],
            "has_test": False,
            "id": "122160167",
            "insider_interview": None,
            "internship": False,
            "is_adv_vacancy": False,
            "name": "Старший системный инженер",
            "night_shifts": False,
            "premium": False,
            "professional_roles": [{"id": "114", "name": "Системный инженер"}],
            "published_at": "2025-07-02T10:06:13+0300",
            "relations": [],
            "response_letter_required": False,
            "response_url": None,
            "salary": None,
            "salary_range": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "show_contacts": False,
            "show_logo_in_search": None,
            "snippet": {
                "requirement": "Базовые знания принципа работы сетей: "
                "коммутация, маршрутизация, NAT. Уверенное "
                "владение <highlighttext>Python</highlighttext>, "
                "PowerShell. Опыт администрирования Zabbix: "
                "умение добавлять собственные метрики, "
                "конфигурация...",
                "responsibility": "Разработка скриптов мониторинга с помощью "
                "<highlighttext>Python</highlighttext>, "
                "PowerShell. Разработка автотестов с помощью "
                "Selenium. Автоматизировать рутинные задачи с "
                "помощью "
                "<highlighttext>Python</highlighttext>, "
                "PowerShell. ",
            },
            "sort_point_distance": None,
            "type": {"id": "open", "name": "Открытая"},
            "url": "https://api.hh.ru/vacancies/122160167?host=hh.ru",
            "work_format": [],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "working_days": [],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "working_time_intervals": [],
            "working_time_modes": [],
        },
    ]
