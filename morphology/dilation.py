import argparse
import cv2

arg=argparse.ArgumentParser()
arg.add_argument("-i","--image", required=True, help="path to the image")

args=vars(arg.parse_args())


image=cv2.imread(args["image"])

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray" , gray)

dilate=cv2.dilate(gray.copy(), None, iterations=4)

cv2.imshow("dilate afeter {} iteration".format(4), dilate)

cv2.waitKey(0)
cv2.waitKey(0)