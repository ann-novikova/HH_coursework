import pprint
import re


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("vacancy_id", "name", "company", "url", "salary_from", "salary_to", "requirements", "description")

    def __init__(
        self,
        vacancy_id: str,
        name: str,
        company: str,
        url: str,
        salary_from: int | float | None,
        salary_to: int | float | None,
        description: str,
        requirements: str,
    ) -> None:
        """Конкструктор для создания экзепмляра класса Vacancy"""

        self.vacancy_id = self.__validate_id(vacancy_id)
        self.name = self.__validate_name(name)
        self.company = self.__validate_company(company)
        self.url = self.__validate_url(url)
        self.salary_to = self.__validate_salary_to(salary_to)
        self.salary_from = self.__validate_salary_from(salary_from)
        self.description = self.__validate_description(description)
        self.requirements = self.__validate_requirements(requirements)

    def __repr__(self) -> str:
        """Переопределение магического метода"""
        return pprint.pformat(self.to_dict())

    def __lt__(self, other: "Vacancy") -> bool:
        """Метод сравнения по заработной плате"""
        if not isinstance(other, Vacancy):
            raise TypeError("Поддерживается сравнение только между экземплярами класса")
        return self.salary_to < other.salary_to

    @staticmethod
    def __validate_id(vacancy_id: str) -> str:
        """Валидация аттрибута "ID" в вакансии"""
        if not isinstance(vacancy_id, str) or not vacancy_id:
            return "ID вакансии не указано"
        return vacancy_id

    @staticmethod
    def __validate_name(name: str) -> str:
        """Валидация названия вакансии"""
        if not isinstance(name, str) or not name:
            return "Название вакансии не указано"
        return name

    @staticmethod
    def __validate_company(company: str) -> str:
        """Валидация названия компании"""
        if not isinstance(company, str) or not company:
            return "Название вакансии не указано"
        return company

    @staticmethod
    def __validate_url(url: str) -> str:
        """Валидация url"""
        if isinstance(url, str) and re.match("https://", url, flags=0):
            return url
        return "URL не указан"

    @staticmethod
    def __validate_salary_to(salary_to: int | float | None) -> int | float:
        """Валидация заработной платы ДО"""
        if not isinstance(salary_to, (int, float)) or salary_to < 0:
            return 0
        return salary_to

    @staticmethod
    def __validate_salary_from(salary_from: int | float | None) -> int | float:
        """Валидация заработной платы ОТ"""
        if not isinstance(salary_from, (int, float)) or salary_from < 0:
            return 0
        return salary_from

    @staticmethod
    def __validate_description(description: str) -> str:
        """Валидация описания вакансии"""
        if not isinstance(description, str) or not description:
            return "Описание вакансии не указано"
        return description

    @staticmethod
    def __validate_requirements(requirements: str) -> str:
        """Валидация требований вакансии"""
        if not isinstance(requirements, str) or not requirements:
            return "Требования вакансии не указаны"
        return requirements

    def to_dict(self) -> dict:
        """Изменение формата вывода вакансии в словарь"""
        return {
            "vacancy_id": self.vacancy_id,
            "name": self.name,
            "company": self.company,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description,
            "requirements": self.requirements,
        }

    @classmethod
    def cast_to_object_list(cls, list_vacancies: list[dict]) -> list["Vacancy"]:
        """Метод для создания экземпляра класса из данных"""
        vacancy_obj_list = []
        for vacancy in list_vacancies:
            vacancy_id = vacancy.get("id")
            name = vacancy.get("name")
            company = vacancy.get("employer")
            company_name = company.get("name") if company else ""

            url = vacancy.get("url") or ""

            salary = vacancy.get("salary")
            salary_from = salary.get("from") if salary else None
            salary_to = salary.get("to") if salary else None

            try:
                salary_from = float(salary_from) if salary_from is not None else 0.0
            except (ValueError, TypeError):
                salary_from = 0.0

            try:
                salary_to = float(salary_to) if salary_to is not None else 0.0
            except (ValueError, TypeError):
                salary_to = 0.0

            details = vacancy.get("snippet")
            description = details.get("responsibility") if details else ""
            requirements = details.get("requirement") if details else ""

            vacancy_id = str(vacancy_id) if vacancy_id is not None else ""
            name = str(name) if name is not None else ""
            company_name = str(company_name)
            url = str(url)
            description = str(description)
            requirements = str(requirements)

            vacancy_obj_list.append(
                cls(vacancy_id, name, company_name, url, salary_from, salary_to, description, requirements)
            )
        return vacancy_obj_list
