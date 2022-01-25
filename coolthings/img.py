
import cv2
image = cv2.imread("coolthings\Picture_Alemmaya.jpg")
grey_img= cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
invert=cv2.bitwise_not(grey_img)
blur=cv2.GaussianBlur(invert,(21,21),0)
invertedBlur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img,invertedBlur,scale=250.0)

cv2.imwrite("sketch.PNG",sketch)


