from math import *
from consts import *


def f(step):
    return x0 + v0x * step + ax * step * step / 2


x = x0
y = y0
h = float(input())
ax = -G * M * x / ((x ** 2 + y ** 2) ** (3 / 2))
fi = (f(h) - f(h / 2)) / f(h)
print('rel error =', fi)

p0 = v0x
p = p0 + h*ax
x = x + h*(p + p0)/2
print('x =', x)

ay = -G * M * y / ((x ** 2 + y ** 2) ** (3 / 2))
k0 = v0y
k = k0 + h*ay
y = y + h*(k + k0)/2
print('y =', y)
