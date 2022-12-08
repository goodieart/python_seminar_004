# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint


def get_polinom(k: int) -> list:
    li = [randint(0, 100) for _ in range(k)]
    li = list(filter(lambda i: i != 0, li))
    li.sort()
    li = list(map(str, li))
    if k > 1:
        res = [f'{li[i]}*x^{i}' for i in range(len(li) - 1, 0, -1)]
        res_str = f"{' + '.join(res)} + {li[0]} = 0"
    elif k == 1:
        res_str = f'{li[0]}*x^{1} = 0'
    return res_str


print(get_polinom(8))
