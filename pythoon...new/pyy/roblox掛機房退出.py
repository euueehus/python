import pyautogui
import time
import keyboard

click_interval = 0.01
x = int(pyautogui.prompt("次數"))
time.sleep(2)
while x != 0:
    pyautogui.click()
    x -= 1
