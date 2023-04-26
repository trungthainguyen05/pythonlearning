import sys
import os
import pandas as pd
import csv


filename = os.path.dirname(sys.argv[0])
currentPath = os.path.abspath(filename)
excelFilePath = currentPath+'\linkgroup.xlsx'
csvFilePath = currentPath+'\data.csv'

# f1 = pd.read_excel(excelFilePath)
# print(f1)

# newLine = 'hello'

# with open(csvFilePath, newline='') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         print(row)

# with open(csvFilePath, newline='') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         print(row)

# with open(csvFilePath, newline='') as File:
#     reader = csv.DictReader(File)
#     for row in reader:
#         print(row)


# WRITE CSV FILE
input_dic = [
    {'Name': 'Arkansas1', 'Capital City': 'Little Rock1',
     'Largest City': 'Little Rock1', 'Population': '30115241'},
    {'Name': 'Arkansas2', 'Capital City': 'Little Rock2',
     'Largest City': 'Little Rock2', 'Population': '30115242'}
]

fields = ['Name', 'Capital City', 'Largest City', 'Population']

input = ["Arkansas2", "Little Rock2", "Little Rock2", "30115242"]

# with open(csvFilePath, 'a', newline='\n') as File:
#     writer = csv.writer(File)
#     writer.writerow(input)

with open(csvFilePath, 'a', newline='') as File:
    writer = csv.DictWriter(File, fields)
    writer.writerows(input_dic)


with open(csvFilePath, newline='') as File:
    reader = csv.DictReader(File)
    for row in reader:
        print(row)
