import cv2

faceCascade = cv2.CascadeClassifier("C:/Users/ASUS/Desktop/AR/New folder/openCV/haarcascade_frontalface_default.xml")
img = cv2.imread('C:/Users/ASUS/Desktop/AR/New folder/openCV/ace2.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# find faces
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

# create a bounding box around face
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
cv2.imshow("face",img)
cv2.waitKey(0)