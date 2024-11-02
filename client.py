from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def open_file():
    select_file_button = filedialog.askopenfilename()
    return select_file_button

main = Tk()
main.title("приложение")
left_frame = Frame(borderwidth=4)
right_frame = Frame(borderwidth=4)
languages = ["ru", "kz", "us"]
models = ["small", "medium", "large"]

select_file = Label(left_frame, text="Выберите файл")
select_file_button = Button(left_frame, text="Выберите файл", command=open_file)
setup_process = Label(left_frame, text="Настройки обработки")

languages_var = Variable(value=languages)
languages_listbox = Listbox(left_frame, listvariable=languages_var)

models_var = Variable(value=models)
models_listbox = Listbox(left_frame, listvariable=models_var)

output = Label(right_frame, text="Вывод работы")
output_field = Text(right_frame)

left_frame.grid(row=0, column=0)
right_frame.grid(row=0, column=1)

select_file.grid(row=0,  columnspan=2)
select_file_button.grid(row=1, columnspan=2)
languages_listbox.grid(row=2, column=0)
models_listbox.grid(row=2, column=1)
output.grid(row=0, column=1)
output_field.grid(row=1, column=1)

main.mainloop()
