import pyautogui
import time

time.sleep(5)
while 1:
    x = 1680 #default
    y = 1010

    pyautogui.moveTo(x, y)   # moves mouse to X of 100, Y of 200.
    pyautogui.click()  # click the mouse
    time.sleep(240)

