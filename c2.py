import cv2
import numpy as np
# print("resize image")
# img = cv2.imread('C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg')
# print(img.shape)
# imgResize = cv2.resize(img,(300,500))   #300 is witdth, 500 is height
# print(imgResize.shape)
# cv2.imshow("output",imgResize)
# cv2.waitKey(0)

# print("cropped image")
# img = cv2.imread('C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg')
# print(img.shape)
# imgCropped = img[0:200,200:500]  #the height come first then width
#                 #0-200 is the height then 200-500 is the width 
# cv2.imshow("output",imgCropped)
# cv2.waitKey(0)

# print("create the color image")
# img = np.zeros((512,512,3),np.uint8) #matrix size
# print(img)
# img[:] = 255,0,0    #color the whole img with [:]
# # img[100:200,200:300] = 255,0,0    #color the rang of selected
# cv2.imshow("img",img)
# cv2.waitKey(0)

# print("create line with the color")
# img = np.zeros((512,512,3),np.uint8) #matrix size
# cv2.line(img,(0,0),(300,300),(100,200,90),3)   #img,start point,end point, color,thickness(thick)
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(100,200,90),3)  #shape[1] mean width, 0 mean height
# cv2.imshow("img",img)
# cv2.waitKey(0)


# print("create retangle with the color")
# img = np.zeros((512,512,3),np.uint8) #matrix size
# # cv2.rectangle(img,(10,10),(300,300),(100,50,90),3)   #img,start point,end point, color,thickness(no full color)
# cv2.rectangle(img,(10,10),(300,300),(100,50,90),cv2.FILLED) #color the inside
# cv2.imshow("img",img)
# cv2.waitKey(0)

# print("create circle with the color")
# img = np.zeros((512,512,3),np.uint8) #matrix size
# cv2.circle(img,(100,100),30,(250,250,190),5) #img, start from, radius, color,thick(size of the border)
# cv2.imshow("img",img)
# cv2.waitKey(0)

# print("create circle with the color")
# img = np.zeros((512,512,3),np.uint8) #matrix size
# cv2.putText(img, " OPENCV ", (100,100),cv2.FONT_HERSHEY_COMPLEX,1,(100,100,100),2)   
#             #img,text show,start from,font style,scale,color,thickness
# cv2.imshow("img",img)
# cv2.waitKey(0)

