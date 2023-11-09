W = int(input("W"))
L = int(input("L"))
P = int(input("P"))
X = W - L


P_n_1 = round((100 - P) / 2 + 0.5 + (P / 20) * (X / 10))


print(P_n_1, "/", 100 - P)
