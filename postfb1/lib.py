import pyautogui as pag
import time
import pandas as pd
import os
import sys

# Declare variables
filename = os.path.dirname(sys.argv[0])
currentPath = os.path.abspath(filename)
excelFilePath = currentPath+'\linkgroup.xlsx'
csvFilePath = currentPath+'\data.csv'
linkFbData = currentPath+'\linkfbdata.csv'
linkGoogleChrome = '"C:\Program Files\Google\Chrome\Application\chrome.exe"'

# Autoclick function


class mouseControl:
    # Thuộc tính
    count = 0

    # hàm khởi tạo

    def __init__(self):
        mouseControl.count += 1
        print('Khởi tạo class mouseControl')

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
    os.startfile(pathLink)
