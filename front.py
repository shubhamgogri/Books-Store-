from tkinter import *
import Back

data = Back.Database()

print(data.select())


def add_entry():
    list.delete(1, END)
    data.insert(title.get(), author.get(), year.get(), isbn.get())
    list.insert(END, (title.get(), author.get(), year.get(), isbn.get()))


def clear_all_entries():
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    year_entry.delete(0, END)
    isbn_entry.delete(0, END)


def search_entry():
    list.delete(0, END)
    for row in data.search(title.get(), author.get(), year.get(), isbn.get()):
        list.insert(END, row)


def view_all():
    list.delete(0, END)
    for row in data.select():
        list.insert(END, row)


def get_selected_row(event):
    global selected_tuple
    index = list.curselection()[0]
    selected_tuple = list.get(index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_tuple[2])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_tuple[3])
    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected_tuple[4])


def delete_entry_command():
    data.delete(selected_tuple[0])


def update_entry_command():
    data.update(selected_tuple[0], title.get(),
                author.get(), year.get(), isbn.get())


window = Tk()

window.wm_title("Book Store")
l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

title = StringVar()
title_entry = Entry(window, textvariable=title)
title_entry.grid(row=0, column=1)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

author = StringVar()
author_entry = Entry(window, textvariable=author)
author_entry.grid(row=0, column=3)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

year = StringVar()
year_entry = Entry(window, textvariable=year)
year_entry.grid(row=1, column=1)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

isbn = StringVar()
isbn_entry = Entry(window, textvariable=isbn)
isbn_entry.grid(row=1, column=3)

list = Listbox(window, height=6, width=35)
list.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)

list.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text='View All', width=12, command=view_all)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Entry', width=12, command=search_entry)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=12, command=add_entry)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update', width=12, command=update_entry_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete', width=12, command=delete_entry_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Clear Entries', width=12, command=clear_all_entries)
b6.grid(row=7, column=3)

window.mainloop()
