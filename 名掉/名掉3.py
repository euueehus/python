while True:
    Polls_Cand_W_name = input("在這份名調中，贏家候選人的名字")
    Polls_Cand_M_name = input("在這份名調中，中間候選人的名字")
    Polls_Cand_L_name = input("在這份名調中，輸家候選人的名字")

    Polls_Cand_W_Vrate = float(input("輸入贏家候選人得票率(輸入百分比，不用加%號)"))
    Polls_Cand_M_Vrate = float(input("輸入中間候選人得票率(輸入百分比，不用加%號)"))
    Polls_Cand_L_Vrate = float(input("輸入輸家候選人得票率(輸入百分比，不用加%號)"))
    alist_1 = [Polls_Cand_W_Vrate, Polls_Cand_M_Vrate, Polls_Cand_L_Vrate]

    T = 0
    h1 = 0

    Polls_ratio = int(input("輸入此民調抽樣比(輸入百分比，不用加%號)"))

    Polls_pos_N = 0
    for i in alist_1:
        T += 1
        for k in range(100 - i):
            for h1, h2 in enumerate["W", "M", "L"]:
                h1 += 1
                exec("if i == {} :".format(h1))
                exec("  ")
