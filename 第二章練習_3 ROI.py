import numpy as np
import cv2

img = cv2.imread("kirby.jpg", -1)

# 2. 輸入 ROI 的起點座標 (左上角)
ROI_x, ROI_y = eval(input("請輸入 ROI 的左上角座標 (x, y): "))

# 3. 輸入 ROI 的大小（列數、行數）→ 也就是高和寬
ROI_nr, ROI_nc = eval(input("請輸入 ROI 的大小 (rows, columns): "))

# 4. 取出 ROI 區域（使用 NumPy 切片）
'''
語法結構:img[rows範圍 , columns範圍]
img是NumPy陣列（ndarray） 表示的影像資料矩陣
ROI在做的是擷取矩陣某部分，例如:
img[rows範圍 , columns範圍]
ROI_y : ROI_y + ROI_nr就是row的範圍
ROI_x : ROI_x + ROI_nc就是col的範圍
'''
ROI = img[ROI_y : ROI_y + ROI_nr, ROI_x : ROI_x + ROI_nc]

# 5. 將 ROI 儲存為一張新圖
cv2.imwrite("kirby_ROI.jpg", ROI)

# 6. 顯示原圖與 ROI 圖片
cv2.imshow("原圖", img)
cv2.imshow("ROI 區塊", ROI)
cv2.waitKey(0) #按下鍵盤繼續執行以下程式
cv2.destroyAllWindows()#關掉所有視窗
