import tkinter as tk
from tkinter import messagebox

s = 2  # 重複顯示 messages 列表的次數


def show():
    messages = [
        ("資訊", "這是第一個資訊對話框！"),
        ("警告", "這是第二個警告對話框！"),
        ("錯誤", "這是第三個錯誤對話框！"),
    ]

    for _ in range(s):  # 重複 s 次
        for title, message in messages:
            messagebox.showinfo(title, message)


root = tk.Tk()
root.title("多個對話框範例")
root.geometry("300x200")

button = tk.Button(root, text="顯示對話框", command=show)
button.pack(pady=20)

root.mainloop()
