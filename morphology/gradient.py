import cv2
import argparse

arg=argparse.ArgumentParser()
arg.add_argument("-i","--image", required=True, help="path to the image")
args=vars(arg.parse_args())


image =cv2.imread(args["image"])

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)

kernelsize=[(3,3),(5,5),(7,7)]
for kernelindex in kernelsize:
	kernel=cv2.getStructuringElement(cv2.MORPH_RECT, kernelindex)
	gradient= cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

	cv2.imshow("opening " , gradient)
	cv2.waitKey(0)