import sys
import os

filename = os.path.dirname(sys.argv[0])
currentPath = os.path.abspath(filename)

fullCurrentPath = currentPath + '\QLSV.txt'
# 'F:\ProjectIT\py\\tkinterQLSV\QLSV.txt'
print('check path: ', fullCurrentPath)


def save(line):
    try:
        f = open(fullCurrentPath, 'a', encoding='utf8')
        f.writelines(line)
        f.writelines('\n')
        f.close()
    except:
        print('something wrong with save function')
        pass


def read():
    sv = []
    try:
        f = open(fullCurrentPath, 'r', encoding='utf8')
        for i in f:
            data = i.strip()
            arr = data.split('-')
            sv.append(arr)
        f.close()
        return sv
    except:
        print('something wrong with read function')
        pass
