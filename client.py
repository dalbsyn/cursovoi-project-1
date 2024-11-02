from tkinter import *
from tkinter import ttk

main = Tk()
main.title("приложение")

select_file = Label(text="Выберите файл")
output = Label(text="Вывод работы")

select_file.grid(row=0,  column=0)
output.grid(row=0, column=1)

main.mainloop()
