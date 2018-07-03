import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("mypic.jpg",1)

#Face detection works better with grayscale images, for converting bgr to grayscale
grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(grey_img, scaleFactor=1.1, minNeighbors=5)
print(faces)

#plotting coordinates on image
for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

resized_img=cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)) )
cv2.imshow("My pic",resized_img)
cv2.waitKey(0)
cv2.closeAllWindows()

