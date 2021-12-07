#данная функция преобразует текстовый документ с городами России
#и убирает все "\n" в питонячий, чтобы потом была возможность 
# работать со списком городов
import random

def file_read():
    char = 'абвгдеёжзийклмнопрстуфхцчшщэюя'
    cities_dict = {}
    for letter in char:
        cities_dict[letter] = []
    with open('cities_of_Russia.txt') as cities_list:
        cities = [city.strip().lower() for city in cities_list]
        for city in cities:
            cities_dict[city[0]].append(city)
    return cities_dict

# рандомный выбор города из списка
def generate_city(letter, cities_dict):
    city = random.choice(cities_dict[letter])
    return city

#функция находящая город на последнюю букву города пользователя
def answer(user_city, cities_of_russia, used_cities):
    cities = cities_of_russia
    city = user_city
    forbidden_list = ['й', 'ь', 'ъ', 'ы']
    last_letter = ''
    city_answer = ''
    if city[-1] in forbidden_list:
        last_letter = city[-2]
    else:
        last_letter = city[-1]
    city_answer = generate_city(last_letter, cities_of_russia)

    used_cities.append(user_city)
    print(len(used_cities))
    used_cities.append(city_answer)
    print(len(used_cities))
    return city_answer, cities, used_cities

def city_control (user_city, citices_of_russia, used_cities):
    last_letter = user_city[0]
    char = 'абвгдеёжзийклмнопрстуфхцчшщэюя'
    if last_letter not in char:
        print('В моей базе нет городана такую букву')
        return True
    elif user_city in used_cities:
        print('Такой город уже был, попробуйте снова')
        return True
    elif user_city not in citices_of_russia[last_letter]:
        print('В моей базе нет такого города, попробуйте снова')
        return True
    elif len(used_cities) != 0:
        forbidden_list = ['й', 'ь', 'ъ', 'ы']
        if used_cities[-1][-1] in forbidden_list:
            if user_city[0] != used_cities[-1][-2]:
                print(f"Ваш город должен начинаться на букву '{used_cities[-1][-2].upper()}', попробуйте снова")
                return True
        elif user_city[0] != used_cities[-1][-1]:
            print(used_cities)            
            print(f"Ваш город должен начинаться на букву '{used_cities[-1][-1].upper()}', попробуйте снова")
            return True


used_cities = []
#часть основного кода (необходимо перенести ее в самый конец)
cities_of_russia = file_read()
while True:
    user_city = input('Введите город: ').strip().lower()
    if city_control(user_city, cities_of_russia, used_cities):
        continue

    city, cities_of_russia, used_cities = answer(user_city, cities_of_russia, used_cities)
    print(city.capitalize())           



     