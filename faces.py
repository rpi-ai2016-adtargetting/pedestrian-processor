import numpy as np
import cv2


# Displays image, press any key to close window
def displayImage(img):
	cv2.imshow("Detect Features", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	
	img = cv2.imread("photos/sample2.png", 1)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



	faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
	faces = faceCascade.detectMultiScale(gray, 1.1 ,5)
	print "Found %d faces" %(len(faces))

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

	"""
	bodyCascade = cv2.CascadeClassifier("haarcascades/haarcascade_fullbody.xml")
	body = bodyCascade.detectMultiScale(gray, 1.1 ,5)
	print "Found %d bodies" %(len(body))
	for (x, y, w, h) in body:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

	"""

	


	skirtCascade = cv2.CascadeClassifier("haarcascades/skirts.xml")
	skirts = skirtCascade.detectMultiScale(img, 1.3, 4)
	
	print "Found %d skirts" %(len(skirts))
	for (x, y, w, h) in skirts:
		cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)





	displayImage(img)



	

