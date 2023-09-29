import json
import os.path
import requests
from src import API_Vacancy, Abstract_classes


class Vacancy:
    """Класс для сохранения информации о вакансии"""

    # all = []

    def __init__(self, name: str, salary_from: int, salary_to: int, experience: str, description: str, alt_url: str):
        try:
            self.name = name  # Название
            self.salary_from = salary_from  # Зарплата от
            self.salary_to = salary_to  # Зарплата до
            self.experience = experience  # Опыт работы
            self.description = description  # Описание вакансии
            self.alt_url = alt_url  # Ссылка на вакансию
            self.salary = self.salary()
        except KeyError as err:
            raise KeyError(err)

    def salary(self):
        if self.salary_to:
            if self.salary_from:
                return int((self.salary_from + self.salary_to) / 2)
            else:
                return self.salary_to
        else:
            if self.salary_from:
                return self.salary_from
            else:
                return 0

    def __str__(self):
        return f'''Вакансия: {self.name}.
Зарплата: {self.salary_from if self.salary_from else 0} -> {self.salary_to if self.salary_to else ""}.
Требуемый опыт: {self.experience}.
Ссылка на вакансию: {self.alt_url}
'''

    def get_list(self):
        return [
            {
                "name": self.name,
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "experience": self.experience,
                "description": self.description,
                "alt_url": self.alt_url
            },
        ]

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __le__(self, other):
        return self.salary <= other.salary
