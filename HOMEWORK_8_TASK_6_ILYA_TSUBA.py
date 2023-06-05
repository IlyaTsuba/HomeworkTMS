import json
import csv


# task1
def json_reading(file_path: str) -> list:
    with open(file_path, encoding='utf-8') as file_6:
        content_6 = json.load(file_6)  # Read data from json file
        return content_6


# task2
def json_converting_to_csv(file_path: str):
    content_6 = json_reading(file_path)

    columns = list(content_6[0].keys())

    with open("employees.csv", 'w', encoding='utf-8') as file_6_csv:  # Make csv file
        writer = csv.DictWriter(file_6_csv, fieldnames=columns, delimiter=",")
        writer.writeheader()
        writer.writerows(content_6)


def info_to_add():
    name = input("Set name: ")
    birthday = input("Set birthday: ")
    height = int(input("Set height: "))
    weight = float(input("Set weight: "))
    car = bool(input("Input true if person has car, else input false: "))
    languages = [i for i in input("Set languages: ").split()]
    data_to_add = {"name": name, "birthday": birthday, "height": height,
                   "weight": weight, "car": car, "languages": languages}
    return data_to_add


# task3
def add_data_to_json(file_path: str, repeats: int):
    data_from_json = json_reading("employees.json")
    while repeats != 0:
        data_to_add = info_to_add()
        repeats -= 1
        data_from_json.append(data_to_add)
        with open(file_path, "w", encoding='utf-8') as file_6:
            json.dump(data_from_json, file_6, indent=4)


# task 4
def add_data_to_csv(file_path: str, repeats: int):
    while repeats != 0:
        data_to_add = info_to_add()
        repeats -= 1
        columns = list(data_to_add.keys())
        with open(file_path, "a", encoding='utf-8') as file_csv:
            writer = csv.DictWriter(file_csv, fieldnames=columns, delimiter=",")
            writer.writerow(data_to_add)


# task5
def get_person_info(file_path: str, person: str) -> dict:
    data_from_json = json_reading(file_path)
    for person_info in data_from_json:
        if person_info["name"] == person:
            return person_info


# print(get_person_info('employees.json', 'Maria Ivanova'))

# task6
def get_persons_per_language(file_path: str, language: str) -> list:
    data_from_json = json_reading(file_path)
    list_of_employees = []
    for person_info in data_from_json:
        if language in person_info["languages"]:
            list_of_employees.append(person_info["name"])
    return list_of_employees


# task7
def get_avg_height_per_year(file_path: str, year: int):
    data_from_json = json_reading(file_path)
    list_of_employees_height = []
    for person_info in data_from_json:
        if int(person_info["birthday"][-4:]) < year:
            list_of_employees_height.append(person_info['height'])
    average_height = sum(list_of_employees_height) / len(list_of_employees_height)
    return f"Average height of employees whose birth year older than {year} = {average_height} cm"


def interaktivchik():
    dict_of_funcs = {1: ["Чтобы считать данные из json файла введите 1", json_reading],
                     2: ["Чтобы сконвертировать данные из json файла в csv, введите 2", json_converting_to_csv],
                     3: ["Чтобы добавить информацию о новом сотруднике в json файл введите 3", add_data_to_json],
                     4: ["Чтобы добавить информацию о новом сотруднике в csv файл введите 4", add_data_to_csv],
                     5: ["Чтобы вывести информацию о сотруднике по имени введите 5", get_person_info],
                     6: ["Чтобы получить список сотрудников, влядеющим языком введите 6", get_persons_per_language],
                     7: ["Чтобы получить средний рост сотрудников старше введенного года введите 7",
                         get_avg_height_per_year],
                     0: ["Чтобы выйти из интерактивчика введите 0", "харэ"]}

    while True:
        for dict_el in dict_of_funcs.values():
            print(f"{dict_el[0]}")
        choice = int(input("Введите номер задания: "))
        if choice == 0:
            exit()
        else:
            file_path = input("Введите путь к файлу ")
            if choice in [1, 2]:
                dict_of_funcs[choice][1](file_path)
            elif choice in [3, 4]:
                dict_of_funcs[choice][1](file_path, int(input("Введите кол-во человек для добавления: ")))
            elif choice == 5:
                print(dict_of_funcs[choice][1](file_path, input("Введите имя сотрудника: ")))
            elif choice == 6:
                print(dict_of_funcs[choice][1](file_path, input("Введите язык программирования: ")))
            elif choice == 7:
                print(dict_of_funcs[choice][1](file_path, int(input("Введите год: "))))
        print()


interaktivchik()
