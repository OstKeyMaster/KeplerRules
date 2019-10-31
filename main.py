from consts import *
import matplotlib.pyplot as plt


def f(step):
    return x_start + v0x * step + ax * step * step / 2


fig = plt.figure()
sun = plt.scatter(0.0, 0.0, c='r')

x0 = x_start
y0 = y_start
p0 = v0x
k0 = v0y
s = 'rgb'

#  ax = -G * M * x0 / ((x0 ** 2 + y0 ** 2) ** (3 / 2))
#  fi = (f(h) - f(h / 2)) / f(h)
#  print('rel error =', fi)

for i in range(times):
    ax = -G * M * x0 / ((x0 ** 2 + y0 ** 2) ** 1.5)
    ay = -G * M * y0 / ((x0 ** 2 + y0 ** 2) ** 1.5)

    p = p0 + h * ax
    k = k0 + h * ay

    x = x0 + p0 * h + ax * h**2 / 2
    # x = x0 + h * (p + p0) / 2
    y = y0 + k0 * h + ax * h**2 / 2
    # y = y0 + h * (k + k0) / 2

    line = plt.plot([x0, x], [y0, y], s[i % 3])
    # text = plt.text(x, y, str(i+1))
    # r = (x**2 + y**2)**0.5
    print(i)

    x0 = x
    y0 = y
    p0 = p
    k0 = k

grid = plt.grid(True)
plt.show()
