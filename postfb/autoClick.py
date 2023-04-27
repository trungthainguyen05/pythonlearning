import pyautogui as pag
import time


# Autoclick function
def oneClick(x, y, timeBefore=1, timeAfter=1):
    time.sleep(timeBefore)
    pag.click(x, y)
    time.sleep(timeAfter)


def doubleClick(x, y, timeBefore=1, timeAfter=1):
    time.sleep(timeBefore)
    pag.doubleClick(x, y)
    time.sleep(timeAfter)
