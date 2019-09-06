import cv2
import numpy as np
 
cropping = False

rangemin = 158
rangemax = 160

x_start, y_start, x_end, y_end = 0, 0, 0, 0
 
image = cv2.imread('jujubas.jpg')
oriImage = image.copy()
 
 
def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping
 
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
 
    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
 
    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished
 
        refPoint = [(x_start, y_start), (x_end, y_end)]
 
        if len(refPoint) == 2: #when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            # imgHSV = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV) 

            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) 
            cv2.imwrite("testeeee.jpg",roi)
            img = cv2.imread("testeeee.jpg")

            # for l in verifCafe:
            #    for c in l:
            #        (b,g,r) = c
            #        if((b >= 11 and b <=259) and (g>=162 and  g <= 234) and (r >= 223 and r <=255)):
            #            c[2] = 255
            #            c[1] = 255
            #            c[0] = 255

            sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
            sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
            sobelX = np.uint8(np.absolute(sobelX))
            sobelY = np.uint8(np.absolute(sobelY))
            sobel = cv2.bitwise_or(sobelX, sobelY)
            resultado = np.vstack([
            np.hstack([img, sobelX]),
            np.hstack([sobelY, sobel])]) 

            cv2.imwrite("testeeee.jpg",resultado)
            cv2.imshow("Cropped", resultado)
             
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)
	
while True:
 
    i = image.copy()
 
    if not cropping:
        cv2.imshow("image", image)
 
    elif cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
        cv2.imshow("image", i)
 
    cv2.waitKey(1)
 
# close all open windows
cv2.destroyAllWindows()
