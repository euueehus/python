while True:
    Polls_Cand_W_name = input("在這份名調中，贏家候選人的名字")
    Polls_Cand_L_name = input("在這份名調中，輸家候選人的名字")

    Polls_Cand_W_Vrate = float(input("輸入贏家候選人得票率(輸入百分比，不用加%號)"))
    Polls_Cand_L_Vrate = float(input("輸入輸家候選人得票率(輸入百分比，不用加%號)"))

    Polls_ratio = int(input("輸入此民調抽樣比(輸入百分比，不用加%號)"))

    Pos_number = 0

    Polls_ratio_left = 100 - Polls_ratio
    x = Polls_ratio_left
    y = 0

    for k in range(50):
        x_compare = Polls_Cand_W_Vrate * Polls_ratio / 100 + x
        y_compare = Polls_Cand_L_Vrate * Polls_ratio / 100 + y
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
            Pos_BL = "F"

        print(x_compare, ",", y_compare, ",", Pos_name, ",", Pos_BL)

    print(
        "準確率是",
        Pos_number,
        "/ ",
        Polls_ratio_left,
        Pos_number / Polls_ratio_left * 100,
        "%",
    )
