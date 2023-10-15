"""
1.	請問Python有哪五種形態:
答案:
2.	請問使用什麼function可以顯示出形態
答案:print(type(資料物件))
3.	請問 a = int('1'), a的形態是什麼
答案:整數
4.	請問 b = str(1), b的形態是什麼
答案:變字串
5.	請問 c = float(1), c的形態是什麼
答案:浮點數
6.	請問 d = bool(1), d的形態是什麼
答案:布林
7.	請列出Python加、減、乘、除表示符號
答案:1.+ 2. - 3.* 4. / % // 
8. 請問今天學了哪一些function(函式)?
答案:# max(數字)=抓最大的數

# print(type(資料物件))取得資料物件的型態

# print(int(數值))將輸入數值轉換為整數型態

# print(int(True))=1

# print(float(True))=1.0浮點數

# (bool(""))有東西=true

# str(字) 變字串

# a = input()
# print(type(a))
# print("你輸的字:" + a)
# 
# a = input() 括號中的字是提示字
# print(type(a)) input()輸入的字會變字串
# print("你輸的字:" + a)
9. 延續上題, 請嘗試描述每個function的功能各別是什麼?
答案:# max(數字)=抓最大的數

# print(type(資料物件))取得資料物件的型態

# print(int(數值))將輸入數值轉換為整數型態

# print(int(True))=1

# print(float(True))=1.0浮點數

# (bool(""))有東西=true

# str(字) 變字串

# a = input()
# print(type(a))
# print("你輸的字:" + a)
# 
# a = input() 括號中的字是提示字
# print(type(a)) input()輸入的字會變字串
# print("你輸的字:" + a)

"""


"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果

bmi = w/h**2

EX:
請輸入身高:1.7
請輸入體重:50
你的BMI為17.301038062283737
"""


while True:
    w = float(input("請輸入體重"))
    h = float(input("請輸入身高"))
    bmi = w / h**2
    print("你的bmi是:" + str(bmi))
