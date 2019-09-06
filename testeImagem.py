import cv2
import numpy as np
from matplotlib.image import imread  

img = cv2.imread("rgb.png")


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(np.array(img))

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Original", img)
print(np.array(img))
status = cv2.imwrite("testedeimagem0.png",img)	
print(status)
cv2.waitKey(0)