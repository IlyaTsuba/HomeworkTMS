import re
import os
import sys


# task1

def task1(number):
    a, b = 0, 1
    for _ in range(number):
        yield a
        a, b = b, a + b


fib_num = task1(16)

for i in fib_num:
    print(i)


# task 2

def task2(number):
    while True:
        for num in range(1, number + 1):
            yield f"{num}-"


obj1 = task2(4)

for i in obj1:
    print(i, end='')

# # task 3
print(os.name)
print(sys.platform)
print(os.getcwd())

file_extensions = {"text_files": "txt", "csv_files": "csv"}
path = os.path.join(os.getcwd())
all_files = os.listdir(path)

for dir_name, extension in file_extensions.items():
    counter = 0
    folder_size = 0
    for cur_file in all_files:
        cur_file_extension = cur_file.split('.')[-1]
        if cur_file_extension == extension:
            counter += 1
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
                folder_size += os.path.getsize(cur_file) / 1000
                print(f"Folder {dir_name} was created!")
                os.replace(cur_file, f"{dir_name}/{cur_file}")
                print(f"File {cur_file} was replaced to folder {dir_name}")
            else:
                folder_size += os.path.getsize(cur_file) / 1000
                os.replace(cur_file, dir_name + "/" + cur_file)
                print(f"File {cur_file} was replaced to folder {dir_name}")
            all_files.remove(cur_file)

    print(f"{counter} files were replaced to folder {dir_name}")
    print(f"Total size of folder {dir_name} is {round(folder_size, 1)}Kbs")

# У меня тут вопрос. Я так и не придумал как переимоновать файл зная его название, но не зная расположение.......


# task 4

text = 'Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном заседании вину инкриминируемого ' \
       'правонарушения признала в полном объёме и суду показала, что 14 сентября 1876 года, будучи в состоянии ' \
       'алкогольного опьянения от безысходности, в связи с состоянием здоровья позвонила со своего стационарного ' \
       'телефона в полицию, сообщив о том, что у неё в квартире якобы заложена бомба. После чего приехали сотрудники ' \
       'полиции, скорая и пожарные, которым она сообщила, что бомба — это она.'

result = re.sub(r"([А-ЯЁ]\w+-)?([А-ЯЁ]\w+)( [А-ЯЁ]\w+){2}(?= [а-я]|[.,?!:-])", "N", text)

print(result)
