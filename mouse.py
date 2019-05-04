from pynput.mouse import Controller
import random
import time
import pyautogui

def controlMouse():
    while True:
        mouse = Controller()
        width, height = pyautogui.size()
        mouse.position = [random.randint(0, width), random.randint(0, height)]
        time.sleep(0.1)

controlMouse()
