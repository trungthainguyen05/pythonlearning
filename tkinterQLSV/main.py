from tkinter import *
root = Tk()
root.title('Student Manage Program')
root.minsize(height=500, width=500)
Label(root, text='STUDENT MANAGE PROGRAM',
      fg='red', font=('cambria', 16), width=25).grid(row=0)
Listbox(root, width=80, height=20).grid(row=1, columnspan=2)
Label(root, text='Student ID: ').grid(row=2, column=0)
Entry(root, width=40).grid(row=2, column=1)

Label(root, text='Student name: ').grid(row=3, column=0)
Entry(root, width=40).grid(row=3, column=1)

Label(root, text='Student birthday: ').grid(row=4, column=0)
Entry(root, width=40).grid(row=4, column=1)

button = Frame(root)
Button(button, text='Add').pack(side=LEFT)
Button(button, text='Show').pack(side=LEFT)
Button(button, text='Sort').pack(side=LEFT)
Button(button, text='Close', command=root.quit).pack(side=LEFT)
button.grid(row=5, column=1)


root.mainloop()
