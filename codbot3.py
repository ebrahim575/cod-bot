import ctypes
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pyautogui
import win32api, win32con, win32gui
import cv2
import math
import time
from PIL import ImageGrab
from functools import partial
import ctypes
import pyautogui
import time
import pydirectinput as pydirectinput
import pytesseract
from PIL import ImageGrab
from functools import partial


ImageGrab.grab = partial(ImageGrab.grab, all_screens=True) #allows all monitors to be accessed
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe' #PATH of pytesseract

detector = hub.load("https://tfhub.dev/tensorflow/centernet/resnet50v1_fpn_512x512/1")

#Note :

print('Super Bot Executed!')

def aimbot():
    # size_scale = 3
    counter = 0
#add a detect play again button
    while counter < 25:
        # Get rect of Window
        # hwnd = win32gui.FindWindow(None, 'Call of Duty :Modern Warfare')
        # #hwnd = win32gui.FindWindow("UnrealWindow", None) # Fortnite
        # rect = win32gui.GetWindowRect(hwnd)
        # region = rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]

        # Get image of screen
        region = 0, 0, 1920, 1080
        ori_img = np.array(pyautogui.screenshot('C:\\Users\\ezulq\\Desktop\\Coding\\Python\\cod-bot\\aimbottest.jpg', region=region))
        time.sleep(1)
        # ori_img = cv2.resize(ori_img, (ori_img.shape[1] // size_scale, ori_img.shape[0] // size_scale))
        image = np.expand_dims(ori_img, 0)
        img_w, img_h = image.shape[2], image.shape[1]

        # Detection
        result = detector(image)
        result = {key: value.numpy() for key, value in result.items()}
        boxes = result['detection_boxes'][0]
        scores = result['detection_scores'][0]
        classes = result['detection_classes'][0]

        # Check every detected object
        detected_boxes = []
        for i, box in enumerate(boxes):
            # Choose only person(class:1)
            if classes[i] == 1 and scores[i] >= 0.5:
                ymin, xmin, ymax, xmax = tuple(box)
                if ymin > 0.5 and ymax > 0.8:  # CS:Go
                    # if int(xmin * img_w * 3) < 450: # Fortnite
                    continue
                left, right, top, bottom = int(xmin * img_w), int(xmax * img_w), int(ymin * img_h), int(ymax * img_h)
                detected_boxes.append((left, right, top, bottom))
                # cv2.rectangle(ori_img, (left, top), (right, bottom), (255, 255, 0), 2)

        print("Detected:", len(detected_boxes))
        print('Time : ',counter)
        # Check Closest
        if len(detected_boxes) >= 1:
            min = 99999
            at = 0
            centers = []
            for i, box in enumerate(detected_boxes):
                x1, x2, y1, y2 = box
                c_x = ((x2 - x1) / 2) + x1
                c_y = ((y2 - y1) / 2) + y1
                centers.append((c_x, c_y))
                dist = math.sqrt(math.pow(img_w / 2 - c_x, 2) + math.pow(img_h / 2 - c_y, 2))
                if dist < min:
                    min = dist
                    at = i

            # Pixel difference between crosshair(center) and the closest object
            x = centers[at][0] - img_w / 2
            y = centers[at][1] - img_h / 2

            # y = centers[at][1] - img_h/2 - (detected_boxes[at][3] - detected_boxes[at][2]) * 0.45

            # Move mouse and shoot
            scale = 1.7
            x = int(x * scale)
            y = int(y * scale)
            ctypes.windll.user32.SetCursorPos(-300, 670)  # moves to click screen @any loc
            pyautogui.click()
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)

            time.sleep(0.05)
            pyautogui.click()

            #pyautogui.mouseDown(button='right')  # press the right button down
            #pyautogui.mouseDown(button='left')  # press the right button down
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)

        else:

            #pydirectinput.keyDown('w')                  # hold w to splatter
            pyautogui.mouseUp(button='left')  # press the right button down
            #pyautogui.mouseUp(button='right')  # press the right button down
            #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            # time.sleep(0.1)
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

            # ori_img = cv2.cvtColor(ori_img, cv2.COLOR_BGR2RGB)
            # cv2.imshow("ori_img", ori_img)
            # cv2.waitKey(1)

            time.sleep(0.1)
            counter+=1

def main():
    flag = False
    while 1:
        time.sleep(1) #3 second buffer time

        #takes screenshot of where "space" should be every 3 seconds and overwrites image
        im = pyautogui.screenshot('C:\\Users\\ezulq\\Desktop\\Coding\\Python\\cod-bot\\jumplive.jpg', region=(955, 860, 90, 25))  # x,y,width,height SOLOS
        #im = pyautogui.screenshot('C:\\Users\\ezulq\\Desktop\\Coding\\Python\\cod-bot\\jumplive.jpg',region=(870, 860, 90, 25))  # x,y,width,height # this is for duos and upwards

        #takes screenshot of where "play again" should be
        im2 = pyautogui.screenshot('C:\\Users\\ezulq\\Desktop\\Coding\\Python\\cod-bot\\playagain.jpg', region=(1400, 700, 200, 50))  # x,y,width,height

        #this takes gulag screenshot
        im3 = pyautogui.screenshot('C:\\Users\\ezulq\\Desktop\\Coding\\Python\\cod-bot\\gulag.jpg', region=(1650, 120, 180, 50))

        #prints the result of the space location
        result = pytesseract.image_to_string(im) #print the image to text (OCR)
        print('OCR of what is in the \'Space\' location : ', result)

        result2 = pytesseract.image_to_string(im2)  # print the image to text (OCR)
        print('OCR of what is in the \'Play again\' location : ', result2)

        result3 = pytesseract.image_to_string(im3)  # print the image to text (OCR)
        print('OCR of what is in the \'Gulag\' location : ', result3)

        #if we find space
        if 'SPACE' in result:
            flag = True
            print('Jumping out of plane.')
            ctypes.windll.user32.SetCursorPos(-300,670) # moves to click screen @any loc
            pyautogui.click()
            pyautogui.click()                           # click that loc
            pydirectinput.press('space')                # acitivate spacebar (jump out of plane)
            time.sleep(1)                               # wait a few seconds

            ctypes.windll.user32.SetCursorPos(-300,670) # moves to click screen @any loc
            pyautogui.click()                           # click loc again
            time.sleep(2)
            pydirectinput.move(-1000, 900)              # moves mouse to look str8 down
            pydirectinput.keyDown('w')                  # hold w to splatter
            print('Splattering...')
            time.sleep(10)                              # falling 10 seconds
            pydirectinput.keyUp('w')                    # release w
            print('Splattered.')

            #pydirectinput.keyUp('w')                  # hold w to splatter

        if 'Play' in result2:
            print('Clicking Play Again.')
            ctypes.windll.user32.SetCursorPos(-300, 665)  #
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            ctypes.windll.user32.SetCursorPos(-800, 430)
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            print('Next game started.')
        if flag and ('New' in result3):
            time.sleep(2)
            print('You are fighting in the gulag.')
            print('Activating aimbot...')
            pydirectinput.keyDown('w')                  # hold w to splatter
            time.sleep(1)
            pydirectinput.keyUp('w')                  # hold w to splatter
            aimbot()

            print('Aimbot deactivated.')
main()

