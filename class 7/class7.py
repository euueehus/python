import random

"""
e = random.randint(1, 100)
while 1:
    n = int(input("ssss"))
    print(e)
    if n == e:
        print("eeeeeeeeee")
        break
    elif n > e:
        print("small")
    else:
        print("big")
       """
"""
L = [1,2,3]
print(L)
L = [1,2,3,'hello',"world"]
print(L)
L = [1,2,3,'hello',"world",[4,5,6]]
print(L)



l = [ "a","b","c","d","e","f","g","h","i","j" ]
print(l)
print(l[0])
print(l[2])

print(l[-1])
print(l[-3])
print(l[0:3])
print(l[3:6])
print(l[0:10:2])
print(l[::2])
print(len(l))
for i in range(len(l)):
    print(l[i])
    for i in l :
        print(i)
        
"""
"""
juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "可樂", "系統關閉"]如要改選只改這個就好
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
        """
while True:
    print("1. 蘋果汁")
    print("2. 柳橙汁")
    print("3. 葡萄汁")
    print("4. 系統關閉")
    ans = input("請輸入編號:")
    if ans == "1":
        print("您點的商品是蘋果汁")
    elif ans == "2":
        print("您點的商品是柳橙汁")
    elif ans == "3":
        print("您點的商品是葡萄汁")
    elif ans == "4":
        print("~~系統關閉~~")
        break
    else:
        print("輸入錯誤查無此果汁，請重新輸入")
