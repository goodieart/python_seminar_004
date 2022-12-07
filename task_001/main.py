# Вычислить число Пи c заданной точностью d

# *Пример:*

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415
from math import pi as p


def pi(d):
    p16 = 1.0
    pi = 0
    #precision = len(str(d).split('.')[1])
    i = 0
    while d < 1:
        pi += 1.0/p16 * (4.0/(8*i + 1) - 2.0/(8*i + 4) - 1.0/(8*i + 5) - 1.0/(8*i+6))
        p16 *= 16
        d *= 10
        i += 1
    return round(pi, i)

print(pi(0.001))
print(p)