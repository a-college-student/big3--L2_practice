import cv2
import matplotlib.pyplot as plt
img = cv2.imread("kirby.jpg", -1)  #0:讀灰階，1讀三原色，-1原封不動讀入（包含 alpha(透明度)通道，若圖片有）
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img = cv2.imread() 這個函式它會讀進一張圖片，轉成一個 NumPy 陣列（矩陣），每個像素的 RGB 值都會變成數字。
cv2.line(img, (50, 50), (200, 50), (0, 255, 0), 3)
cv2.rectangle(img, (100, 100), (200, 200), (255, 0, 0), 1)
cv2.circle(img, (150, 150), 30, (150, 100, 255), -1)
cv2.ellipse(img, (200, 200), (80, 40), 30, 0, 360, (0, 255, 255), 2)



plt.imshow(img) #將矩陣數值轉成圖片
plt.show() #展示圖片

 
