import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30

# Определение корней
roots = np.roots([-12, 0, -18, 5, 10, -30])
print("Корни функции:", roots)

# Определение интервалов возрастания и убывания функции
increasing_intervals = []
decreasing_intervals = []
x_values = np.linspace(-10, 10, 1000)
for i in range(len(x_values)-1):
    if f(x_values[i+1]) > f(x_values[i]):
        increasing_intervals.append((x_values[i], x_values[i+1]))
    elif f(x_values[i+1]) < f(x_values[i]):
        decreasing_intervals.append((x_values[i], x_values[i+1]))

print("Интервалы возрастания функции:", increasing_intervals)
print("Интервалы убывания функции:", decreasing_intervals)

# Построение графика
plt.plot(x_values, f(x_values))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции f(x)")
plt.grid(True)
plt.show()

# Вычисление вершины
vertex_x = -10  # Начальное значение x
min_y = f(vertex_x)  # Начальное значение y
for x in x_values:
    if f(x) < min_y:
        vertex_x = x
        min_y = f(x)
vertex = (vertex_x, min_y)
print("Вершина функции:", vertex)

# Определение промежутков, на которых f > 0 и f < 0
positive_intervals = []
negative_intervals = []
for i in range(len(x_values)-1):
    if f(x_values[i]) > 0 and f(x_values[i+1]) > 0:
        positive_intervals.append((x_values[i], x_values[i+1]))
    elif f(x_values[i]) < 0 and f(x_values[i+1]) < 0:
        negative_intervals.append((x_values[i], x_values[i+1]))

print("Промежутки, на которых f > 0:", positive_intervals)
print("Промежутки, на которых f < 0:", negative_intervals)