l = {}


def add():
    global l
    c = input("請輸入科目:")
    a = input("輸入該科目分數:")
    l[c] = a


def delete():
    global l
    b = input("你要移除甚麼:")

    if b in l:
        l.pop(b)
        print("已移除" + b)
    else:
        print("發生極大的錯誤，你腦袋有問題!")


def exit():
    print("已提交")
    if len(l) > 0:
        tot = sum([int(score) for score in l.values()])
        ave = tot / len(l)
        print("你的所有科目的平均是:" + ave)
    else:
        print("沒有科目成績可以顯示")


while True:
    print("目前的成績" + str(l))
    print("1,新增分")
    print("2,移除分")
    print("3,提交並且顯示成績")
    option = input("歡迎使用，請輸入你的選項(1~3):")

    if option == "1":
        add()
    elif option == "2":
        delete()
    elif option == "3":
        exit()
        break
    else:
        print("錯誤，我操你居然看不懂文字!")
        continue

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 變可擴充
l = {}
O = [add, delete, exit]


def add():
    global l
    c = input("請輸入科目:")
    a = input("輸入該科目分數:")
    l[c] = a


def delete():
    global l
    b = input("你要移除甚麼:")

    if b in l:
        l.pop(b)
        print("已移除" + b)
    else:
        print("發生極大的錯誤，你腦袋有問題!")


def exit():
    print("已提交")
    if len(l) > 0:
        tot = sum([int(score) for score in l.values()])
        ave = tot / len(l)
        print("你的所有科目的平均是:" + ave)
    else:
        print("沒有科目成績可以顯示")


while True:
    print("目前的成績" + str(l))
    print("1,新增分")
    print("2,移除分")
    print("3,提交並且顯示成績")
    option = input("歡迎使用，請輸入你的選項(1~3):")
    try:
        s = int(input("請輸入編號:"))
    except:
        print("幹幹幹幹幹幹")
        continue
    if s == len(O):
        print("~~系統關閉~~")
        break
    elif s > len(O) or s <= 0:
        print("輸入錯誤查無此果汁，請重新輸入")

        break
    else:
        O[s - 1]()
    continue
