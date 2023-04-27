import pandas as pd
import os
import sys
import utility

BASE_LINK = 'https://www.facebook.com/groups/'

filename = os.path.dirname(sys.argv[0])
currentPath = os.path.abspath(filename)
excelFilePath = currentPath+'\linkgroup.xlsx'
csvFilePath = currentPath+'\data.csv'
linkFbData = currentPath+'\linkfbdata.csv'


excelFile = pd.read_excel(excelFilePath)

excelFile.to_csv(csvFilePath, index=None, header=True)

df = pd.DataFrame(pd.read_csv(csvFilePath))

df['link'] = BASE_LINK + df['Group no.']
df.to_csv(linkFbData)

df_linkFb = pd.DataFrame(pd.read_csv(linkFbData))
