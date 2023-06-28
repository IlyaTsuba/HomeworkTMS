import re
import os
import sys
# task1

def task1(number):
    a, b = 0, 1
    for _ in range(number):
        yield a
        a, b = b, a + b


fib_num = task1(15)

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

# task 3
print(os.name)
print(sys.platform)
print(os.getcwd())

# task 4

text = 'Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном заседании вину инкриминируемого ' \
       'правонарушения признала в полном объёме и суду показала, что 14 сентября 1876 года, будучи в состоянии ' \
       'алкогольного опьянения от безысходности, в связи с состоянием здоровья позвонила со своего стационарного ' \
       'телефона в полицию, сообщив о том, что у неё в квартире якобы заложена бомба. После чего приехали сотрудники ' \
       'полиции, скорая и пожарные, которым она сообщила, что бомба — это она.'

result = re.sub(r"([А-ЯЁ]\w+-)?([А-ЯЁ]\w+)( [А-ЯЁ]\w+){2}(?= [а-я]|[.,?!:-])", "N", text)

print(result)
