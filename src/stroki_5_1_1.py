# print("Введите в терминале 'да' или \"нет\" ")
#
# my_list = [1, 2, 3, 4, 5]
# slice_result = my_list[:]
# print(slice_result)


# info = input('Введите чтото!')
#
# for i, io in enumerate(info):
#     if i == True:
#         print(info)
#         print(info[0])
#         print(info[-1])
#         print(info[::-1])
#         print(info[1::2])
#         print(info[2:6])

# info = input('Введите текст!')
#
# text = info.split()
# for i in text:
#     print(i)
# print(info)
# print(text)
# print(len(info))
# print(len(info.split()))


# Условие:
# Твоя задача — пройтись по всей строке с помощью индексов (через range(len(...))) и:
# Найти все заглавные буквы в строке.
# Вывести:
# Сами заглавные буквы.
# Их позиции в строке (индексы).
#
# Используй цикл for i in range(len(text)): — чтобы получить индексы.
# Проверяй: if text[i].isupper():
# Можно хранить буквы в списке upper_letters и индексы в positions.
# upper_letters = []
# positions = []
# info = input('Введите текст!')
# for i in range(len(info)):
#     if info[i].isupper():
#         upper_letters.append(info[i])
#         positions.append(i)
#
# print(upper_letters)
# print(positions)


# Слово не должно содержать символ @.
# Слово не должно содержать пробел.
# Слово должно содержать хотя бы одну букву а или е.

# info = str(input('Введите текст!'))
# # for i in info:
# if '@' in info or ' ' in info:
#     print('Слово не принято: содержит символ \'@\' или пробел')
# elif 'a' in info or 'e' in info:
#     print('Слово допустимо!')





