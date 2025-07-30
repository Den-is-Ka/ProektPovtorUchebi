# цифры = [2, 4, 6, 8 ,10]
#
# for циф in цифры:
#     print(циф)
#
# цифры = [2, 4, 6, 8 ,10]
#
# элемент = цифры[4]
# print(элемент)
#
# items = ["палатка", "спички", "одеяло", "нож", "зефирки", "крючок", "консервы"]
#
# index_1 = int(input())
# index_2 = int(input())
#
# print(items[index_1])
# print(items[index_2])
# print(type(items[index_2]))

# items = ["палатка", "спички", "одеяло", "нож", "зефирки", "крючок", "консервы"]
#
# items.append('24')
# print(items)
# print(len(items))
# lengs = len(items)
# print(lengs)
# for item in items:
#   print(item)


# fruits = ["яблоко", "груша"]
# fruits_2 = ["лимон", "банан", "киви"]
# # fruits.extend(["лимон", "банан", "киви"])
# fruits_3 = fruits + fruits_2
#
#
# for fruit in fruits_3:
#   print(fruit)

# list_1 = ["apple", "banana", "blueberry", "strawberry", "melon"]
# list_2 = ["blue", "orange", "blue", "blue", "yellow"]
# list_3 = [True, False, True, True, False, True]
#
# list_1_len = len(list_1)
# list_2_len = len(list_2)
# list_3_len = len(list_3)
#
# print(list_1_len, list_2_len, list_3_len)


# list_1 = ["apple", "banana", "strawberry", "melon"]
# print(len(list_1))
# print(type(len(list_1)))
# print(type(list_1))

# fruits = ["яблоко", "груша"]
# fruits_2 = ["лимон", "банан", "киви"]
#
# fruits.extend(fruits_2)
# print(fruits)
# print(type(fruits))

# list_1 = ["apple", "banana", "strawberry", "melon"]
# list_1[2] = 'ersfsdf'
# pos = 1
# print(list_1)
# print(list_1[pos])
# pos += 1
# print(list_1[pos])


# list_1 = ["apple", "banana", "blueberry", "strawberry", "melon"]
# print(list_1[2:])

list = ["apple", "арбуз", "banana", "корень", "blueberry", "strawberry", "железо", "melon"]
list_en = list[0:1] + list[2:3] + list[4:6] + list[-1:]
list_ru = list[1:2] + list[3:4] + list[-2:-1]

print(list_en)
print(list_ru)
print(list)

print(type(list_en))
print(type(list_ru))







