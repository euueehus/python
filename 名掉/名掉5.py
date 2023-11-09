import random

Pos_number = 0
while 1:
    input()
    W = random.randint(51, 99)
    L = 100 - W
    P = random.randint(1, 100)
    X = W - L

    T = round(((100 - P) / 2 + 0.5 + (P / 20) * (X / 10)), 0)
    P_n = round(((100 - P) / 2 + 0.5 + (P / 20) * (X / 10)), 0) / (100 - P) * 100

    if P_n >= 100:
        P_n = 100

    W1 = W
    L1 = L
    P1 = P

    Polls_Cand_W_Vrate = W1
    Polls_Cand_L_Vrate = L1

    Polls_ratio = P1

    Pos_number = 0
    Polls_ratio_left = 100 - Polls_ratio
    x = Polls_ratio_left
    y = 0

    for k in range(Polls_ratio_left):
        x_compare = Polls_Cand_W_Vrate * Polls_ratio / 100 + x
        y_compare = Polls_Cand_L_Vrate * Polls_ratio / 100 + y
        x -= 1
        y += 1
        if x_compare > y_compare:
            Pos_number += 1
            Pos_BL = "T"

        elif x_compare < y_compare:
            Pos_BL = "F"

        else:
            Pos_BL = "F"
            Pos_num += 0.5
    P_n_2 = Pos_number / Polls_ratio_left * 100

    print(W, L, P)
    print(Pos_number, round(T, 0))
    print(round(P_n), round(P_n_2))
    if P_n == P_n_2:
        print("T")
    else:
        print("F")
