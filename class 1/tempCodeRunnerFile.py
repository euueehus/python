print("公式1")
a1 = int(input("請輸入第一個橡樹"))
an = int(input("請輸入第n個橡樹"))
n = int(input("多少項"))
if n <= 0:
    print("請重新輸入")
else:
    x = (a1 + an) * n / 2
    print("總共的數量為")
    print(x)
