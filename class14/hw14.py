from datetime import datetime


def date(a):
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%Y.%m.%d"]
    for date_format in formats:
        try:
            date = datetime.strptime(a, date_format)  # 讓字串便時間的格式
            return date.strftime("%Y-%m-%d")  # 讓date變("%Y-%m-%d")
        except ValueError:
            continue
    return "Invalid date format. Please enter a valid date."  # 錯誤OwO


E = input("Please enter a date: ")  # 問幾號
print(f"原d{E}變{date(E)}")  # 打印出轉玩的time
