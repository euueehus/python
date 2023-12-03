"""
以下功能說明:
1. 新增餐點
    1.1 顯示餐點列表
    1.2 輸入餐點編號
    1.3 將餐點加入my_list
2. 移除餐點
    2.1 輸入想移除的餐點完整名稱
    2.2 將餐點從my_list移除
3. 提交菜單
    3.1 顯示my_list中的餐點及數量
    3.2 顯示"菜單已提交囉!"
"""
list = []
s = ["1", "2", "3"]
l = ["1新增餐點", "2移除餐點", "3提交菜單"]
while True:
    print(f"目前以點的餐:_{list}")
    print(l)
    try:
        A = int(input("自"))
        if A == 1:
            O = input("餐")
            list.append(O)
        elif A == 2:
            t = input("12312312312312312312312312312")
        if t in list:
            list.remove(t)
        elif A == 3:
            print(list)
            l = input("eadhjkafioahauikfjaklshfagfuiasfhj")
            print(list.count(l))
            print("已提交")
            break
    except:
        print("幹")
