from math import *
from consts import *


def f(step):
    return x0 + v0x * step + ax * step * step / 2


x = x0
y = y0
h = float(input())
ax = -G * M * x / ((x ** 2 + y ** 2) ** (3 / 2))
fi = (f(h) - f(h / 2)) / f(h)
print(fi)
print(f(h/2))
