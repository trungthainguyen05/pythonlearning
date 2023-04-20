from student import Student
sv = []

while True:
    print('''
    Choose the function
    0. Exit
    1. Show all student list
    2. Add a new student
    3. Delete a student
    4. Edit a student
    ...
    ''')

    select = input('Please choose the function that you want?')
    if select.isdigit():
        select = int(select)

        if select == 0:
            break
        elif select == 1:
            if len(sv) == 0:
                print('There is no student in the list')
            else:
                for i in sv:
                    i.show()
        elif select == 2:
            id = input('Input ID new student: ')
            name = input('Input name new Student:')
            sv.append(Student(id, name))
        elif select == 3:
            id = input('Please input student ID that you want to delete')
            for i in sv:
                if i.id == id:
                    sv.remove(i)
        elif select == 4:
            id = input('Please input student ID that you want to edit: ')
            for i in sv:
                if i.id == id:
                    i.set_name(
                        input('Input name student that you want to edit:'))

    else:
        print('Please input the correct function')
