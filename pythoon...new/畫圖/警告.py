import tkinter as tk
from PIL import Image, ImageTk
import os
import random


def custom_alert(message, title="錯誤", folder_path=None):
    root = tk.Tk()
    root.title(title)
    root.resizable(False, False)  # 禁止手動調整視窗大小

    # 載入圖片
    image_path = None
    if folder_path and os.path.isdir(folder_path):
        # 取得資料夾中的圖片檔案
        image_extensions = (".png", ".jpg", ".jpeg", ".gif")
        images = [
            f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)
        ]

        if images:
            # 隨機選擇一張圖片
            image_path = os.path.join(folder_path, random.choice(images))

    # 顯示圖片
    if image_path and os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            img = img.resize((150, 150), Image.LANCZOS)  # 縮放圖片至150x150
            photo = ImageTk.PhotoImage(img)
            label_img = tk.Label(root, image=photo)
            label_img.image = photo  # 保持圖片引用
            label_img.pack(pady=10)
        except Exception as e:
            tk.Label(root, text=f"無法載入圖片: {e}", font=("Arial", 12)).pack(pady=10)
    else:
        tk.Label(root, text="無圖片", font=("Arial", 12)).pack(pady=10)

    # 顯示訊息
    tk.Label(root, text=message, font=("Arial", 14), wraplength=350).pack(pady=10)

    # OK 按鈕
    tk.Button(root, text="OK", command=root.destroy, font=("Arial", 12)).pack(pady=10)

    # 居中顯示視窗
    root.eval("tk::PlaceWindow . center")
    root.mainloop()


# TODO: 你需要修改這裡
# 指定包含圖片的資料夾路徑
folder_path = r"C:\Users\user\Desktop\py\pythoon...new\photo"
if __name__ == "__main__":
    custom_alert("what can i say 好玩嗎~", title="測試", folder_path=folder_path)
