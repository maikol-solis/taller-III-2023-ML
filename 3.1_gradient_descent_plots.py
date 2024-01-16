# Gradient Descent
# gcorazzari

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from typing import Callable

def update(frame):
    x = x_gd[:frame]
    y = y_gd[:frame]
    line_gd.set_xdata(x)
    line_gd.set_ydata(y)
    return (line_gd)

def gradient_descent(start: float, gradient: Callable[[float], float],
                     learn_rate: float, max_iter: int, tol: float = 0.01):
    x = start
    steps = [start]  # history tracking

    for _ in range(max_iter):
        diff = learn_rate*gradient(x)
        if np.abs(diff) < tol:
            break
        x = x - diff
        steps.append(x)  # history tracing
  
    return steps, x

#EJ1-4
def f_ej1(x:float):
  return x**4-2*x**3+2

def dfdx_ej1(x:float):
  return 4*x**3-6*x**2

start = -0.5
gradient = dfdx_ej1
learn_rate = 0.3
max_iter = 100

res_ej1 = gradient_descent(start, gradient, learn_rate, max_iter)

fig, ax = plt.subplots()

x = np.linspace(-0.8, 2.2, 100)
y = f_ej1(x)

line = ax.plot(x, y)

x_gd = np.array(res_ej1[0])
y_gd = f_ej1(x_gd)

line_gd = ax.plot(res_ej1[0][0], f_ej1(res_ej1[0][0]), 'ro-', linewidth=0.5, markersize=2)[0]

ani = animation.FuncAnimation(fig=fig, func=update, frames=102, interval=200)

plt.grid(True)
plt.title('Inicio=-0.5, alpha=0.3')

writer = animation.PillowWriter(fps=5)

plt.show()
ani.save('ej1-4.gif', writer=writer)

#EJ1-3
def f_ej1(x:float):
  return x**4-2*x**3+2

def dfdx_ej1(x:float):
  return 4*x**3-6*x**2

start = -0.5
gradient = dfdx_ej1
learn_rate = 0.1
max_iter = 100

res_ej1 = gradient_descent(start, gradient, learn_rate, max_iter)

fig, ax = plt.subplots()

x = np.linspace(-0.8, 2.2, 100)
y = f_ej1(x)

line = ax.plot(x, y)

x_gd = np.array(res_ej1[0])
y_gd = f_ej1(x_gd)

line_gd = ax.plot(res_ej1[0][0], f_ej1(res_ej1[0][0]), 'ro-', linewidth=0.5, markersize=2)[0]

ani = animation.FuncAnimation(fig=fig, func=update, frames=9, interval=500)

plt.grid(True)
plt.title('Inicio=-0.5, alpha=0.1')

writer = animation.PillowWriter(fps=5)

plt.show()
ani.save('ej1-3.gif', writer=writer)

#EJ1-2
def f_ej1(x:float):
  return x**4-2*x**3+2

def dfdx_ej1(x:float):
  return 4*x**3-6*x**2

start = 2
gradient = dfdx_ej1
learn_rate = 0.3
max_iter = 100

res_ej1 = gradient_descent(start, gradient, learn_rate, max_iter)

fig, ax = plt.subplots()

x = np.linspace(-0.8, 2.2, 100)
y = f_ej1(x)

line = ax.plot(x, y)

x_gd = np.array(res_ej1[0])
y_gd = f_ej1(x_gd)

line_gd = ax.plot(res_ej1[0][0], f_ej1(res_ej1[0][0]), 'ro-', linewidth=0.5, markersize=2)[0]

ani = animation.FuncAnimation(fig=fig, func=update, frames=4, interval=200)

plt.grid(True)
plt.title('Inicio=2, alpha=0.3')

writer = animation.PillowWriter(fps=5)

plt.show()
ani.save('ej1-2.gif', writer=writer)


#EJ1-1
def f_ej1(x:float):
  return x**4-2*x**3+2

def dfdx_ej1(x:float):
  return 4*x**3-6*x**2

start = 2
gradient = dfdx_ej1
learn_rate = 0.1
max_iter = 100

res_ej1 = gradient_descent(start, gradient, learn_rate, max_iter)

fig, ax = plt.subplots()

x = np.linspace(-0.8, 2.2, 100)
y = f_ej1(x)

line = ax.plot(x, y)

x_gd = np.array(res_ej1[0])
y_gd = f_ej1(x_gd)

line_gd = ax.plot(res_ej1[0][0], f_ej1(res_ej1[0][0]), 'ro-', linewidth=0.5, markersize=2)[0]

ani = animation.FuncAnimation(fig=fig, func=update, frames=6, interval=500)

plt.grid(True)
plt.title('Inicio=2, alpha=0.1')

writer = animation.PillowWriter(fps=5)

plt.show()
ani.save('ej1-1.gif', writer=writer)