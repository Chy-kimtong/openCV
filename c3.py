import numpy as np
import cv2


# print("(warp img)cropped and make the img into the right in front")
# img = cv2.imread("C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg")
# width,height = 250,350
# pts1 = np.float32([[100,219],[287,188],[154,482],[352,440]])
#             #4 different points, 
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))
# cv2.imshow("Imgage", imgOutput)
# cv2.waitKey(0)

# print("join img together")
# img = cv2.imread("C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg")
# imgHor = np.hstack((img,img))
#     #horizental function
# imgVer = np.vstack((img,img))
#     #vertical one
# cv2.imshow("Imgage", imgVer)    #can't resize, can't work with different color type, lose some img
# cv2.waitKey(0)

# print("color detection")
# path = 'C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg'
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240)
# cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)    #name,window,current value(initial),max value,call function
# img = cv2.imread(path)
# imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow("",imgHSV)
# cv2.waitKey(0)

print("create trackbars to change the value of color")
path = 'C:/Users/ASUS/Desktop/AR/New folder/openCV/output.jpg'
def empty(a):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)    #name,window,current value(initial),max value,call function
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)   
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")   #name of value, name of window
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")   #name of value, name of window
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")   #name of value, name of window
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Mask",imgResult)
    cv2.waitKey(1)


# #detect the shape which type its were base on the corner it get
# def getContours(img):   #function to detect the shape base on the corner
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)    #
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         if area>500:
#             cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
#             peri = cv2.arcLength(cnt,True)
#             print(peri)
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)
#             print(len(approx))
#             objCor = len(approx)
#             x,y,w,h = cv2.boundingRect(approx)
#             # obj mean the number of the corner
#             if objCor==3: 
#                 objectType = "Tri"
#             elif objCor==4:
#                 aspRatio = w/float(h)
#                 if aspRatio > 0.95 and aspRatio <1.05:
#                     objectType = "Square"
#                 else:
#                     objectType = "Retangle"
#             elif objectType>4:
#                 objectType = "Circle"
#             else:objectType="None"
#             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
#             cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)
# print("Shape detection(work with pnj)")
# path = 'C:/Users/ASUS/Desktop/AR/New folder/openCV/shape.png'
# img = cv2.imread(path)
# imgContour = img.copy()
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
# imgCanny = cv2.Canny(imgBlur,50,50)
# getContours(imgCanny)
# imgBlank = np.zeros_like(img)

# cv2.imshow("shape2",imgContour)
# cv2.waitKey(0)