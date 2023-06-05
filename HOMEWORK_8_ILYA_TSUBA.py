# task1
print("____TASK1____")


with open('lines.txt', encoding='utf-8') as file_1:  # reading data from file
    content = list(map(str.strip, file_1.readlines()))  # Making a list
    res_list = []
    for i in content:  # Delete not alpha symbols
        result_string = ""
        for j in i:
            result_string += j if j.isalpha() else " "
        res_list.append(result_string)

    result = []

    for s in res_list:  # Make a dict with words and number of repetitions for each word
        res_dict = {}
        for word in s.split():
            if word not in res_dict:
                res_dict[word] = 1
            elif word in res_dict:
                res_dict[word] += 1
        max_value = 1
        most_popular_word = ""

        for key, value in res_dict.items():  # Find most popular word and number of repetitions
            if res_dict[key] > max_value:
                max_value = res_dict[key]
                most_popular_word = key
        result.append(f"Most popular word in a string is {most_popular_word}, number of repetitions = {max_value}")

with open('result_task1.txt', "w", encoding='utf-8') as result_file_task1:
    result_file_task1.writelines(line + '\n' for line in result)

# task2
print("____TASK2____")


file_name_2 = input("Set a name of file for task 2:")
with open('stop_words.txt', encoding='utf-8') as stop_words:  # Make a list of stop words
    stop_words_list = stop_words.readline().split()

with open(file_name_2, encoding='utf-8') as file_2:  # Open a test file
    content2 = file_2.read().strip()
    content_lower = content2.lower().strip()
    for word in stop_words_list:
        if word in content_lower:
            content_lower = content_lower.replace(word, "*" * len(word))  # Replace stop word
    [print(j if j == '*' else i, end='') for i, j in zip(content2, content_lower)]

# task3
print("____TASK3____")


file_name_3 = input("Set a name of file for task 3:")
with open(file_name_3, encoding='utf-8') as file_3:
    content_3 = list(map(str.split, file_3.readlines()))
    for i in content_3:
        if int(i[-1]) < 3:
            print(i[0], i[1])


# task4
print("____TASK4____")


file_name_4 = input("Set a name of file for task 4:")
with open(file_name_4, encoding='utf-8') as file:
    content4 = list(map(str.strip, file.readlines()))
    result_string = ""
    for i in content4:
        for j in i:
            result_string += j if j.isdigit() else " "
    result_string = [int(i) for i in result_string.split()]
    print(sum(result_string))


# task5
print("____TASK5____")


file_name_5 = input("Set a name of file for task 5:")
with open(file_name_5, encoding='utf-8') as file_5:
    content_5 = file_5.readlines()
    content_5 = [i.strip() for i in content_5]
    print(content_5)
    index = 1
    for s in content_5:
        for char in s:
            if 65 <= ord(char) <= 90:
                d = ord(char) + index
                if d > 90:
                    d -= 26
                print(chr(d), end="")
            elif 97 <= ord(char) <= 122:
                d = ord(char) + index
                if d > 122:
                    d -= 26
                print(chr(d), end="")
        index += 1
        print()


