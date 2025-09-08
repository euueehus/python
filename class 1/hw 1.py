goodmath = [
    "知道首項+末項+橡樹",
    "首相,橡樹,公差(總和)",
    "首相,橡樹,公差(不合)",
    "求首",
    "系統關閉",
]  # 如要改選只改這個就好
while True:
    for i in range(len(goodmath)):
        print(str(i + 1) + ". " + goodmath[i])
    try:
        ans = int(input("請輸入編號:"))
    except:
        print("輸入錯誤查無此攻勢，請重新輸入")
        continue
    if ans == len(goodmath):
        print("~~系統關閉~~")
        break
    elif ans > len(goodmath) or ans <= 0:
        print("輸入錯誤查無此咚咚，請重新輸入")
    elif ans == 4:
        an = int(input("請輸入第最後個數字"))
        d = int(input("請輸入公差"))
        n = int(input("多少項"))
        if n <= 0:
            print("請重新輸入")
            break
        else:
            x = an - (n - 1) * d
            print("第一是:" + str(x))
    elif ans == 3:
        a1 = int(input("請輸入第一個數字"))
        d = int(input("請輸入公差"))
        n = int(input("多少項"))
        if n <= 0:
            print("請重新輸入")
            break
        else:
            x = a1 + (n - 1) * d
            print("總和為" + str(x))
    elif ans == 2:
        a1 = int(input("請輸入第一個橡樹"))
        d = int(input("請輸入公差"))
        n = int(input("多少項"))
        if n <= 0:
            print("請重新輸入")

        else:
            x = n * (2 * a1 + (n - 1) * d) / 2
            print("總共的數量為")
            print(x)
            break
    elif ans == 1:
        a1 = int(input("請輸入第一個橡樹"))
        an = int(input("請輸入第n個橡樹"))
        n = int(input("多少項"))

        if n <= 0:
            print("請重新輸入")
        else:
            x = (a1 + an) * n / 2
            print("總共的數量為")
            print(x)
            break
