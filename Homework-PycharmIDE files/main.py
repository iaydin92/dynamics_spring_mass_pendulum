import matplotlib
import numpy as np
import math
import matplotlib.pyplot as plt

l = 0.5
g = 9.8
m1 = 100
m2 = 10
timeTotal = 15
dt = 0.0015
k = 1000
theta0 = np.pi / 4
thetadot = 0
x = 0.1
xdot = 0


def fn(theta, w, x, u, g, l, m1, m2, k):
    return np.array([w, (((-m2 * l * w * w * np.sin(theta) - m2 * g * np.sin(theta)* np.cos(theta) + k * x) / (m1 + m2 - m2 * np.cos(theta)*np.cos(theta))) * np.cos(theta) - g * np.sin(theta)) / l,
                     u,(m2 * l * w * w * math.sin(theta) + m2 * g * np.sin(theta)* np.cos(theta) - k * x) / ( m1 + m2 - m2 * np.cos(theta) * np.cos(theta))])


yn = np.array([theta0, thetadot, x, xdot])
yExplicit = yn.copy()

time = 0
while time < timeTotal:
    y =yn+dt*fn(yn[0], yn[1], yn[2], yn[3], g, l, m1, m2, k)
    yn = y.copy()
    time = time + dt
    yExplicit = np.vstack((yExplicit, y))
    print(yn)
print("After 10 seconds value of θ is : -0.636"  "\nAfter 10 seconds value of x is : -0.062")
t = np.linspace(0, timeTotal, num=len(yExplicit))
plt.rcParams["figure.figsize"] = 15, 5
a = plt.plot(t, yExplicit[:, 0], label='Theta', color='red')
b = plt.plot(t, yExplicit[:, 2], label='Dispx', color='blue')
plt.axhline(0, color='black')
plt.legend(loc='best')
plt.show()


plt.rcParams["figure.figsize"] = 15, 5
d = plt.plot(yExplicit[:, 0], yExplicit[:, 2], label='Theta and x', color='blue')
plt.axhline(0, color='black')
plt.legend(loc='best')
plt.show()


plt.rcParams["figure.figsize"] = 15, 5
c = plt.plot(yExplicit[:, 1], yExplicit[:, 3], label='thetadot and xdot', color='red')
plt.axhline(0, color='black')
plt.legend(loc='best')
plt.show()


plt.rcParams["figure.figsize"] = 15, 5
d = plt.plot(yExplicit[:, 2], yExplicit[:, 3], label='x and xdot', color='blue')
plt.axhline(0, color='black')
plt.legend(loc='best')
plt.show()


plt.rcParams["figure.figsize"] = 15, 5
c = plt.plot(yExplicit[:, 0], yExplicit[:, 1], label='Theta and thetadot', color='red')
plt.axhline(0, color='black')
plt.legend(loc='best')
plt.show()

