while True:
    Polls_Cand_W_name = input("在這份名調中，贏家候選人的名字")
    Polls_Cand_L_name = input("在這份名調中，輸家候選人的名字")

    Polls_Cand_W_got = int(input("輸入贏家候選人得票數"))
    Polls_Cand_L_got = int(input("輸入輸家候選人得票數"))

    Polls_ratio = int(input("輸入此民調抽樣比(輸入百分比，不用加%號)"))

    Pos_number = 0

    Polls_got_left = (100 - Polls_ratio) * (Polls_Cand_W_got + Polls_Cand_W_got) / 100
    x = Polls_got_left
    y = 0

    for k in range(50):
        x_compare = Polls_Cand_W_got * Polls_ratio / 100 + x
        y_compare = Polls_Cand_L_got * Polls_ratio / 100 + y
        x -= 1
        y += 1
        if x_compare > y_compare:
            Pos_number += 1
            Pos_name = Polls_Cand_W_name
            Pos_BL = "T"

        elif x_compare < y_compare:
            Pos_name = Polls_Cand_L_name
            Pos_BL = "F"

        else:
            Pos_name = Polls_Cand_L_name + Polls_Cand_L_name
            Pos_number += 0.5
            Pos_BL = "F"

        print(x_compare, ",", y_compare, ",", Pos_name, ",", Pos_BL)

    print(
        "準確率是",
        Pos_number,
        "/ ",
        Polls_got_left,
        Pos_number / Polls_got_left * 100,
        "%",
    )
