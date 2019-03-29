import cv2
import argparse

arg=argparse.ArgumentParser()

arg.add_argument("-i","--image", required=True, help="path to image")

args=vars(arg.parse_args())



image=cv2.imread(args["image"])

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# get structuring elemement
kernelGroup=[(3,3),(5,5) ,(7,7)]

for kernelsize in kernelGroup:
    kernel= cv2.getStructuringElement(cv2.MORPH_RECT ,kernelsize)
    opening= cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("opening ", opening)
    cv2.waitKey(0)

cv2.waitKey(0)    