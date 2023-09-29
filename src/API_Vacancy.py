import requests
from Abstract_classes import SearchVacancies
from class_vacancy import Vacancy
import os

class HHManager(SearchVacancies):
    '''Класс для получения данных по слову API HH  и преобразование их в нужный формат данных'''

    def __init__(self, keyword: str, count=100, page=0):
        self.url = 'https://api.hh.ru/vacancies'  # ссылка с вакансиями
        self.keyword = keyword  # ключевое слово для поиска
        self.count = count
        self.page = page  # колличество страниц

    def get_vacancies(self):

        dict_vacancies = []
        parms = {
            'text': self.keyword,  # ключевое слово для поиска
            'per_page': self.count,
            'area': 113,  # страна для поска(Россия)
        }
        response = requests.get(self.url, parms).json()

        for data in response['items']:
            name = data.get('name')  # Имя вакансии
            salary = data.get('salary')  # Зарплата
            if salary is None:
                salary_from = 0
                salary_to = 0
            else:
                salary_from = salary.get('from')
                if salary_from is None:
                    salary_from = 0
                salary_to = salary.get('to')
                if salary_to is None:
                    salary_to = 0

            experience = data.get('experience')['name']  # Требования работодателя
            description = data.get('snippet')['requirement']  # Описание вакансии
            alt_url = data.get('alternate_url')  # Альтернативнная ссылка на вакансию

            sample_vacancy = {'name': name,
                              'salary_from': salary_from,
                              'salary_to': salary_to,
                              'experience': experience,
                              'description': description,
                              'alt_url': alt_url,
                              }

            dict_vacancies.append(sample_vacancy)

        return dict_vacancies


class SJManager(SearchVacancies):
    def __init__(self, keyword: str, count=100, page=0):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.keyword = keyword
        self.count = count
        self.page = page

    def get_vacancies(self):
        API_KEY = os.environ.get('API_KEY_SJ')
        dict_vacancies = []
        headers = {'X-Api-App-Id': API_KEY}
        params = {'keywords': self.keyword, 'count': self.count, 'page': self.page}
        response = requests.get(self.url, headers=headers, params=params).json()

        for data in response['objects']:
            name = data.get('profession')
            salary_from = data.get('payment_from')  # Зарплата от
            salary_to = data.get('payment_to')
            experience = data.get('experience')['title']  # Требования работодателя
            description = data.get('candidat')  # Описание вакансии
            alt_url = data.get('link')  # Cсылка на вакансию

            sample_vacancy = {'name': name,
                              'salary_from': salary_from,
                              'salary_to': salary_to,
                              'experience': experience,
                              'description': description,
                              'alt_url': alt_url,
                              }

            dict_vacancies.append(sample_vacancy)

        return dict_vacancies







