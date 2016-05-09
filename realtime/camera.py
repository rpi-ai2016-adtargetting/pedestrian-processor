import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        #self.video = cv2.VideoCapture("photos/move.mov")

    def __del__(self):
        self.video.release()

	def isOpened(self):
		return self.video.isOpened()

    def get_frame(self):
        success, image = self.video.read()
        return image
