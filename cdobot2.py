
import ctypes
import pyautogui
import time
import pydirectinput as pydirectinput
import pytesseract
from PIL import ImageGrab
from functools import partial


ImageGrab.grab = partial(ImageGrab.grab, all_screens=True) #allows all monitors to be accessed
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe' #PATH of pytesseract



#Note :

print('Super Bot Executed!')


def main():
    flag = False
    while 1:
        time.sleep(1) #3 second buffer time
        #takes screenshot of where "space" should be every 3 seconds and overwrites image
        im = pyautogui.screenshot('C:\\Users\\ezulq\\Desktop\\Coding\\Python\\cod-bot\\jumplive.jpg', region=(955, 860, 90, 25))  # x,y,width,height SOLOS
        #im = pyautogui.screenshot('C:\\Users\\ezulq\\Desktop\\Coding\\Python\\cod-bot\\jumplive.jpg',region=(870, 860, 90, 25))  # x,y,width,height # this is for duos and upwards

        #takes screenshot of where "play again" should be
        im2 = pyautogui.screenshot('C:\\Users\\ezulq\\Desktop\\Coding\\Python\\cod-bot\\playagain.jpg', region=(1400, 700, 200, 50))  # x,y,width,height



        #prints the result of the space location
        result = pytesseract.image_to_string(im) #print the image to text (OCR)
        print('OCR of what is in the \'Space\' location : ', result)

        result2 = pytesseract.image_to_string(im2)  # print the image to text (OCR)
        print('OCR of what is in the \'Play again\' location : ', result2)


        #if we find space
        if 'SPACE' in result:
            flag = True
            print('Jumping out of plane.')
            ctypes.windll.user32.SetCursorPos(-300,670) # moves to click screen @any loc
            pyautogui.click()
            pyautogui.click()                           # click that loc
            pydirectinput.press('space')                # acitivate spacebar (jump out of plane)
            time.sleep(1)                               # wait a few seconds

                                     # click loc again
            time.sleep(2)
            ctypes.windll.user32.SetCursorPos(-1000, 700)
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            #pydirectinput.move(-300, 900)              # moves mouse to look str8 down
            pydirectinput.keyDown('w')                  # hold w to splatter
            print('Splattering...')
            time.sleep(10)                              # falling 10 seconds
            pydirectinput.keyUp('w')                    # release w
            print('Splattered.')

            #pydirectinput.keyUp('w')                  # hold w to splatter

        if 'Play' in result2:
            time.sleep(1)
            print('Taking SBMM Screenshot')
            im3 = pyautogui.screenshot('C:\\Users\\ezulq\\Desktop\\Coding\\Python\\cod-bot\\sbmm.jpg',
                                      region=(2480, 130,150, 65))  # x,y,width,height SOLOS

            result = pytesseract.image_to_string(im3)  # print the image to text (OCR)
            time.sleep(1)

            print('Here is the avg KD : ',result)
            print('Writing data to file')
            time.sleep(1)

            with open("C:\\Users\\ezulq\\Desktop\\data.txt", "a") as myfile:
                myfile.write(result + '\n')
            time.sleep(1)

            print('File written to data')
            time.sleep(1)


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


main()

