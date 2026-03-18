""" "
滑鼠功能

點擊操作：

click()：點擊滑鼠左鍵。

doubleClick()：雙擊滑鼠。

rightClick()：點擊滑鼠右鍵。

middleClick()：點擊滑鼠中鍵。

拖放操作：

dragTo(x, y)：將滑鼠拖動到指定位置。

drag(x, y)：相對於當前位置進行拖動。

滾動操作：

scroll()：垂直滾動滑鼠滾輪。

hscroll() 和 vscroll()：橫向或垂直滾動。

鍵盤功能
模擬鍵盤輸入：

write('Hello', interval=0.25)：模擬鍵入文字，每個字母間隔0.25秒。

press('enter')：模擬按下按鍵。

keyDown('shift') 和 keyUp('shift')：模擬按下與鬆開按鍵。

快捷鍵組合：

hotkey('ctrl', 'c')：模擬按下 Ctrl+C。

螢幕功能
螢幕截圖：

screenshot()：截取螢幕，並返回一個 PIL 圖片物件。

locateOnScreen('image.png')：在螢幕上找到與提供圖像匹配的區域。

locateCenterOnScreen('image.png')：返回匹配圖像的中心座標。

像素顏色檢測：

pixel(x, y)：獲取螢幕上指定位置的像素顏色。

pixelMatchesColor(x, y, (r, g, b))：檢查某位置的像素顏色是否與指定顏色匹配。

彈窗功能
顯示簡單的彈窗與訊息框：

alert()：顯示一個警告對話框。

confirm()：顯示一個確認對話框並返回結果。

prompt()：彈出輸入對話框。
"""
