from API_Vacancy import *
from Abstract_classes import SaverVacancies
from class_vacancy import Vacancy
import json


class JsonManager:

    def __init__(self, path):
        self.path = path

    def json_saver(self, list_vacancy):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(list_vacancy, file, indent=4, ensure_ascii=False)

    def json_open(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            json.load(file)

    def select_vacancy(self):
        pass

    def add_vacancy(self):
        pass

    def del_vacancy(self):
        pass
