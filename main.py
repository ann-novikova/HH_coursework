from src.file_worker import JsonWorker
from src.parser import HeadHunterAPI
from src.processing import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    sort_vacancies,
    user_interaction,
)
from src.vacancy import Vacancy

if __name__ == "__main__":
    search_query, top_n, filter_words, salary_range = user_interaction()
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.load_vacancies(search_query)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    list_of_dict = []
    for vacancy in vacancies_list:
        list_of_dict.append(vacancy.to_dict())

    filtered_vacancies = filter_vacancies(list_of_dict, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    for item in top_vacancies:
        print(item)

    vacancy1 = Vacancy(
        "122115665",
        "Начинающий макроэкономист",
        "Центральный банк Российской Федерации (Банк России)",
        "https://api.hh.ru/vacancies/122115665?host=hh.ru",
        None,
        None,
        (
            """Построение структурных моделей российской экономики для прогнозирования
            широкого круга макроэкономических показателей. Расчеты с использованием эконометрических,
            структурных и других моделей, а..."""
        ),
        "Требования: опыт работы от 3 лет...",
    )

    json_worker = JsonWorker()
    json_worker.write_data(list_of_dict)
    json_worker.add_vacancy(vacancy1)
    json_worker.delete_vacancy(vacancy1)
