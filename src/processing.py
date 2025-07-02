def user_interaction() -> tuple[str, int, list[str], list[str]]:
    """Функция для получения данных от пользователя"""

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()
    salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ").split(" - ")

    return search_query, top_n, filter_words, salary_range


def filter_vacancies(vacancies_list: list[dict], filter_words: list) -> list[dict]:
    """Функция фильтрации по ключевым словам"""
    return [
        vacancy
        for vacancy in vacancies_list
        if any(any(word in str(value).lower() for word in filter_words) for value in vacancy.values())
    ]


def get_vacancies_by_salary(filtered_vacancies: list[dict], salary_range: list[str]) -> list[dict]:
    """Функция ранжирования по заданным параметрам заработной платы"""
    min_salary = int(salary_range[0])
    max_salary = int(salary_range[1])

    result = []
    for vacancy in filtered_vacancies:
        salary_from = vacancy.get("salary_from")
        salary_to = vacancy.get("salary_to")
        try:
            if salary_from is not None:
                salary_from = int(salary_from)
            else:
                salary_from = 0
            if salary_to is not None:
                salary_to = int(salary_to)
            else:
                salary_to = 0
        except (ValueError, TypeError):
            continue
        if salary_from >= min_salary and salary_to <= max_salary:
            result.append(vacancy)

    return result


def sort_vacancies(ranged_vacancies: list[dict]) -> list[dict]:
    """Функция сортировки"""
    return sorted(ranged_vacancies, key=lambda vacancy: vacancy.get("salary_from", 0), reverse=True)


def get_top_vacancies(sorted_vacancies: list[dict], top_n: int) -> list[dict]:
    return sorted_vacancies[:top_n]
