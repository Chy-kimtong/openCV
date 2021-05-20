import cv2
import numpy as np
## waitkey is Milisecond


# print("imported image")
# img = cv2.imread("C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg")
# cv2.imshow("output",img)
# cv2.waitKey(0)

# print("play video")
# cap = cv2.VideoCapture("address")
# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# print("record video from default cam(0 as default)")
# cap = cv2.VideoCapture(0)
# cap.set(3,640) #width
# cap.set(4,480)  #height
# # cap.set(10,100)  #brightness
# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# print("color changing of image")
# img = cv2.imread("C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("output",imgGray)
# cv2.waitKey(0)

# print("blur image")
# img = cv2.imread("C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg")
# imgBlur = cv2.GaussianBlur(img,(7,7),0)
# cv2.imshow("output",imgBlur)
# cv2.waitKey(0)

# print("canny image(black and white)")
# img = cv2.imread("C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg")
# imgCanny = cv2.Canny(img,150,100)
# cv2.imshow("output",imgCanny)
# cv2.waitKey(0)

# kernel = np.ones((5,5),np.uint8)
# print("dilation image")
# img = cv2.imread("C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg")
# imgCanny = cv2.Canny(img,150,100)
# imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
# cv2.imshow("output",imgDilation)
# cv2.waitKey(0)

# kernel = np.ones((5,5),np.uint8)
# print("eroded image")
# img = cv2.imread("C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg")
# imgCanny = cv2.Canny(img,150,100)
# imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
# imgEroded = cv2.erode(imgDilation,kernel,iterations=1)
# cv2.imshow("output",imgEroded)
# cv2.waitKey(0)

