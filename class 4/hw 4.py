"""
測量你的BMI值, 確認你的體重是否正常?
* BMI公式:體重(公斤) / 身高(公尺)的平方
* BMI值正常範圍:14.8到20.7之間
* BMI值過重範圍:20.7以上
EX:
請輸入身高(公尺):1.7
請輸入體重(公斤):45
你的BMI為15.570934256055365
體重過輕
請輸入身高(公尺):1.7
請輸入體重(公斤):60
你的BMI為20.761245674740486
體重正常
請輸入身高(公尺):1.7
請輸入體重(公斤):90
你的BMI為31.14186851211073
體重過重
"""
while True:
    i = 0
    while True:
        w = float(input("請輸入體重"))
        h = float(input("請輸入身高"))
        bmi = w / h**2
        print("你的bmi是:" + str(bmi))
        if bmi > 20.7:
            print("胖子")
        elif bmi < 14.8:
            print("過輕")
        else:
            print("正常")
            i += 1
            if i == 1:
                break
    """
    輸入三角形三邊(存入變數a, b, c中) 
    判斷是否能構成三角形(利用邊長運算進行判斷，可以上網搜尋公式)
    是三角形:則顯示面積和周長
    不是:則顯示，無法構成三角形
    三角形面積公式:
    底*高/2
    p = 1/2 (a+b+c)
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    EX:
    a = 3 
    b = 4
    c = 5
    周長:12.0
    面積:6.0 
    a = 1
    b = 10
    c = 100
    無法構成三角形
    """
    h = 0
    a = int(input("底"))
    b = int(input("高"))
    c = int(input("長"))
    while True:
        try:
            d = a * b / 2
            e = a + b + c
            f = "周長"
            g = "面坤"
            print(g, d)
            print(f, e)
        except:
            print("無法構成三角形")
        h += 1
        if h == 1:
            break
