while True:
    Polls_Cand_W_name = input("在這份名調中，贏家候選人的名字")
    Polls_Cand_M_name = input("在這份名調中，中間候選人的名字")
    Polls_Cand_L_name = input("在這份名調中，輸家候選人的名字")

    Polls_Cand_W_Vrate = float(input("輸入贏家候選人得票率(輸入百分比，不用加%號)"))
    Polls_Cand_M_Vrate = float(input("輸入中間候選人得票率(輸入百分比，不用加%號)"))
    Polls_Cand_L_Vrate = float(input("輸入輸家候選人得票率(輸入百分比，不用加%號)"))
    alist_1 = [Polls_Cand_W_Vrate, Polls_Cand_M_Vrate, Polls_Cand_L_Vrate]

    T = 0
    TT = 0
    h1 = 0

    Polls_ratio = int(input("輸入此民調抽樣比(輸入百分比，不用加%號)"))

    Polls_pos_N = 0
    for i in alist_1:
        T += 1
        alist_2 = ["W", "M", "L"]
        for k in range(100 - round(i)):
            for h1, h2 in enumerate(alist_2):
                print(h1)
                h1 += 1
                # exec(alist_2.pop({alist_2[T - 1])})
                alist_2.remove(alist_2[T - 1])
                for num in ["1", "100"]:
                    TT += 1
                    print(TT)
                    exec("ano_{} = alist_2[{}]".format(TT, TT - 1))
                    exec("ano_{} = {}".format(TT, num))
