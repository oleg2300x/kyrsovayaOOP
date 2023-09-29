from abc import abstractmethod, ABC


class SearchVacancies(ABC):
    '''Класс поиска вакансий по API'''

    @abstractmethod
    def get_vacancies(self):
        pass

class SaverVacancies(ABC):
    '''Класс для добавления, выбора и удаления вакансии'''

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def select_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

