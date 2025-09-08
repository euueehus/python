import pyautogui
import time
import random
import turtle
from 警告 import custom_alert

s = 0
ss = 0
folder_path = r"C:\Users\user\Desktop\py\pythoon...new\photo"
try:
    mode = int(pyautogui.prompt("要甚模式" "星星或是多邊形" "輸入1或2"))
except:
    custom_alert("是在測試嗎Ww", title="錯誤", folder_path=folder_path)
    exit()


def start():
    global ss
    ss = pyautogui.prompt("幾角星")
    try:
        ss = int(ss)

    except:
        custom_alert("????????", title="錯誤", folder_path=folder_path)
    if ss <= 4:
        custom_alert("????????", title="錯誤", folder_path=folder_path)
        exit()


def m():
    global s
    s = pyautogui.prompt("幾邊形")
    try:
        s = int(s)

    except:
        custom_alert("????????", title="錯誤", folder_path=folder_path)
        exit()
    if s <= 3:
        custom_alert("????????", title="錯誤", folder_path=folder_path)
        exit()


if mode == 1:
    start()
elif mode == 2:
    m()


def pen(s, l):
    for i in range(s):
        turtle.forward(l)
        turtle.right(360 / s)


def strdart(ss, ll):
    for i in range(ss):
        turtle.forward(ll)
        turtle.right(360 * (ss // 2) / ss)


# 老師我這邊小偷懶
# 因為如果s=0的話也不會執行
# 嘶~加一下好了
if ss != 0:
    strdart(ss, 100)
if s != 0:
    pen(s, 100)
