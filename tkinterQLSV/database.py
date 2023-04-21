path='F:\ProjectIT\py\\tkinterQLSV\QLSV.txt'
def save(line):
    try:
        f=open(path,'w',encoding='utf8')
        f.writelines(line)
        f.writelines('\n')
        f.close()
    except:
        print('something wrong with save function')
        pass

def read():
    sv=[]
    try:
        f=open(path,'r',encoding='utf8')
        for i in f:
            data=i.strip()
            arr = data.split('-')
            sv.append(arr)
        f.close()
        return sv
    except:
        print('something wrong with read function')
        pass
    

