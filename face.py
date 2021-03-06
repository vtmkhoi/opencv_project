import cv2
face_cascade=cv2.CascadeClassifier('/home/pi/khoi_workspace/haarcascade_frontface_default.xml')
eye_cascade=cv2.CascadeClassifier('/home/pi/khoi_workspace/haarcascade_eye.xml')

#ReadImage
img=cv2.imread("dog01.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Finding face in the image by using file .XML 
faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5, minSize=(100,100), flags=cv2.CASCADE_SCALE_IMAGE)
print(type(faces))
print(faces)

#Drawing rectangle around faces
for x,y,w,h in face:
    roi_gray=gray_img[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    img = cv2.rectangle(img, (x,y),(x+ư,y+h),(255,0,0),2)
    eyes=eye_cascade.detectMultiScale(roi_gray)
    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh), (0,255,0),2)
resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

#Show image
cv2.imshow("aaa",resized)
cv2.waitKey(1)
cv2.destroyAllWindows