"""
o = int(input("$"))

while o != 0:
    print(f" 目前$={o}")
    o += int(input("$"))
    break


"""
"""
import time

e = int(input("s"))
for O in range(e,0,-1):
    print(O)
    time.sleep(1)
else:
    print("到了")
"""


while True:
    print("1.app 2. O 3. n 4 . close")
    O = input("n")
    O = int(O)
    if O == "1":
        print("app")
    elif O == "2":
        print("O")
    elif O == "3":
        print("n")
    elif O == "4":
        print("close")
        break
    else:
        print(
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        )

"""
O = int(input("eeeeeeeeee"))

for e in range(O):
    if e % 10 == 0:
        continue
    print(e)
"""
