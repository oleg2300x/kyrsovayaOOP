import json
import os.path
import requests
from src import API_Vacancy, Abstract_classes


class Vacancy:
    """Класс для сохранения информации о вакансии"""
    # all = []

    def __init__(self, service_name: str, name: str, salary_from: int, salary_to: int, experience: str, description: str, alt_url: str):
        try:
            self.name = name  # Название
            self.salary_from = salary_from  # Зарплата от
            self.salary_to = salary_to  # Зарплата до
            self.experience = experience  # Опыт работы
            self.description = description  # Описание вакансии
            self.alt_url = alt_url  # Ссылка на вакансию
            self.service_name = service_name
        except KeyError as err:
            raise KeyError(err)

    @property
    def salary(self):
        return self.salary_to if self.salary_to else self.salary_from

    def __str__(self):
        return f'Сервис: {self.service_name}. ' \
               f'Вакансия: {self.name}.' \
               f' Зарплата: {self.salary_from if self.salary_from else 0} -> {self.salary_to if self.salary_to else ""}'\
               f' Требуемый опыт: {self.experience}.' \
               f' Ссылка на вакансию: {self.alt_url}'

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

