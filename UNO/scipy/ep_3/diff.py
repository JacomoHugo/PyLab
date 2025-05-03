import numpy as np
import sympy as sp
import scipy.integrate as spi
import matplotlib.pyplot as plt


t = sp.Symbol('t')
y = sp.Function('y')(t)
deq = sp.Eq(y.diff(t), -2*y)
sol_sympy = sp.dsolve(deq, y, ics={y.subs(t, 0): sp.sqrt(2)})
sol_sympy_func = sp.lambdify(t, sol_sympy.rhs, 'numpy')


def ode_func(t, y):
    return [-2 * y]

t_vals = np.linspace(0, 10, 100)
y0 = [np.sqrt(2)]
sol_scipy = spi.solve_ivp(ode_func, [0, 10], y0, t_eval=t_vals, method='RK45')
y_scipy = sol_scipy.y[0]


print("Решение SymPy:", sol_sympy)


plt.figure(figsize=(10, 5))
plt.plot(t_vals, sol_sympy_func(t_vals), label='SymPy Solution', linestyle='--', color='blue')
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(10, 5))
plt.plot(t_vals, y_scipy, label='SciPy Solution', linestyle='-', color='red')
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(10, 5))
plt.plot(t_vals, sol_sympy_func(t_vals) - y_scipy, label='Разница SymPy - SciPy', color='green')
plt.legend()
plt.grid()
plt.show()
