from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
rawCapture = PiRGBArray(camera,size = (640,480))

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port = True):
	image = frame.array
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 7, minSize = (100,100), flags = cv2.CASCADE_SCALE_IMAGE)

	for (x,y,w,h) in faces:
		roi_gray = gray[y:y+h, x:x+w]
		cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
		print (x,y,w,h)
	cv2.imshow("Frame", image)
	if cv2.waitKey(1) & 0xff == ord("q"):
		exit()
	rawCapture.truncate(0)
