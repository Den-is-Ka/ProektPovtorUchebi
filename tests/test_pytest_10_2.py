import pytest
from src.pytest_10_2 import is_leap_year

# def test_positive():
#     assert multiply(3, 5) == 15
#
# def test_zero():
#     assert multiply(999, 0) == 0
#
# def test_negatives():
#     assert multiply(-2, 4) == -8
#
# def test_2_negative():
#     assert multiply(-3, -7) == 21
#
# def test_floats():
#     assert multiply(1.5, 2) == 3.0
#
# def test_normal():
#     assert divide(10, 2) == 5.0
#
# def test_zeros():
#     with pytest.raises(ZeroDivisionError):
#         divide(10, 0)
#
# def test_negative():
#     assert divide(-2, 4) == -0.5
#
# def test_int_float():
#     with pytest.raises(TypeError):
#         divide("10", 0)

# def test_ghfbkmyjcnm():
#     assert is_valid_email("user@example.com") == True
#     assert is_valid_email("my.mail@site.ru") == True
# def test_ghfbkmyjcnm():
#     assert is_valid_email("user@example.com") == True
#     assert is_valid_email("my.mail@site.ru") == True
#
# def test_necodgflftn():
#     with pytest.raises(ValueError):
#         is_valid_email("user@site")
# def test_necodgflftn():
#     with pytest.raises(ValueError):
#         is_valid_email("user@site")
# @pytest.mark.parametrize('password', ["Qwerty123",
#     "Admin2024",
#     "Strong1X",
#     "PassWORD8",])
# def test_isdigit(password):
#     assert is_strong_password(password) is True
#
#
# @pytest.mark.parametrize('password', ["Qwggeggg",
#     "Adыввmin",
#     "23423424234",
#     "Passfghhhg",])
# def test_invalid(password):
#     with pytest.raises(ValueError, match="слабый пароль"):
#         is_strong_password(password)

# @pytest.fixture
# def my_list():
#     return [1, 2, 3, 4, 5]
#
# def test_reverse_list(my_list):
#     assert reverse_list(my_list) == [5, 4, 3, 2, 1]
#
# def test_reverse_empty():
#     assert reverse_list([]) == []


# @pytest.fixture
# def sample_price():
#     return 1000
#
# @pytest.fixture
# def user_types():
#     return ["regular", "vip", "staff"]
#
# @pytest.mark.parametrize('user_type, expected',[('regular', 1000), ('vip', 900), ('staff', 750),])
#
# def test_discount_calculation(sample_price, user_type, expected):
#     assert calculate_discount(sample_price, user_type) == expected
#
# def test_invalid_user_type(sample_price):
#     with pytest.raises(ValueError, match='это вообще кто?'):
#         calculate_discount(sample_price, "ha_ha_ha_her")

def test_delim_in_400():
    assert is_leap_year(2000) is True

def test_delim_in_100_not_400():
    assert is_leap_year(1900) is False

def test_delim_in_4_not_100():
    assert is_leap_year(2024) is True

def test_delim_not_4():
    assert is_leap_year(2023) is False



