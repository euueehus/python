import tkinter as tk

root = tk.Tk()
root.withdraw()  # 隱藏主視窗


def show(event):
    title = "提示"
    message = "錯誤"
    total_popups = 3  # 彈窗數量

    # 同時顯示所有彈窗
    for i in range(total_popups):
        popup = tk.Toplevel()
        popup.title(f"{title} {i+1}")
        popup.geometry("200x100")  # 設定視窗大小
        popup.transient(root)  # 設定為臨時視窗
        popup.geometry(f"+{100 + i*50}+{100 + i*50}")  # 偏移位置以避免完全重疊

        # 顯示訊息
        label = tk.Label(popup, text=f"{message} {i+1}", font=("Arial", 12))
        label.pack(pady=20)


root.bind("<KeyPress-a>", show)
root.mainloop()
