import numpy as np
import matplotlib.pyplot as plt


with open("C:/Users/nakov/OneDrive/Рабочий стол/UNO/lab_3/2_large.txt", 'r') as f:
    lines = f.readlines()


N = int(lines[0].strip())


A = np.array([list(map(float, line.split())) for line in lines[1:N+1]])
b = np.array(list(map(float, lines[N+1].split())))


x = np.linalg.solve(A, b)


plt.figure(figsize=(8, 6))
plt.bar(range(1, N+1), x)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
