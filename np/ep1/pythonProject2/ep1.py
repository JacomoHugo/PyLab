from PIL import Image
import numpy as np

def enhance_contrast_pil(file_path, new_file_path=None):
    # Считываем изображение с помощью PIL
    img = Image.open(file_path).convert('L')  # Градации серого/Преобразует изображение в градации серого (8 бит на пиксель)
    data = np.array(img)
    #Каждый пиксель после этого будет числом от 0 (чёрный) до 255 (белый).

    # Выводим диапазон яркости
    min_val = np.min(data)
    max_val = np.max(data)
    print(f"Минимальное значение: {min_val}, Максимальное значение: {max_val}")

    # Проверка, есть ли вообще контраст
    if max_val == min_val:
        print("Изображение однотонное. Невозможно растянуть контраст.")
        updated_data = data.copy()
    else:
        updated_data = ((data - min_val) * 255.0 / (max_val - min_val)).astype(np.uint8)

    # Сохраняем результат
    res_img = Image.fromarray(updated_data)
    if new_file_path:
        res_img.save(new_file_path)

    return res_img


input_path1 = r"C:\Users\nakov\OneDrive\Рабочий стол\ep1\pythonProject2\lunar_images\lunar01_raw.jpg"
output_path1 = r"C:\Users\nakov\OneDrive\Рабочий стол\ep1\output1.jpg"
result1 = enhance_contrast_pil(input_path1, output_path1)
result1.show()

input_path2 = r"C:\Users\nakov\OneDrive\Рабочий стол\ep1\pythonProject2\lunar_images\lunar02_raw.jpg"
output_path2 = r"C:\Users\nakov\OneDrive\Рабочий стол\ep1\output2.jpg"
result2 = enhance_contrast_pil(input_path2, output_path2)
result2.show()

input_path3 = r"C:\Users\nakov\OneDrive\Рабочий стол\ep1\pythonProject2\lunar_images\lunar03_raw.jpg"
output_path3 = r"C:\Users\nakov\OneDrive\Рабочий стол\ep1\output3.jpg"
result3 = enhance_contrast_pil(input_path3, output_path3)
result3.show()
