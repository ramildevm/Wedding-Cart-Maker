import sys
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import tkinter as tk

# Функция для вставки текста в середину изображения
def insert_text(image_path, text, line_spacing, y):
    # Загрузка изображения
    image = Image.open(image_path)

    # Создание объекта ImageDraw для рисования на изображении
    draw = ImageDraw.Draw(image)

    # Определение размеров изображения
    width, height = image.size

    # Загрузка пользовательского шрифта# Укажите путь к вашему шрифту и размер шрифта
    #font_path = 'D:/Diploma Script Basic RUS.otf'  # Укажите путь к вашему шрифту
    #font_bold_path = 'D:/Diploma Script Bold RUS.otf'  # Укажите путь к вашему полужирному шрифту
    font_bold_path = os.path.join(sys._MEIPASS, 'Diploma Script Bold RUS.otf')
    #set_font_bold(font_path, font_bold_path) 
    # Определение размеров текста
    font = ImageFont.truetype(font_bold_path, 80)  

    text_width, text_height = draw.textsize(text, font=font)

    # Определение координат для вставки текста в середину изображения
    x = ((width - text_width) // 2) +(text_width//2)
    # Расположение текста по середине сверху

    # # Рисование текста на изображении
    # draw.multiline_text((x, y), text, font=font, fill='#3c3e67', anchor="mm")  # Здесь fill определяет цвет текста, anchor="mm" центрирует текстовый блок

    # # Преобразование изображения в массив numpy
    # image_array = np.array(image)
    lines = text.split('\n')
    num_lines = len(lines)
    line_height = text_height // num_lines

    # Расчет вертикальной координаты начала каждой строки
    y_start = y - ((num_lines - 1) * (line_height + line_spacing)) // 2

    # Рисование текста на изображении с учетом line_spacing
    # Рисование текста на изображении с учетом line_spacing и обводки
    outline_color = '#3c3e67'
    outline_width = 1
    for line in lines:
        line_width, _ = draw.textsize(line, font=font)
        x_line = x - line_width // 2

        # Рисование обводки вокруг текста
        for outline in range(1, outline_width + 1):
            draw.text((x_line - outline, y_start), line, font=font, fill=outline_color)  # Левая граница
            draw.text((x_line + outline, y_start), line, font=font, fill=outline_color)  # Правая граница
            draw.text((x_line, y_start - outline), line, font=font, fill=outline_color)  # Верхняя граница
            draw.text((x_line, y_start + outline), line, font=font, fill=outline_color)  # Нижняя граница

        # Рисование текста
        draw.text((x_line, y_start), line, font=font, fill='#3c3e67')
        y_start += line_height + line_spacing

    # Преобразование изображения в массив numpy
    image_array = np.array(image)

    # Возврат массива изображения
    return image_array


def execute_action():
    # Пример использования
    string1 = entry1.get()
    string2 = entry2.get()
    string3 = entry2_1.get()
    path = entry3.get()

    #image_path = 'D:/wedding.png'
    image_path = os.path.join(sys._MEIPASS, 'wedding.png')  # Укажите путь к вашему изображению
     
    y = 85
    text = string1
    if len(string2)>0:
        y = 60
        text +=("\n" + string2)
    if len(string3)>0:
        #image_path = 'D:/wedding_2.png'
        image_path = os.path.join(sys._MEIPASS, 'wedding_2.png')
        y = 90
        text +=("\n" + string3)

    # Вставка текста в изображение
    result_image = insert_text(image_path, text, 10, y)

    # Сохранение результата
    result_image = Image.fromarray(result_image)
    if not os.path.exists(path):
        os.makedirs(path)
    result_image.save(path+ '/приглашение'+string1.replace('!','').replace(' ','_').replace(',','')+string2.replace('!','').replace(',','').replace(' ','_')+'.png')
    result_image.show()
    if var.get() == 1:
        entry1.delete(0, tk.END)
        entry1.insert(0,"Дорогие ")
        entry2.delete(0, tk.END)
        entry2_1.delete(0, tk.END)



window = tk.Tk()
# Set the padding for objects in the window
window.configure(padx=40, pady=40)
custom_font = ('Arial', 16) 
custom2_font = ('Arial', 14) 
custom_label_font = ('Arial', 12) 
button_font = ('Arial', 16, ) 
# Create the labels and entry fields
label1 = tk.Label(window, text="Строка 1:", font=custom_label_font)
label1.pack()
entry1 = tk.Entry(window, width="40", font=custom_font)
entry1.insert(0,"Дорогие ")
entry1.pack(padx=10, pady=10)

label2 = tk.Label(window, text="Строка 2:", font=custom_label_font)
label2.pack()
entry2 = tk.Entry(window, width="40", font=custom_font)
entry2.pack(padx=10, pady=10)

label2_1 = tk.Label(window, text="Строка 3:", font=custom_label_font)
label2_1.pack()
entry2_1 = tk.Entry(window, width="40", font=custom_font)
entry2_1.pack(padx=10, pady=10)

label3 = tk.Label(window, text="Путь для сохранения:", font=custom_label_font)
label3.pack()
entry3 = tk.Entry(window, width="40", font=custom2_font)
entry3.insert(0,"C:/Пригласительные")
entry3.pack(padx=10, pady=10)

var = tk.IntVar()

# Create the checkbox
checkbox = tk.Checkbutton(window, text="очищать поля", variable=var)
checkbox.pack()
# Create the "Выполнить" button
button = tk.Button(window, text="Выполнить", command=execute_action, width=30, font=button_font, background='#3c3e67', foreground='white')
button.pack(padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()