# .split=分割
# .join=接
# p = "2023/10/20"
# p = p.split("/")
# print(p)
# p = "-".join(p)
# print(p)
# append(數字)=家東西到list最後
# insert=插入:3

import random

order_list = []
while True:
    juices_list = [
        "新餐",
        "移除",
        "+餐",
        "算數",
        "取消最後一項",
        "取消特定",
        "顯示小到大",
        "顯示大to小",
        "反轉",
        "查餐為",
        "退出",
    ]
    for i in range(len(juices_list)):
        print(str(i + 1) + ". " + juices_list[i])
    try:
        ans = int(input("請輸入編號:"))
    except:
        print("輸入錯誤查無此功能，請重新輸入")

    if ans == 1:
        a = input("餐點名")
        order_list.append(a)
    elif ans == 2:
        o = input("打字")
        if o in order_list:
            order_list.remove(o)
            print("已移除")
        else:
            print("沒有")

    elif ans == 3:
        l = int(input("位子"))
        m = input("餐")
        order_list.insert(l, m)
    elif ans == 4:
        ssss = input("?????????????")
        print(order_list.count(ssss))
    elif ans == 5:
        order_list.pop()
    elif ans == 6:
        pp = int(input("jklbnhhjkjklhjjjkjjkhjkhjkhj"))
        order_list.pop(pp)
    elif ans == 7:
        order_list.sort()
        print(order_list)
    elif ans == 8:
        order_list.sort(reverse=True)
        print(order_list)
    elif ans == len(juices_list):
        print("~~系統關閉~~")
        break
    elif ans > len(juices_list) or ans <= 0:
        print("輸入錯誤查無此功能，請重新輸入")
    print("目前的餐為" + str(order_list))
