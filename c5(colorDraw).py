import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,130)

myColors= [[5,107,0,19,255,255] #orange
            ,[133,56,0,159,156,255], #purple
            [57,76,0,100,255,255]   #green
            ]
myColorValues = [[51,153,255],
                [255,0,255],
                [0,255,0]]

myPoints = []   #[x,y,colorId]

# function to find color
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
        # cv2.imshow(str(color[0]), mask)
    return newPoints

def getContours(img):   #function to detect the shape base on the corner
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)    #
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)


while True:
    success,img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# #in order to get the exact code of color we need this to test
# print("create trackbars to change the value of color in real camera")
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)
# cap.set(10,150)
# def empty(a):
#     pass
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240)
# cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)    #name,window,current value(initial),max value,call function
# cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
# cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
# cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
# cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
# cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
# while True:
#     success, img = cap.read()
#     imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)   
#     h_min = cv2.getTrackbarPos("Hue Min","TrackBars")   #name of value, name of window
#     h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min","TrackBars")   #name of value, name of window
#     s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min","TrackBars")   #name of value, name of window
#     v_max = cv2.getTrackbarPos("Val Max","TrackBars")
#     print(h_min,h_max,s_min,s_max,v_min,v_max)
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max,s_max,v_max])
#     mask = cv2.inRange(imgHSV,lower,upper)
#     imgResult = cv2.bitwise_and(imgHSV,imgHSV,mask=mask)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     cv2.imshow("Mask",imgResult)
#     cv2.waitKey(1)