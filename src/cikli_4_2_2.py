import pandas as pd
from config import DATA_DIR
import os
import json

titanic_path = os.path.join(DATA_DIR, 'titanic.csv')
def get_pass_by_age_and_price(df, age=30, price=50):
    filtred_pass = df[(df['Age'] < age) & (df['Fare'] > price)]
    sorted_by_name = filtred_pass.sort_values('Name')
    return sorted_by_name
"""{
    "1st": {
        "average_ticket_price": 84.15,
        "passenger_count": 216
    },
    "2nd": {
        "average_ticket_price": 20.66,
        "passenger_count": 184
    },
    "3rd": {
        "average_ticket_price": 13.68,
        "passenger_count": 491
}
}"""

def get_class_info(df):
    classes = df.groupby('Pclass', as_index=False)
    agginfo = classes.agg(average_ticket_price=('Fare', 'mean'),passenger_count=('PassengerId', 'count')).round(2)
    sufix = {1: "1st", 2: "2nd", 3: "3rd"}
    agginfo['Pclass'] = agginfo['Pclass'].apply(lambda x: sufix[x])
    agg_dict = agginfo.to_dict('records')
    result = {}
    for clas_info in agg_dict:
        pclass = clas_info.pop('Pclass')
        result[pclass]= clas_info
    return result




data = pd.read_csv(titanic_path)
result = get_class_info(data)
result_to_print = json.dumps(result, indent=4, ensure_ascii=False)

print(result_to_print)



numbers = [3, 6, 1, 8, 5, 4, 2, 7, 10, 1, 13, 20, 22, 5, 7, 9]

nums = 0
nums2 = 0

for num in numbers:
    if num % 2 == 0:
        nums += 1
    elif num % 2 == 1:
        nums2 += 1

print(nums)
print(nums2)

x = int(input('Введи число: '))
som = 0
while x != 0:
    if x > 0:
        som += 1
        x = int(input('Введи число: '))
    elif x < 0:
        x = int(input('Введи число: '))
    elif x == 0:
        break


print(som)
# print(som)

x = int(input('Введи число: '))
max_num = None

while x != 0:
    if x > 0:
        som += 1
        max_num = som
        if som > max_1:
            max_num = som
        x = int(input('Введи число: '))
    elif x < 0:
        x = int(input('Введи число: '))
    elif x == 0:
        print('Числа не введены')
        break

print(som)
print(max_num)

x = int(input('Введи число: '))
min_num = None

while x != 0:
    if min_num is None or x < min_num:
        min_num = x
    x = int(input('Введи число: '))

if min_num is not None:
    print('Минимальное число:', min_num)
else:
    print('Числа не введены')


x = int(input('Введи число: '))
sum_1 = 0
while x != 0:
    if x % 2 == 0:
        sum_1 += x
    x = int(input('Введи число: '))
    # elif x % 2 == 1:
    #     # sum_1 += x
    #     x = int(input('Введи число: '))
    # elif x == 0:
    #     break

print(sum_1)
print(f'вот что в итоге: {sum_1}')

gfhjkm = '1221'
num = input('Введи число: ')
while True:
    if num == gfhjkm:
        print('VERNO')
        break

    elif num != gfhjkm:
        print('NO')
        num = input('Введи число: ')

gfhjkm = '22'
num = input('Введи число: ')
while True:
    if num == gfhjkm:
        print(f'правильно число: {num}')
        break

    elif num != gfhjkm:
        print('Не правильно')
        num = input('Попробуй еще: ')


numbers = [0, -3, -1, 4, 8, -7, 6, 11, 14]
num = 0
sum_num = 0
# num_1 = 0
for n in numbers:
    if n < 0:
        continue
    elif n % 2 == 1:
        num += n
        sum_num += 1
    elif num > 14:
        break

    print(num)
    print(sum_num)
    print(num_1)


numbers = [-5, 3, -2, 6, 9, 8, 4, -1, 2]

count = 0
sum_count = []
for n in numbers:
    if n == 9:
        break
    elif n < 0 :
        continue
    else:
        count += 1
        sum_count.append(n)

print(f'учтены: {sum_count }')
print(count)


numbers = [-4, 0, -3, 6, 2, 8, 7, 10, 1]

for n, num in enumerate(numbers):
    if num <= 0:
        continue
    elif num % 2 ==1:
        print(n, num)
        break

numbers = [-1, 4, 0, 3, 8, -6, 2, 5, 10]
count = 0
for n, num in enumerate(numbers):
    if num < 0 or num % 2 != 0:
        continue
    count += 1
    if count == 3:
        print(f'число {num} индекс {n}')
        break
























