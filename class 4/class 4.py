"""
p = input("密碼")
if p == "1234":
    print("歡迎光鈴e")
elif p == "5678":
    print("hi")
else:
    print("XXXXXXXXXXXX")
"""
"""
while True:
    s = int(input("成績"))
    if s >= 90:
        print("a")
    elif s >= 80:
        print("b")
    elif s >= 70:
        print("c")
    elif s >= 60:
        print("d")
    else:
        print("e")
"""
"""''
while True:
    e = int(input("數字"))
    if e % 2 != 0:
        print("坤數")
    else:
        print("偶數")
        """ ""


# for i in range(3):
#   turtle.forward(100)
#   turtle.right(90)


# turtle.forward(100)
# turtle.done()
# turtle.stamp()蓋章

# turtle.penup()提筆

import turtle

turtle.speed(0)
turtle.color("blue")
turtle.shape("circle")
turtle.penup()
for i in range(200):
    turtle.stamp()
    turtle.right(18)
    turtle.forward(i)


turtle.done()
