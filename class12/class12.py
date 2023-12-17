# 新增指令
# def hello(我可以放變數):
#   print("d"+str(變數))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 有輸入有傳回值得函數
# def my_min(a,b):
# if a>b :
# retun a
# else:
# retun b
# 外面
# x= my_min(1,2)
# print("my_min"+str(x))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 全域變數
#
#
#
# 區域變數
# def e (a,b)括號中是區域變數
# print(a)
# 變數前+gobal變全域
#
#
#
#
# import random
#
#
# def s(e):
#    """骰子指令,n=次數(整數)"""
#    l = []
#    for a in range(e):
#        l.append(random.randint(1, 6))
#    return l
#
#
# e = int(input("次數"))
# print(s(e))
#
# 當函式有預設值變化時,應將變數放在函示參數的最後
def fun(a, b, c=0, d=0):
    print("a=", a)
    print("b=", b)
    print("c=", c)
    print("d=", d)


fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4)
# 必須照順序
fun(a=4, b=4)
