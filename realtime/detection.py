# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import imutils
import cv2

from camera import VideoCamera
#from ad_retrieval.ad_retrieval import AdSystem
import ad_retrieval.ad_retrieval as AdSystem
import nearest_neighbor_color
import colorDetection

from PIL import Image

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# initialize HAAR pretrained haar cascade classifiers
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
genderCascade = cv2.CascadeClassifier("./haarcascade_gender_alt2.xml")

# initialize our camera feed
cam = VideoCamera()

#initialize ad system
ads = AdSystem.create_ads_list()

# while the video stream is open, get the image frame by frame
while cam.video.isOpened():
	#Get the image frame
	image = cam.get_frame()

	image = imutils.resize(image, width=min(400, image.shape[1]))

	orig = image.copy()

	# detect pedestrians in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
		padding=(8, 8), scale=1.05)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	# If we did not find any pedestrains, do manual close-range object detection
	if not len(pick):
		# convert image to gray scale, since haar cascade was trained on greyscale images
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# Find faces in the image
		faces = faceCascade.detectMultiScale(
		    gray,
		    scaleFactor=1.1,
		    minNeighbors=5,
		    minSize=(30, 30),
		    flags = 0
		)

		# For each face, manually scale the bounding rectangle to encompass the person's body
		for (x, y, w, h) in faces:
			scale = w * h / 100;
			xA = x - scale;
			xB = x + scale + w;
			yA = y - (scale / 2);
			yB = y + (10 * scale)+ h;

			cropped_face = image[yA:yB, xA:xB]
			# Detect gender in the image
			genders = genderCascade.detectMultiScale(cropped_face, 1.1, 5)
			color = (255,0,0) if len(genders) else (255, 192, 203)
			gender = "Male" if len(genders) else "Female"
			cv2.putText(image,"Gender: %s" % (gender), (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))

			#Display the common color in the image if the bounding box was not cropped
			try:
				rgb = (image[(x+x+w)/2][y+2*h])
				for i in xrange(0, 40):
					for j in xrange(0, 40):
						image[i][j] = rgb
				rgb_real = [rgb[2], rgb[1], rgb[0]]
				temp_col = nearest_neighbor_color.find_closest_color(rgb_real)
				ad = AdSystem.get_random_ad(temp_col, gender, ads)
				if ad is not None:
					print(ad)
					cv2.imshow("Ad", ad)
			except:
				pass

			cv2.rectangle(image, (xA, yA), (xB, yB), color, 2)
	else:
		for (xA, yA, xB, yB) in pick:
			cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

	# show the output images
	cv2.imshow("Pedestrian", image)
	if cv2.waitKey(5) & 0xFF == ord('q'):
 		break

cv2.destroyAllWindows()
