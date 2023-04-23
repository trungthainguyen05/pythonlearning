from tkinter import *
from database import *


def add():
    line = id.get()+'-'+name.get()+'-'+year.get()
    print('Check input line: ', line)
    save(line)
    show()


def show():
    sv = read()
    listbox.delete(0, END)
    for k in sv:
        listbox.insert(END, k)


def sort():
    sv = read()
    for i in range(len(sv)):
        for j in range(len(sv)):
            x, y = sv[i], sv[j]
            if x[2] > y[2]:
                sv[i], sv[j] = y, x
    listbox.delete(0, END)
    for i in sv:
        listbox.insert(END, i)


root = Tk()
# Declare variables
id = StringVar()
name = StringVar()
year = StringVar()

# Interface
root.title('Student Manage Program')
root.minsize(height=500, width=500)

lb0 = Label(root, text='STUDENT MANAGE PROGRAM',
            fg='red', font=('cambria', 16), width=25)
lb0.grid(row=0)

listbox = Listbox(root, width=80, height=20)
listbox.grid(row=1, columnspan=2)
show()

lb1 = Label(root, text='Student ID: ')
lb1.grid(row=2, column=0)
entry1 = Entry(root, width=40, textvariable=id)
entry1.grid(row=2, column=1)

lb2 = Label(root, text='Student name: ')
lb2.grid(row=3, column=0)
entry2 = Entry(root, width=40, textvariable=name)
entry2.grid(row=3, column=1)

lb3 = Label(root, text='Student birthday: ')
lb3.grid(row=4, column=0)
entry3 = Entry(root, width=40, textvariable=year)
entry3.grid(row=4, column=1)

button = Frame(root)
Button(button, text='Add', command=add).pack(side=LEFT)
Button(button, text='Show', command=show).pack(side=LEFT)
Button(button, text='Sort', command=sort).pack(side=LEFT)
Button(button, text='Close', command=root.quit).pack(side=LEFT)
button.grid(row=5, column=1)


root.mainloop()
