import ctypes
import pyautogui
import time
import pydirectinput as pydirectinput
import pytesseract
from PIL import ImageGrab
from functools import partial
import cv2
import numpy as np


ImageGrab.grab = partial(ImageGrab.grab, all_screens=True) #allows all monitors to be accessed
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe' #PATH of pytesseract

im3 = pyautogui.screenshot('C:\\Users\\ezulq\\Desktop\\Coding\\Python\\cod-bot\\sbmm.jpg',
                                      region=(2480, 130,150, 65))  # x,y,width,height SOLOS



result = pytesseract.image_to_string(im3)  # print the image to text (OCR)
print(result)
with open("C:\\Users\\ezulq\\Desktop\\data.txt", "a") as myfile:
    myfile.write(result + '\n')