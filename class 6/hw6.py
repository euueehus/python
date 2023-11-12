""""
e = int(input("數"))

for i in range(1, e + 1):
    if i % 3 == 0 or i % 7 == 0:
        print(i)
"""
e = int(input("x"))
for s in range(e):
    print(" " * (e - 1 - s) + "*" * (s * 2 + 1))
for s in range(e):
    print(" " * (e - 1) + "*")
