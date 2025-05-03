import pandas as pd
import matplotlib.pyplot as plt
import imageio
import os


def load_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    frames = []
    for i in range(0, len(lines), 2):
        if i + 1 >= len(lines):
            break
        x_values = list(map(float, lines[i].strip().split()))
        y_values = list(map(float, lines[i + 1].strip().split()))
        frames.append((x_values, y_values))

    return frames

def babadzaki(frames):

    all_x = [x for frame in frames for x in frame[0]]
    all_y = [y for frame in frames for y in frame[1]]

    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)

    return x_min, x_max, y_min, y_max
    


def plot_data(frames, x_min, x_max, y_min, y_max):

    image_files = []
    for idx, (x, y) in enumerate(frames):
        file_name = f"frame_{idx + 1}.png"
        image_files.append(file_name)

        plt.figure(figsize=(8, 5))
        plt.plot(x, y, marker='o', linestyle='-', color='b')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'Frame {idx + 1}')
        plt.grid()


        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)

        plt.savefig(file_name)
        plt.close()

    return image_files


def create_gif(image_files, output_file="график.gif", duration=1.0):
    images = [imageio.imread(file) for file in image_files]
    imageio.mimsave(output_file, images, duration=duration)


# основная часть
file_path_2 = 'C:/Users/nakov/OneDrive/Рабочий стол/UNO/lab_1/2.dat'
frames = load_data(file_path_2)
x_min, x_max, y_min, y_max = babadzaki(frames)
image_files = plot_data(frames, x_min, x_max, y_min, y_max)
create_gif(image_files)
