mesadge_num = int(input("введите число: "))
if mesadge_num > 0:
    print('Есть сообщения')
else:
    print('Сообщений нет')

if __name__ == '__main__':
    print


слово_1 = input("введите слово: ")
слово_2 = input("введите слово: ")
слово_3 = input("введите слово: ")

counter = 0
if 'ч' in слово_1:
    counter += 1
if 'ч' in слово_2:
    counter += 1
if 'ч' in слово_3:
    counter += 1

print(f'Набралось {counter} слов')

if __name__ == '__main__':
    print

residency = int(input("введите время жизни на одном месте: "))
salary = int(input("введите вашу зарплату: "))
experience = int(input("введите стаж работы: "))

counter = 0
if residency >= 2:
    counter += 1
else:
    print('Мало жили на одном месте')
if salary >= 50000:
    counter += 1
else:
    print('Мало зарабатываете')
if experience >= 2:
    counter += 1
else:
    print('Малый стаж')

if counter == 3:
    print('Вам одобрен кредит')
elif counter == 2:
    print('Вам немного не хватает')
else:
    print('Вам не хватает, идите работать')

print(f'ваш счетчик составляет {counter} балов')

