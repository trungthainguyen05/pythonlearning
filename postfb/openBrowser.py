import pandas as pd
import os
import sys
import utility


filename = os.path.dirname(sys.argv[0])
currentPath = os.path.abspath(filename)
excelFilePath = currentPath+'\linkgroup.xlsx'
csvFilePath = currentPath+'\data.csv'
linkFbData = currentPath+'\linkfbdata.csv'

link = '"C:\Program Files\Google\Chrome\Application\chrome.exe"'
# Open google chrome browser
os.startfile(link)
