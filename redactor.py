import tkinter as tk
from tkinter import filedialog
help_window_flag = False
root=tk.Tk()
root.title("Блокнот")
root.geometry("600x600+500+300")
root.minsize(200,100)
root.maxsize(1920,1080)
def exit_func():
    root.destroy()
def new_text():
    text.delete('1.0',tk.END)
def close_asksave():
    root_asksave.destroy()
def file_new():
    text_save=str(text.get(1.0,tk.END))
    if text_save!="\n":
        root_asksave=tk.Tk()
        root_asksave.geometry("300x100+500+450")
        root_asksave.resizable(False,False)
        root_asksave.title("Сохранить документ")
        def new_text():
            text.delete('1.0',tk.END)
            root_asksave.destroy()
        def close_asksave():
            root_asksave.destroy()
        def new_save():
            root_asksave.destroy()
            file_save()
            text.delete("1.0",tk.END)
        save_label=tk.Label(root_asksave,
                            text="Сохранить файл?")
        save_label.pack()
        yes_button=tk.Button(root_asksave,text="Да",
                              command=file_save)
        yes_button.pack()
        no_button=tk.Button(root_asksave,text="Нет",
                              command=new_text)
        no_button.pack()
        back_button=tk.Button(root_asksave,text="Отмена",
                              command=close_asksave)
        back_button.pack()
def help_window():
    global help_window_flag
    if help_window_flag == False:
        root_help=tk.Tk()
        root_help.geometry("300x70+500+450")
        root_help.resizable(False,False)
        root_help.title("Помощь")
        help_label=tk.Label(root_help,
                            text="Ссылка для инструкции\nhttp://python.com")
        help_label.pack()
        help_window_flag = True
        def close_root_help():
            root_help.destroy()
            global help_window_flag
            help_window_flag = False
        help_button=tk.Button(root_help,text="Закрыть",
                              command=close_root_help)
        help_button.pack()
def file_save():
    file_name=filedialog.asksaveasfilename(initialdir="/",
                                           title="Сохранить как",
                                           filetypes=(("Текстовые документы","*.txt"),("Все файлы","*.*")))
    if file_name:
        with open(file_name+".txt","w") as f:
            text_save=str(text.get(1.0,tk.END))
            f.write(text_save)
def file_open():
    file_name=filedialog.askopenfilename(initialdir="/",
                                           title="Открыть файл",
                                           filetypes=(("Текстовые документы","*.txt"),("Все файлы","*.*")))
    if file_name:
        with open(file_name,"r") as f:
            text_open=f.read()
            text.insert(1.0,text_open)
main_menu=tk.Menu(root)
root.config(menu=main_menu)

file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label="New",command=file_new)
file_menu.add_command(label="Open",command=file_open)
file_menu.add_command(label="Save as",command=file_save)
file_menu.add_command(label="Exit",command=exit_func)
main_menu.add_cascade(label="File",menu=file_menu)

help_menu=tk.Menu(main_menu,tearoff=0)
help_menu.add_command(label="Help",command=help_window)
help_menu.add_command(label="About")
main_menu.add_cascade(label="Help",menu=help_menu)

text=tk.Text(root)
text.pack(expand=tk.YES,fill=tk.BOTH)

root.mainloop()