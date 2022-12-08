# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint


def get_polynomial(k: int) -> list:
    li = [randint(0, 100) for _ in range(k + 1)]
    li = list(filter(lambda i: i != 0, li))
    li.sort()
    li = list(map(str, li))
    if k > 1:
        res = [f'{li[i]}*x^{i}' for i in range(len(li) - 1, 0, -1)]
        res_str = f"{' + '.join(res)} + {li[0]} = 0"
    elif k == 1:
        res_str = f'{li[0]}*x^{1} = 0'
    return res_str


def save_data(data: str):
    with open('data.txt', 'w') as f:
        f.write(data)


save_data(get_polynomial(8))
