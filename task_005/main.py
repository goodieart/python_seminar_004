# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def get_polynomial(values: list) -> str:
    values.reverse()
    l = len(values)
    if l > 1:
        res = [
            f'{values[i]}*x{"**" + str(i) if i > 1 else ""}' for i in range(l - 1, 0, -1)]
        res_str = f'{" + ".join(res)} + {values[0]}'
    elif l == 1:
        res_str = f'{values[0]}*x^{1}'
    return res_str


def get_ratios(value: str) -> list:
    li = value.split('+')
    buffer = []
    for i in li:
        buffer.append(int(i.split('*')[0]))
    return buffer


def sum_ratios(r1: list, r2: list) -> list:
    r1.extend([0,] * (len(r2) - len(r1)))
    r2.extend([0,] * (len(r1) - len(r2)))
    return list(map(sum, zip(r1, r2)))


def load_data(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()


def save_data(file: str, data):
    with open(file, 'w') as f:
        f.write(data)


s1 = load_data('input_1.txt')
s2 = load_data('input_2.txt')
r1 = get_ratios(s1)
r2 = get_ratios(s2)
r_sum = sum_ratios(r1, r2)
p = get_polynomial(r_sum)

save_data('output.txt', p)
