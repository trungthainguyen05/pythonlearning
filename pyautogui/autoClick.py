import pyautogui as pag
import time

# tim toa do
# time.sleep(1)
# pos = pag.position()
# print(pos)
# x_search = 32
# y_search = 90
# pag.click(x_search, y_search)

# Tim theo đối tượng (hình)
# time.sleep(1)
# img = 'searchBtnVS.png'
# obj = pag.locateOnScreen(img)
# pag.click(obj)


# Auto click on tiktok
time.sleep(1)
# pos = pag.position()
# print(pos)

x_coccoc = 1110
y_coccoc = 1058
pos_coccoc = pag.position(x_coccoc, y_coccoc)
time.sleep(3)
# pag.click(x_coccoc,y_coccoc)

time.sleep(3)
x_like = 728
y_like = 507
pos_like = pag.position(x_like, y_like)
pag.click(pos_like)
# pag.doubleClick(x_like,y_like)

x_movedown = 1335
y_movedown = 553
pos_movedown = pag.position(x_movedown, y_movedown)
# pag.click(x_movedown,y_movedown)

for _ in range(3):
    pag.doubleClick(pos_like)
    time.sleep(3)
    pag.click(pos_movedown)
    time.sleep(3)


input('Please press to exit program ')
