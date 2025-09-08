import pyautogui
import keyboard
import time

click_interval = 0.0001
time.sleep(5)
while True:
    pyautogui.press("space")
    time.sleep(30)
    if keyboard.is_pressed("a"):
        break
