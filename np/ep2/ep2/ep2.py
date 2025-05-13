import numpy as np
import matplotlib.pyplot as plt

#будем использовать простое скользящее среднее с шагом 10:window_size;

def moving_average_filter(data, window_size=10):
    cumsum = np.cumsum(data)

    # Усреднённые значения для индексов >= window_size - 1
    trailing_avg = (cumsum[window_size - 1:] - np.concatenate(([0], cumsum[:-window_size]))) / window_size

    # Усреднённые значения для начальных точек [0, window_size-2]
    start_avgs = cumsum[:window_size - 1] / np.arange(1, window_size)

    # Объединяем
    return np.concatenate((start_avgs, trailing_avg))

# Список входных файлов
base_path = r"C:\Users\nakov\OneDrive\Рабочий стол\ep2"
signal_files = [
    "signal01.dat",
    "signal02.dat",
    "signal03.dat"
]

for filename in signal_files:
    input_path = fr"{base_path}\signals\{filename}"
    output_path = fr"{base_path}\filtered_{filename.replace('.dat', '.jpg')}"

    try:
        data = np.loadtxt(input_path)
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")
        continue

    filtered = moving_average_filter(data, window_size=10)

    # Построение графиков
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].plot(data)
    axes[0].set_title('Сырой сигнал')

    axes[1].plot(filtered)
    axes[1].set_title('После фильтра')

    plt.tight_layout()
    plt.savefig(output_path, format='jpg', dpi=300)
    plt.show()
    plt.close()
