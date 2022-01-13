#Read a video stream from camera (Frame by frame)
import cv2
cap=cv2.VideoCapture(0)
	
while True:
	#frame is the video input, and gray_frame give grayscale version of video input
	ret,frame=cap.read()
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if ret==False:
		continue

	#display the frame and gray_frame
	cv2.imshow('Video Frame',frame)
	cv2.imshow('Gray Frame',gray_frame)

	#wait for user input ->q , thenyou'll stop the loop
	key_pressed=cv2.waitKey(1) & 0xFF
	if key_pressed==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
