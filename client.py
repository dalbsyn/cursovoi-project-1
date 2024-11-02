from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# Инициализация функций.

def open_file():
    '''
    - принимаемые значения: никакие;
    - предназначение: получение пути файла и присвоение значения оного к тексту 
    элемента select_file_location;
    - используется: кнопка select_file_button.
    '''

    file_location = filedialog.askopenfilename()
    select_file_location["text"]=file_location
    print(file_location)

'''
Инициализация приложения:
- главное окно: main;
- название окна;
- список поддерживаемых языков - надо бы из места получше стягивать, а не само-
стоятельно заполнять;
- список поддерживаемых моделей - тоже самое, что и с языками;
- список мест для обработки - приложение клиент-серверное.
'''
main = Tk()
main.title("приложение")
languages = ["ru", "kz", "us"]
models = ["small", "medium", "large"]
process_location = ["Локально", "Удаленно"]

'''
Оформление интерфейса.
Структура:
- левая часть - настройки, данные о программе;
- правая часть - состояние обработки, выходные данные.
'''

# Рамки
left_frame = Frame(borderwidth=2, relief="solid")
right_frame = Frame(borderwidth=2, relief="solid")

# Левая часть - текст
select_file = Label(left_frame, text="Выберите файл")
select_file_location = Label(left_frame, text="temp")
link_to_docs = Label(left_frame, text="a")
setup_process = Label(left_frame, text="Настройки обработки")
link_to_project = Label(left_frame, text="https://github.com/dalbsyn/cursovoi-project-1")

# Левая часть - кнопки 
begin_button = Button(left_frame, text="Начать")
select_file_button = Button(left_frame, text="Выберите файл", command=open_file)

# Левая часть - прочее
languages_combobox = ttk.Combobox(left_frame, values=languages)
models_combobox = ttk.Combobox(left_frame, textvariable="abc", values=models)
process_location_combobox = ttk.Combobox(left_frame, values=process_location)

# Правая часть - текст
output = Label(right_frame, text="Вывод работы")

# Правая часть - кнопки 
save_to_button = Button(right_frame, text="Сохранить в ...")
copy_to_button = Button(right_frame, text="Скопировать содержимое")

# Правая часть - прочее 
output_field = Text(right_frame)
processing_progressbar= ttk.Progressbar(right_frame, orient="horizontal")

'''
Вставка элементов интерфейса.
'''

# Рамки.
left_frame.grid(row=0, column=0, padx=2, pady=2)
right_frame.grid(row=0, column=1, padx=2, pady=2)

# Левая часть.
select_file.grid(row=0,  columnspan=2, sticky="w")
select_file_location.grid(row=1, column=0)
select_file_button.grid(row=1, column=1)
setup_process.grid(row=2, columnspan=2, sticky="w")
languages_combobox.grid(row=3, column=0)
models_combobox.grid(row=3, column=1)
process_location_combobox.grid(row=4, columnspan=2)
begin_button.grid(row=5, columnspan=2, sticky="w")
link_to_docs.grid(row=6, columnspan=2, sticky="w")
link_to_project.grid(row=7, columnspan=2, sticky="w")

# Правая часть.
output.grid(row=0, columnspan=2, sticky="w")
output_field.grid(row=1, columnspan=2)
processing_progressbar.grid(row=2, columnspan=2)
save_to_button.grid(row=3, column=0, sticky="w")
copy_to_button.grid(row=3, column=1, sticky="w")

# Окно.
main.mainloop()
