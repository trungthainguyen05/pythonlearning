import pyautogui as pag
import time
import pandas as pd
import os
import sys
import utility

# Declare variables
filename = os.path.dirname(sys.argv[0])
currentPath = os.path.abspath(filename)
excelFilePath = currentPath+'\linkgroup.xlsx'
csvFilePath = currentPath+'\data.csv'
linkFbData = currentPath+'\linkfbdata.csv'
linkGoogleChrome = '"C:\Program Files\Google\Chrome\Application\chrome.exe"'

# Autoclick function


def oneClick(x, y, timeBefore=1, timeAfter=1):
    time.sleep(timeBefore)
    pag.click(x, y)
    time.sleep(timeAfter)


def doubleClick(x, y, timeBefore=1, timeAfter=1):
    time.sleep(timeBefore)
    pag.doubleClick(x, y)
    time.sleep(timeAfter)

# Open google chrome


def openGoogleChrome(pathLink):
    # Open google chrome browser
    os.startfile(link)
