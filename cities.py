#данная функция преобразует текстовый документ с городами России
#и убирает все "\n" в питонячий, чтобы потом была возможность 
# работать со списком городов

def file_read():
    char = 'абвгдеёжзийклмнопрстуфхцчшщэюя'
    cities_dict = {}
    for letter in char:
        cities_dict[letter] = []
    print(cities_dict)
    with open('cities_of_Russia.txt') as cities_list:
        cities = [city.strip().lower() for city in cities_list]
        for city in cities:
            cities_dict[city[0]].append(city)
    
    print(cities_dict['а'])
    return cities, cities_dict


#функция находящая город на последнюю букву города пользователя
def answer(user_city, cities_of_russia, used_cities):
    cities = cities_of_russia
    city = user_city
    forbidden_list = ['й', 'ь', 'ъ', 'ы']
    last_letter = ''
    city_answer = ''
    print(used_cities)
    if city in cities:
        if city[-1] in forbidden_list:
            last_letter = city[-2]
        else:
            last_letter = city[-1]
        #print(last_letter)  
        #print(city[0])  
    for city in cities:
        if city[0] == last_letter:
            city_answer = city
            continue

    used_cities.append(user_city)
    print(len(used_cities))
    used_cities.append(city_answer)
    print(len(used_cities))
    cities.remove(user_city)
    print(len(cities))
    cities.remove(city_answer)
    print(len(cities))
    return city_answer, cities, used_cities

def city_control (user_city, citices_of_russia, used_cities):

    #print(used_cities)
    if user_city in used_cities:
        print('Такой город уже был, попробуйте снова')
        return True
    elif user_city not in citices_of_russia:
        #raise ValueError ('нет такого города')
        print('В моей базе нет такого города, попробуйте снова')
        return True
    elif len(used_cities) != 0:
        forbidden_list = ['й', 'ь', 'ъ', 'ы']
        if user_city[-1] in forbidden_list:
            if user_city[-1] != used_cities[-1][-2]:
                print(f"Ваш город должен начинаться на букву '{used_cities[-1][-2].upper()}', попробуйте снова")
                return True
        elif user_city[-1] != used_cities[-1][-1]:
            print(f"Ваш город должен начинаться на букву '{used_cities[-1][-1].upper()}', попробуйте снова")
            return True


used_cities = []
#часть основного кода (необходимо перенести ее в самый конец)
cities_of_russia = file_read()
while True:
    user_city = input('Введите город: ').strip().lower()
    if city_control(user_city, cities_of_russia, used_cities):
        continue
    #print(len(cities_of_russia))

    city, cities_of_russia, used_cities = answer(user_city, cities_of_russia, used_cities)
    print(city.capitalize())           



     