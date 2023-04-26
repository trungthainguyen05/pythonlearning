import pandas as pd
import os
import sys
import utility

BASE_LINK = 'https://www.facebook.com/groups/'

filename = os.path.dirname(sys.argv[0])
currentPath = os.path.abspath(filename)
excelFilePath = currentPath+'\linkgroup.xlsx'
csvFilePath = currentPath+'\data.csv'

excelFile = pd.read_excel(excelFilePath)

excelFile.to_csv(csvFilePath, index=None, header=True)

df = pd.DataFrame(pd.read_csv(csvFilePath))

idgroups = df['Group no.']

# print(df.loc[[0, 1]])


# Convert to base link
# link_groups = []
# for i in idgroups:
#     link_groups.append(BASE_LINK+i)
# print(link_groups)
