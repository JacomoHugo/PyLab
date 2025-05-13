import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Шаг 1: Загрузка начального состояния
u0 = np.loadtxt(r"C:\Users\nakov\OneDrive\Рабочий стол\ep3\3.dat")
N = len(u0)
steps = 255

# Шаг 2: Построение матрицы A и T
I = np.eye(N)
A = I - np.roll(I, 1, axis=1)
T = I - 0.5 * A

# Шаг 3: Диагонализация T
eigvals, V = np.linalg.eig(T)
V_inv = np.linalg.inv(V)

#C = A @ B   Это матричное умножение
# Считаем проекцию начального вектора
u0_proj = V_inv @ u0  # shape (N,)

# Создаём степени собственных значений
powers = np.arange(steps + 1).reshape(-1, 1)      # shape (256, 1)
D_powers = eigvals.reshape(1, -1) ** powers       # shape (256, N)

# Применяем к начальному вектору и возвращаемся в исходное базисное пространство
intermediate = D_powers * u0_proj                 # shape (256, N)
U = intermediate @ V.T                            # shape (256, N)

# Шаг 4: Анимация
fig, ax = plt.subplots()
line, = ax.plot(U[0])
ax.set_ylim(np.min(U), np.max(U))

def update(frame):
    line.set_ydata(U[frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=steps + 1, interval=40)

# Сохранение анимации
output_path = r"C:\Users\nakov\OneDrive\Рабочий стол\ep3\evolution.gif"
ani.save(output_path, writer='pillow', fps=25)

plt.show()
