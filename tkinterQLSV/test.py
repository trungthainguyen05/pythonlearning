path="F:\ProjectIT\py\\tkinterQLSV\QLSV.txt"

def save(text):
    f=open(path,'a',encoding='utf8')
    f.writelines(text)
    f.writelines('\n')
    f.close()

a='test-write-file-a'
b='test-b'
save(a+b)

def read():
    sv=[]
    f=open(path,'r',encoding='utf8')
    for i in f:
        data=i.strip()
        arr=data.split('-')
        sv.append(arr)
    return sv

print(read())

while True:
    print('''
    1. Exit program
    2. Add info
    ''')
    select=input('Please input your selection: ')
    if select.isdigit:
        select=int(select)
        if select ==0:
            break
        elif select ==1:
            pass
    else:
        pass
    
    if select ==0:
        break
    elif select==1:
        pass
    