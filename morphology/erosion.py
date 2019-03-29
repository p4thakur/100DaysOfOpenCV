import argparse
import cv2

arg=argparse.ArgumentParser()
#add the argument
arg.add_argument("-i","--image",required=True,help="path to my image in the disk") #-i matters ,--i gives error with key
#parse argument
args=vars(arg.parse_args())


#load the image from disk
image=cv2.imread(args["image"])

#covert it to gray
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray);

#erodoe the image
erode=cv2.erode(gray.copy(),None, iterations=2)
cv2.imshow("eroding {} times".format(4 ), erode)
cv2.waitKey(0)

##after eroding let find outline using gradient
kernelsize=[(3,3),(5,5),(7,7)]
for kernelindex in kernelsize:
	kernel=cv2.getStructuringElement(cv2.MORPH_RECT, kernelindex)
	gradient= cv2.morphologyEx(erode, cv2.MORPH_GRADIENT, kernel)

	cv2.imshow("opening " , gradient)
	cv2.waitKey(0)