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


# def is_even(number):
#     if number % 2 == 0:
#         # print('True')
#         return True
#     elif number % 2 == 1:
#         # print('False')
#         return False
#     else:
#         print('Это точно число?')
#
# assert is_even(4) == True
# assert is_even(7) == False
# assert is_even(0) == True
# if is_even(4) == True:
#     print('Hopm')
# else:
#     print('XEP')
#
# if is_even(7) == False:
#     print('Hopm')
# else:
#     print('XEP')
#
#
# if __name__ == '__main__':
#     is_even(4)  # True
#     is_even(7)  # False
#     is_even(0)
#     print(is_even(4))
#     print(is_even(7))
#     print(is_even(0))


# def multiply(a, b):
#     return a * b
#
#
# # if __name__ == '__main__':
# #     print(multiply(3, 5))
# #     print(multiply(0, 999))
# #     print(multiply(-2, 4))
# #     print(multiply(-3, -7))
# #     print(multiply(1.5, 2))
#
# def divide(a, b):
#     if not isinstance (a, (int, float)) or not isinstance(b, (int, float)):
#         raise TypeError('надо числовое')
#     if b == 0:
#         raise ZeroDivisionError('на ноль не делим')
#     return a / b

# def is_valid_email(email: str):
#     if ' ' in email or '@' not in email or '.' not in email.split('@')[-1]:
#         raise ValueError('адрес не точен')
#     return True


# if __name__ == '__main__':
#     print(is_valid_email("user@example.com"))


# def is_strong_password(password: str):
#     if len(password) <8:
#         raise ValueError('слабый пароль')
#     if not any(elm.isdigit() for elm in password):
#         raise ValueError('слабый пароль')
#     if not any(elm.isupper() for elm in password):
#         raise ValueError('слабый пароль')
#     return True


# if __name__ == '__main__':
#     print(is_strong_password("1dDgd"))


# def reverse_list(lst):
#     return lst[::-1]
#
# if __name__ == '__main__':
#     print(reverse_list([1, 2, 3, 4, 5]))

# def calculate_discount(price, user_type):
#     if user_type == "regular":
#         return price
#     if user_type == "vip":
#         return price * 0.9
#     if user_type == "staff":
#         return price * 0.75
#     else:
#         raise ValueError('это вообще кто?')


def is_leap_year(year: int) -> bool:
    if year % 400 ==0:
        return True
    if year % 100 ==0:
        return False
    if year % 4 ==0:
        return True
    return False










