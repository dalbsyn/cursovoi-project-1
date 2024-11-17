from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import psutil
import time
import threading
import gpustat
from faster_whisper import WhisperModel

# Инициализация функций.

def open_file():
    '''
    - принимаемые значения: никакие;
    - предназначение: получение пути файла и присвоение значения оного к тексту 
    элемента select_file_location;
    - используется: кнопка select_file_button.
    '''

    file_location = filedialog.askopenfilename()
    select_file_location["text"] = file_location
    print(file_location)

def fetch_specs():
    while True:
        gpu = gpustat.GPUStatCollection.new_query()
        ram_usage = psutil.virtual_memory()
        available_ram_label["text"] = "Доступно ОЗУ: " + str(100 - ram_usage.percent) + "%"
        available_vram_label["text"] = "Доступно видеопамяти:" + str(int((gpu.gpus[0].memory_used / gpu.gpus[0].memory_total) * 100)) + "%"
        time.sleep(1)

def sth():
    ram_thread = threading.Thread(target=fetch_specs)
    ram_thread.start()

def local_process(file_location):
    model = "large-v3"

    model = WhisperModel(model, device="cpu", compute_type="int8")

    segments, info = model.transcribe(file_location, beam_size=5)

    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    output_field.delete("1.0", END)

    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        output_field.insert("1.end", segment.text)

def local_process_sep_thread(file_location):
    local_process_thread = threading.Thread(target=local_process, args=(file_location,))
    local_process_thread.start()

def temp():
    for i in range(0, 20):
        output_field.insert("{0}.0".format(i), "aaaaa\n")
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
left_spec_frame = Frame(left_frame, borderwidth=2, relief="solid")
right_frame = Frame(borderwidth=2, relief="solid")

# Левая часть - текст
select_file = Label(left_frame, text="Выберите файл")
select_file_location = Label(left_frame, text="temp")
link_to_docs = Label(left_frame, text="a")
setup_process = Label(left_frame, text="Настройки обработки")
link_to_project = Label(left_frame, text="https://github.com/dalbsyn/cursovoi-project-1")

# Левая часть - кнопки 
begin_button = Button(left_frame, text="Начать", command=lambda: local_process_sep_thread(select_file_location["text"]))
stop_button = Button(left_frame, text="Остановить", command=temp)
select_file_button = Button(left_frame, text="Выберите файл", command=open_file)

# Левая часть - низ
languages_combobox = ttk.Combobox(left_frame, values=languages)
models_combobox = ttk.Combobox(left_frame, textvariable="abc", values=models)
process_location_combobox = ttk.Combobox(left_frame, values=process_location)

# Левая часть
state_label = Label(left_spec_frame, text="Состояние: OK")
available_ram_label = Label(left_spec_frame, text="Доступно ОЗУ: Нет доступа")
available_vram_label = Label(left_spec_frame, text="Доступно видеопамяти: Нет доступа")
sth()
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
select_file_location.grid(row=1, column=0, sticky="w")
select_file_button.grid(row=1, column=1, sticky="nsew")
setup_process.grid(row=2, columnspan=2, sticky="w")
languages_combobox.grid(row=3, column=0)
models_combobox.grid(row=3, column=1)
process_location_combobox.grid(row=4, columnspan=2, sticky="nsew")
left_spec_frame.grid(row=5, columnspan=2, sticky="nsew")
begin_button.grid(row=6, column=0, sticky="nsew")
stop_button.grid(row=6, column=1, sticky="nsew")
link_to_docs.grid(row=7, columnspan=2, sticky="w")
link_to_project.grid(row=8, columnspan=2, sticky="w")

state_label.grid(sticky="w")
available_ram_label.grid(sticky="w")
available_vram_label.grid(sticky="w")

# Правая часть.
output.grid(row=0, columnspan=2, sticky="w")
output_field.grid(row=1, columnspan=2)
processing_progressbar.grid(row=2, columnspan=2, sticky="nsew")
save_to_button.grid(row=3, column=0, sticky="nsew")
copy_to_button.grid(row=3, column=1, sticky="nsew")

# Окно.
main.mainloop()
