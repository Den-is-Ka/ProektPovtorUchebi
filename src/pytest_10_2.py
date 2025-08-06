# def add_five(number):
#     num = number + 5
#     # print(num)
#     return num
# assert add_five(10) == 15
#
# if add_five(10) == 16:
#     print('YES')
# else:
#     print('NO')
#
#
# if __name__ == '__main__':
#     add_five(10)

# def greet(name):
#     # print(f"Привет, {name}")
#     return f"Привет, {name}"
#
# assert greet("Анна") == 'Привет, Анна'
# assert greet("Вася") == 'Привет, Вася'
# assert greet("Мир") == 'Привет, Мир'
#
# if greet("Анна") == 'Привет, Анна':
#     print('Hopm')
# else:
#     print('XEP')
#
# if greet("Мир") == 'Привет, Мир':
#     print('Hopm')
# else:
#     print('XEP')
#
# if __name__ == '__main__':
#     greet("Анна")
#     greet("Вася")
#     greet("Мир")
#     print(greet("Анна"))
#     print(greet("Вася"))
#     print(greet("Мир"))



def is_even(number):
    if number % 2 == 0:
        # print('True')
        return True
    elif number % 2 == 1:
        # print('False')
        return False
    else:
        print('Это точно число?')

assert is_even(4) == True
assert is_even(7) == False
assert is_even(0) == True
if is_even(4) == True:
    print('Hopm')
else:
    print('XEP')

if is_even(7) == False:
    print('Hopm')
else:
    print('XEP')


if __name__ == '__main__':
    is_even(4)  # True
    is_even(7)  # False
    is_even(0)
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))






