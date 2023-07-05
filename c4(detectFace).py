import cv2

# real time detect face
cap = cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480)  #height
# cap.set(10,100)  #brightness
while True:
    success, img = cap.read()
    faceCascade = cv2.CascadeClassifier("C:/Users/ASUSKIM/Desktop/AR/New folder/openCV/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # # find faces
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    # # create a bounding box around face
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)    
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# faceCascade = cv2.CascadeClassifier("C:/Users/ASUSKIM/Desktop/AR/New folder/openCV/haarcascade_frontalface_default.xml")
# img = cv2.imread('C:/Users/ASUSKIM/Desktop/AR/New folder/openCV/face2.png')
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# # # find faces
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)
# # # create a bounding box around face
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
# cv2.imshow("face2",img)
# cv2.waitKey(0)