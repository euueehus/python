import pyautogui
import time


x = int(pyautogui.prompt("多少次輸入記得複製"))
t = float(pyautogui.prompt("輸入間隔"))
time.sleep(1)
pyautogui.confirm("按下ok開始")


while x != 0:
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    x -= 1
