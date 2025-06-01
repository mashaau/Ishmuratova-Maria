import math
import matplotlib
import matplotlib.pylab as p
import numpy as np
import random


be_x = [random.randint(0, 50) for i in range(5)]
be_y = [random.randint(0, 50) for i in range(5)]
s = []
for i in range(5):
    for _ in range(10):
        s.append((be_x[i] + random.randint(-10, 10), be_y[i] + random.randint(-10, 10)))
a = []
for i in range(5):
    a_x = 0
    a_y = 0
    for j in range(10):
        a_x += s[i* 10 + j][0]
        a_y += s[i* 10 + j][1]
    a.append((a_x/10, a_y/10))
x1 = [s[i][0] for i in range(10)]
y1 = [s[i][1] for i in range(10)]
x2 = [s[i][0] for i in range(10, 20)]
y2 = [s[i][1] for i in range(10, 20)]
x3 = [s[i][0] for i in range(20, 30)]
y3 = [s[i][1] for i in range(20, 30)]
x4 = [s[i][0] for i in range(30, 40)]
y4 = [s[i][1] for i in range(30, 40)]
x5 = [s[i][0] for i in range(40, 50)]
y5 = [s[i][1] for i in range(40, 50)]
x_a = [a[i][0] for i in range(len(a))]
y_a = [a[i][1] for i in range(len(a))]
p.scatter(x1, y1, color='black', marker="s")
p.scatter(x2, y2, color='orange', marker="s")
p.scatter(x3, y3, color='blue', marker="s")
p.scatter(x4, y4, color='yellow', marker="s")
p.scatter(x5, y5, color='red', marker="s")
p.scatter(x_a, y_a, color='pink', marker=11)
p.errorbar(x_a, y_a, yerr=3, xerr=3,  fmt='o-', ecolor='pink')
p.show()
