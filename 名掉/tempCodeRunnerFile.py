juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "可樂", "系統關閉"]  # 如要改選只改這個就好
while True:
    for i in range(len(juices_list)):
        print(str(i + 1) + ". " + juices_list[i])
    try:
        ans = int(input("請輸入編號:"))
    except:
        print("輸入錯誤查無此果汁，請重新輸入")
        continue
    if ans == len(juices_list):
        print("~~系統關閉~~")
        break
    elif ans > len(juices_list) or ans <= 0:
        print("輸入錯誤查無此果汁，請重新輸入")
    else:
        print("您點的商品是" + juices_list[ans - 1])
