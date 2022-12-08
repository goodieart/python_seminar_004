# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from collections import Counter


def get_prime_factors(value: int) -> list:
    result = []
    d = 2
    while value != 1:
        while value % d != 0:
            d += 1
        result.append(d)
        value /= d
    return result


def pretty_output(value: list):
    di = dict(Counter(value))
    for key, value in di.items():
        print(f'{key}^{value}', end=' + ')  # TODO: убрать последний +


user_input = int(input('Введите число N: '))
pf = get_prime_factors(user_input)
pretty_output(pf)
