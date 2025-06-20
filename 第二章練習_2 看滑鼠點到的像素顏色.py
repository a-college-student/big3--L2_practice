import numpy as np
import cv2

global img  # 先聲明 img 是全域變數(因為在滑鼠函式裡會用到)

def onMouse(event, x, y, flags, param):
#聲明一個滑鼠偵測函式，這五個參數是 OpenCV 的滑鼠事件系統自動幫你塞進來的
#第一個值(event)回傳:代表你做了什麼事情（按下滑鼠？放開？移動？）
#第二個值(x)回傳:滑鼠所在的座標位置（從左上角開始）
#第三個值(y)回傳:滑鼠所在的座標位置（從左上角開始）
#第四個值(flags)回傳:有沒有按住 Ctrl、Shift、滑鼠拖曳等
#第五個值(param)回傳:額外參數（你可以傳入別的資料)進階
    x, y = y, x 
    #OpenCV 滑鼠事件(x, y)x是橫的y是直的（像平面座標）
    #NumPy 圖片陣列	[row, col] 或 [y, x]先 row 再 column，先上下、再左右
    #所以需要讓滑鼠指到的地方有正確對應到像素需要xy互換
    if img.ndim != 3: #如果維度不是3(灰階)
        print(f"(x, y) = ({x}, {y})", end="  ")
    #python特殊語法:f-string（格式化字串），可以把變數直接放進字串中來輸出
    #舉例f"文字 {變數} 文字" {}裡面可以直接放進變數
    #舉例:
    #name = "小明"
    #score = 95
    #print(f"{name} 的成績是 {score} 分")
        print("Gray-Level = %3d" % img[x, y])
    #Python 中「舊式字串格式化語法:"%3d" % 整數變數，可以讓字串長度固定為三個字元
    #print("%3d" % 7) 結果是:  7   會空兩格來讓字串是三個字元



    
    else:
        print(f"(x, y) = ({x}, {y})", end="  ")
        print("R, G, B = (%3d, %3d, %3d)" %
              (img[x, y, 2], img[x, y, 1], img[x, y, 0]))

filename = input("Please enter filename: ")#輸入要偵測的圖片名稱
img = cv2.imread(filename, -1)
cv2.namedWindow(filename)#開啟一個新視窗
cv2.setMouseCallback(filename, onMouse)#在新視窗載入滑鼠函式
cv2.imshow(filename, img)#將圖片載入新視窗
cv2.waitKey(0)#暫停程式執行直到按下鍵盤任一鍵
cv2.destroyAllWindows()#關閉視窗