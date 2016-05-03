# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
# import argparse
import imutils
import cv2

from camera import VideoCamera


# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cam = VideoCamera()

skirtCascade = cv2.CascadeClassifier("haarcascades/skirts.xml")
faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

while cam.video.isOpened():
	#Get the image frame
	image = cam.get_frame()

	image = imutils.resize(image, width=min(400, image.shape[1]))

	orig = image.copy()


	
	faces = faceCascade.detectMultiScale(image, 1.1 , 5)

	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 2)

	skirts = skirtCascade.detectMultiScale(image, 5 , 5)
	for (x, y, w, h) in skirts:
		cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), 4)

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
		padding=(8, 8), scale=1.05)


	# draw the original bounding boxes
	# for (x, y, w, h) in rects:
	# 	cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)


	

	# show the output images
	cv2.imshow("After NMS", image)
	if cv2.waitKey(5) & 0xFF == ord('q'):
 		break

cv2.destroyAllWindows()
