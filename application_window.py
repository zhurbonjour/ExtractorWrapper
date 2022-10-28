import re
from tkinter import *
from tkinter import ttk, filedialog
from file_handlers import (
    check_values_in_file,
    wrap_to_expression,
    get_expression_from_collection,
    add_expression_to_collection,
    get_wrapped_output_text
)
from tkinter import messagebox as mb


root = Tk()
root.title('Extract&Wrap')
root.geometry('600x400')
root.resizable(False, False)


# переменные
reg_exp_list = get_expression_from_collection(filename='regular.txt')
wrappers_list = get_expression_from_collection(filename='wrappers.txt')


def add_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get(1.0, END))


def insert_filepath_to_pathfield() -> None:
    filepath = filedialog.askopenfile().name
    pathfield.delete(0, END)
    pathfield.insert(index=0, string=filepath)


def get_wrapped_result():
    try:
        path = pathfield.get()
        if not path:
            mb.showerror('Path Error',
                         'Не указан путь к файлу'
                         )
        reg_exp = reg_expression.get()
        wrap_exp = wrapper_expression.get()
        values_list = check_values_in_file(filepath=path, reg_exp=reg_exp)
        if not values_list:
            mb.showerror('RegExp Error',
                         'По вашему регулярному выражению ничего не найдено'
                         )
        wrap_to_expression(values_list=values_list, expression=wrap_exp)
        output_text.insert(1.0, get_wrapped_output_text())
    except:
        mb.showerror('RegExp Error', 'Ошибочное регулярное выражение')


# верхний блок окна
frame_top = Frame(root, bg='blue')
frame_top.place(relx=0.007, rely=0.007, relheight=0.4, relwidth=0.986)

# Нижний блок окна с выводом данных и кнопками закрытия и копирования
# содержжимого блоков
frame_bottom = Frame(root, bg='green')
frame_bottom.place(relx=0.007, rely=0.407, relheight=0.586, relwidth=0.986)

# строка ввода пути к файлу
title = Label(frame_top, text='Выберите файл или вставьте путь к файлу:')
title.place(relx=0.01, rely=0.05)

pathfield = Entry(frame_top, width=65)
pathfield.place(relx=0.01, rely=0.2)

choose_file_button = Button(frame_top,
                            text='Choose file',
                            command=insert_filepath_to_pathfield
                            )
choose_file_button.place(relx=0.82, rely=0.1, width=95, height=40)

# строка ввода регулярки
reg_title = Label(frame_top, text='Введите регулярное выражение:')
reg_title.place(relx=0.01, rely=0.365)

reg_expression = ttk.Combobox(frame_top, width=65, values=reg_exp_list)
reg_expression.place(relx=0.01, rely=0.515)

reg_templates = Button(frame_top,
                       text='Add RegEx',
                       command=lambda: add_expression_to_collection(
                           'regular.txt',
                           reg_expression.get()
                       ))
reg_templates.place(relx=0.82, rely=0.41, width=95, height=40)

# строка ввода конструкции враппера
wrapper_title = Label(frame_top, text='Введите функцию обертки:')
wrapper_title.place(relx=0.01, rely=0.68)

wrapper_expression = ttk.Combobox(frame_top, width=65, values=wrappers_list)
wrapper_expression.place(relx=0.01, rely=0.83)

wrapper_templates = Button(frame_top,
                           text='Add Template',
                           command=lambda: add_expression_to_collection(
                               'wrappers.txt',
                               wrapper_expression.get()
                           ))
wrapper_templates.place(relx=0.82, rely=0.73, width=95, height=40)

# main functional buttons
convert_button = Button(frame_bottom,
                        text='Extract%Wrap',
                        anchor='center',
                        command=get_wrapped_result)
convert_button.place(relx=0.82, rely=0.1, width=95)

copy_button = Button(frame_bottom,
                     text='Copy',
                     anchor='center',
                     command=add_to_clipboard)
copy_button.place(relx=0.82, rely=0.4, width=95)

output_text = Text(frame_bottom, width=65, height=12)
scr = Scrollbar(frame_bottom, command=output_text.yview)
output_text.configure(yscrollcommand=scr.set)
output_text.place(relx=0.01, rely=0.01)
scr.place(relx=0.767, rely=0.78)


close_button = Button(frame_bottom,
                      text='Close',
                      anchor='center',
                      command=lambda: root.destroy()
                      )
close_button.place(relx=0.82, rely=0.7, width=95)


root.mainloop()
