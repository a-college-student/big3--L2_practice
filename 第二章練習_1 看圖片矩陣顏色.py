import cv2
import matplotlib.pyplot as plt
img = cv2.imread("kirby.jpg", -1)  #0:讀灰階，1讀三原色，-1原封不動讀入（包含 alpha(透明度)通道，若圖片有）

#img = cv2.imread() 這個函式它會讀進一張圖片，轉成一個 NumPy 陣列（矩陣），每個像素的 RGB 值都會變成數字。


nr, nc = img.shape[:2] #取前量維度ROW和COL(如果是彩色或含透明就會有四個維度(顏色、透明度))
print("row=",nr);
print("col=",nc);

if img.ndim != 3: #看矩陣的維度
    print("灰階")
else :
    print("顏色")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#將讀取的顏色格式切換成讀出的格式
#print(img[100:110, 100:110])
print(img) #輸出整個矩陣
plt.imshow(img) #將矩陣數值轉成圖片
plt.show() #展示圖片

 
