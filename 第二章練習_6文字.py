import numpy as np      # 匯入 NumPy 套件，用來處理數字陣列
import cv2              # 匯入 OpenCV 套件，做影像處理用

# 建立一張黑底圖片（高400，寬500，3 色通道，像素值全為 0 就是黑色）
img = np.zeros((400, 500, 3), dtype='uint8')

# 要顯示的文字
text = "Hello OpenCV"

# 第 1 種字體：SIMPLEX
fontFace = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text, (10, 50), fontFace, 1.0, (255, 255, 255))

# 第 2 種字體：PLAIN
fontFace = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, text, (10, 90), fontFace, 1.0, (255, 255, 255))

# 第 3 種字體：DUPLEX
fontFace = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, text, (10, 130), fontFace, 1.0, (255, 255, 255))

# 第 4 種字體：COMPLEX
fontFace = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text, (10, 170), fontFace, 1.0, (255, 255, 255))

# 第 5 種字體：TRIPLEX
fontFace = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img, text, (10, 210), fontFace, 1.0, (255, 255, 255))

# 第 6 種字體：COMPLEX_SMALL（比較細）
fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(img, text, (10, 250), fontFace, 1.0, (255, 255, 255))

# 第 7 種字體：SCRIPT_SIMPLEX（像手寫）
fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img, text, (10, 290), fontFace, 1.0, (255, 255, 255))

# 第 8 種字體：SCRIPT_COMPLEX（更華麗手寫）
fontFace = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(img, text, (10, 330), fontFace, 1.0, (255, 255, 255))

# 顯示圖片（視窗名稱為 "Example"）
cv2.imshow("Example", img)
cv2.waitKey(0)            # 等待鍵盤輸入才會關閉視窗
cv2.destroyAllWindows()   # 關閉所有 OpenCV 視窗
