import json


class Employee:
    "Описание работника"
    def __init__(self, firstname, lastname, age, email, skills, people_lang, coding_lang):
        "Инициализируем атрибуты"
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    # Возвращаем атрибуты экземпляра класса в виде словаря в списке
    def get_list(self):
        return [self.__dict__]


def json_creater(data_list):
    "Запись JSON файла"
    with open("employee_list.txt", "w") as file:
        json.dump(data_list, file)
    "Открываем JSON файл"
    with open("employee_list.txt", "r") as file:
        total_data = json.load(file)
    return total_data

"Создаем функцию списка экземпляров класса"


def total_list(total_data, append_list):
    total_data = total_data
    append_list = append_list
    "Добавляем новый словарь"
    total_data.extend(append_list)
    "Новый JSON файл"
    json_creater(total_data)


def main():
    obj_1 = Employee('Ivasik', 'Telesik', 13, 'ivasik-telesik1732@izkrnanog.ua',
                     ['ходить', "говорить", "кодить"],
                     ['Україньська', "Англійська"], ['Python', "C++", "lisp"])
    obj_2 = Employee('Alex', 'Sokolov', 21, 'alex.sokolov@gmail.com', ['петь', "кодить"],
                     ['Англійська', "Французька"],
                     ['Python', "C++", "JavaScript"])

    "Присваиваем переменной данные класса JSON"
    data_list = json_creater(obj_1.get_list())
    "Запуск"
    total_list(data_list, obj_2.get_list())

main()