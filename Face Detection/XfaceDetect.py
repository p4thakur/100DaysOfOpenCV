import argparse
import cv2

#add argument
arg=argparse.ArgumentParser()
arg.add_argument("-f","--face", required=True, help="path to the haar cascade detector")
arg.add_argument("-i","--image", required=True, help="path to the image")

args= vars(arg.parse_args())

# load the image from the disk
image= cv2.imread(args["image"])

#covert it to gray , since color did not effect our face detection result
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load our face detector

detector= cv2.CascadeClassifier(args["face"])

#using detector to detect face , and return rectangles arounf it

rects= detector.detectMultiScale(gray, scaleFactor=1.07 , minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

#loop over all the bounding box and draw the rectangle on image
for (x,y,w,h) in rects:
    cv2.rectangle(image, (x,y), (x+w,y+h) ,(0,0,255), 2)

cv2.imshow("FaceDetection", image)
cv2.waitKey(0)    
	