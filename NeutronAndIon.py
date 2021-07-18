import numpy as np
import matplotlib.pyplot as plt

m = 9.59 * (10 ** (-27))
gamma = 1.005
mu = 1.25 * 10 ** (-6)
q = 147 * 10 ** (-19)
vx = 2.99 * (10 ** 20)
vy = 0
a = 0.1
e = 8.85 * 10 ** (-12)
Mn = 1.6 * 10**(-24)
dt = 10**(-26)
x = [-1]
y = [a]
for i in range(0, 700000):
    vx -= q*vy*m*gamma/((x[i]**2 + y[i]**2)**(3/2))
    vy += q* vx * m * gamma / ((x[i] ** 2 + y[i] ** 2) ** (3 / 2))
    x.append(x[i] + vx * dt)
    y.append(y[i] + vy * dt)
plt.plot(x, y)
plt.show()
