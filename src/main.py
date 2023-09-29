
from src.API_Vacancy import HHManager, SJManager
from src.class_vacancy import Vacancy
from src.JsonSever import JsonManager

def user_interaction():

    count = int(input("Введите количество вакансий для вывода: "))
    filter_words = input("Введите ключевые слово для фильтрации вакансий: ")
    hh_vacancies = HHManager(filter_words, count)
    superjob_vacancies = SJManager(filter_words, count)

    print('Выберите платформу для поика вакансий HH-1 , SJ-2, HH+Sj-3, выход-0')


    while True:
        user_input = input('')
        if user_input == '1':
            vacancies = hh_vacancies.get_vacancies()
            break
        elif user_input == '2':
            vacancies = superjob_vacancies.get_vacancies()
            break
        elif user_input == '3':
            vacancies = hh_vacancies.get_vacancies() + superjob_vacancies.get_vacancies()
            break
        elif user_input == '0':
            break
        else:
            print('неверный ввод')

    if not vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return
    filter_vacancies = []
    for item in vacancies:
        vacancy = Vacancy(item['name'],
                          item['salary_from'],
                          item['salary_to'],
                          item['experience'],
                          item['description'],
                          item['alt_url'])
        filter_vacancies.append(vacancy)
    filter_vacancies.sort(reverse=True)
    for i, vacancy in enumerate(filter_vacancies):
        print(f'Вакансия номер {i+1}')
        print(vacancy)

    saver = JsonManager('DATA.json')
    list_vacansies_for_saver = []
    for item in filter_vacancies:
        item_vac = item.get_list()
        list_vacansies_for_saver.append(item_vac)

    saver.json_saver(list_vacansies_for_saver)
    print(f'Hайдено {len(vacancies)} вакансий отсортированных по зарплате и сохранённых в файле DATA.json')



if __name__ == "__main__":
    user_interaction()
