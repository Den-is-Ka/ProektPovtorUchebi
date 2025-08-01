
# original_string = "Hello, World!"
# new_word = "Python"
# modified_string = f"{original_string} {new_word}"
# print(modified_string)
#
# original_string = "Hello, World!"
# modified_string = f"M{original_string[1:]}"
# print(modified_string)


# words = ["counter", "clock", "wise"]
# result = ""
#
# for word in words:
#     result += word
#
# print(result)

#
# info_1 = input('Введите имя!')
# info_2 = input('Введите праздник!')
# info_3 = input('Введите пожелание!')
#
# print(f'{info_1} поздравляю с {info_2} и желаю тебе {info_3}')


# info_1 = input('Введите text!')
#
# info_2 = info_1.lower()
# info_3 = info_1.upper()
# info_4 = info_1.title()
#
# print(info_1)
# print(info_2)
# print(info_3)
# print(info_4)


text = "My favorite color is RED."
old_color = "RED"
new_color = "bRRRRRRe"


formatted_text = text.replace(old_color, new_color)
formatted_text_1 = text.replace('o', '0')
formatted_text_2 = text
text_1 = formatted_text_2.split()
text_2 = formatted_text_2.split('o')
text_3 = formatted_text_2.split('o', 2)
text_4 = ' † '.join(text_1)

print(formatted_text)
print(formatted_text_1)
print(text_1)
print(text_2)
print(text_3)
print(text_4)




