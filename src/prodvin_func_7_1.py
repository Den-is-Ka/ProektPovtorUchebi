#
# def greet(name, greeting='Hoi', punctuation='.'):
#     print(f"{greeting}, {name}{punctuation}")
#
#
#
#
# if __name__ == '__main__':
#     greet('Nora')
#     greet('NoZa', greeting='Пириветь')
#     greet('NorKa', greeting='Пириветь', punctuation='!!@!')
#     greet('Nora')


# def shopping_list(*items, **comments):
#     for item in items:
#         if item in comments:
#             print(f'{item} ({comments[item]})')
#         else:
#             print(f'{item}')
#
#
# if __name__ == '__main__':
#     shopping_list("хлеб", "молоко", 'крупа', "сыр", хлеб="чёрный", молоко="1 литр")

# def sum_numbers(*numbers):
#     print("Числа:", numbers)
#     print("Сумма:", sum(numbers))
#
#
# if __name__ == '__main__':
#     sum_numbers(2, 4, 6)
#     sum_numbers(10)
#     sum_numbers()


# def pet_info(name, animal, age):
#     print(f'{name} {animal} {age}')
#
# if __name__ == '__main__':
#     pet_info('Люська', "кошка", 34)
#     pet_info('Мяфька', "рыба", 4)

# def pet_info(name, animal, age):
#    result = f'{name} {animal} {age}'
#    print(result)
#    return result
#
#
# if __name__ == '__main__':
#     # print(result)
#     pet_info('Люська', "кошка", 34)
#     pet_info('Мяфька', "рыба", 4)
#     # print(result)

def pet_info(name, animal, age):
    return f'{name} {animal} {age}'

# result = pet_info('Люська', "кошка", 34)
# print(result)

# if __name__ == '__main__':
#     result = pet_info('Люська', "кошка", 34)
#     result_2 = pet_info('Veська', "dошка", 134)
#     print(result)
#     print(result_2)
#
#
# def full_name(first_name, last_name, age):
#     return f'{first_name} {last_name} {age}'
#
# if __name__ == '__main__':
#     кусь = full_name('ыиаыдваи', "ноно", 12)
#     print(кусь)


# def create_profile(name, city="Не указан", age=18):
#     return f" {name}, {city}, {age}"
#
# result = create_profile('Анна', city='Moskow', age=25 )
# print(result)
#
# def greet(name, time_of_day="день"):
#     return f'Добрый {time_of_day}, {name}'
#
# result = greet('Гога', "ночь")
# result_2 = greet('Тоха', "вечерь")
# result_3 = greet('Тоха')
# print(result)
# print(result_2)
# print(result_3)

# def note(text, *tags):
#     print(f"Заметка: {text}")
#     if tags:
#         print("Метки:", ', '.join(tags))
#     else:
#         print("Метки: нет")
#
# if __name__ == '__main__':
#     note("Купить хлеб", "магазин", "еда")
#     note("Позвонить бабушке", "вечером")


# def product_info(name, **features):
#     print(f'{name}')
#     if features:
#         print('Допы')
#         for key, value in features.items():
#             print(f'{key}: {value}')
#     else:
#         print('NO NO NO')
#
# if __name__ == '__main__':
#     product_info("Ноутбук", brand="Asus", weight="2 кг", color="чёрный")
#     product_info("Книга", ganr='фантастика')


# def make_order(*items, **options):
#     print(f'{items}')
#     if options:
#         print('Допы')
#         for key, nazvanie in options.items():
#             print(f'{key}: {nazvanie}')
#     else:
#         print('Допов нету')
#
#
#
# if __name__ == '__main__':
#     make_order("пицца", "сок", "бургер", доставка="курьер", оплата="наличные")
#     make_order("чай", "печенье", оплата="наличные")
#     make_order()

# def create_ticket(*people, **options):
#     print(f'{people}')
#     if options:
#         print('Уточнения')
#         for key, parametr in options.items():
#             print(f"{parametr}")
#     else:
#         print('Нюансов нету')
#
# if __name__ == '__main__':
#     create_ticket("Анна", "Игорь", event="Концерт", date="12.10.2025", place="Москва")
#     create_ticket("Лера", date="01.01.2026")


# def print_profile(name, age, city):
#     print(f"Имя: {name}, Возраст: {age}, Город: {city}")
#
# list_data = ["Алиса", 30, "Москва"]
# dict_data = {"name": "Игорь", "age": 25, "city": "Казань"}
#
# print_profile(*list_data)
# print_profile(**dict_data)
#
# def add_numbers(a, b):
#     return a + b
#
#
# numbers_list = [6, 2]
#
# result = add_numbers(*numbers_list)
# print(result)


# sdjflsfg = lambda x, y, z: x * y + z
# result = sdjflsfg(2,3,4)
# print(result)
#
#
# sdjflsfg = lambda x, y: x + y
# result = sdjflsfg('rjhtym', ';vs[')
#
# print(result)

# numbers = list(range(1, 21))
#
# event_numbers = list(filter(lambda x: x % 2 == 1, numbers))
# print(event_numbers)


# numbers = list(range(1, 21))
# event_numbers = list(map(lambda x: x ** 2, numbers))
# print(event_numbers)

# try:
#     pervoe = int(input('введите делимое: '))
#     vtoroe = int(input('введите делитель: '))
#     itog = pervoe / vtoroe
# except ZeroDivisionError:
#     print("На 0 не делим")
# except ValueError:
#     print('число вводи да')
# else:
#     print(itog)



# try:
#     slovo = input('введите слово: ')
#     index = int(input('введите индекс: '))
#     print('Буковка:', slovo[index])
# except ValueError:
#     print('Число надо вводить, бестолочь')
# except IndexError:
#     print('Индекс далеко далеко за гранью')

# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Ошибка: Вы пытаетесь сломать математику. Делить на 0 нельзя!")
# else:
#     print(f"Результат: {result}")



# try:
#     pervoe = int(input('введите делимое: '))
#     vtoroe = int(input('введите делитель: '))
#     itog = pervoe / vtoroe
# except ZeroDivisionError:
#     print("На 0 не делим")
# except ValueError:
#     print('число вводи да')
# else:
#     print(itog)
# finally:
#     print('Прогу закрой и вали')
# code == '1234baba'
# try:
#     code = input("Пароль введи: ")
#     if len(code) < 6:
#         raise ValueError('Кортковато словцо')
#     if not any(char.isdigit()for char in code):
#         raise ValueError('А цифры где?')
# except ValueError as e:
#     print('Ошибка:', e)
# else:
#     print('ну ладно заходи')
# finally:
#     print('Ну все')

try:
    code = input("введи имя: ")
    forbidden = ["admin", "root", "moder"]
    if " " in code:
        raise ValueError('зачем тут пробел')
    if code.lower() in forbidden:
        raise ValueError('запрещенка')
except ValueError as e:
    print('Ошибка:', e)
else:
    print('имя принято')
finally:
    print('Ну все')
