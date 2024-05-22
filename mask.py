import cv2
import os
import numpy as np

run = False

def select_region(event, x, y, flag, param):
	global run

	if event == cv2.EVENT_LBUTTONDOWN:
		run = True 

	if event == cv2.EVENT_LBUTTONUP:
		run = False

	if event == cv2.EVENT_MOUSEMOVE:
		if run == True:
			cv2.circle(img, (x,y), 5 , (0,0,0), thickness = cv2.FILLED)
			cv2.imshow('Masked Image',img)

			
			cv2.circle(blank, (x,y), 5 , (0,0,0), thickness = cv2.FILLED)
			cv2.imshow('Binary Mask',blank)


	


img_path = r'C:\Users\ACER\Desktop\Course Projects\Minor Project Resources\Git_Cloned Project Code(2080-11-25)\OcclusionRemoval-Image-Inpainting-\images\house.jpg'
########################## MAIN ############################################



img = cv2.imread(img_path)#loading image

img = cv2.resize(img, (512,512), interpolation = cv2.INTER_AREA)#resizng image to 512,512

cv2.imshow('Masked Image',img)#Displaying original image

blank = np.full((512,512,3), 255,dtype = 'uint8')

cv2.setMouseCallback('Masked Image', select_region)#Mouse callback function

while True:
	if cv2.waitKey(33) == ord('a'):
		os.chdir(r'C:\Users\ACER\Desktop\Course Projects\Minor Project Resources\Git_Cloned Project Code(2080-11-25)\OcclusionRemoval-Image-Inpainting-\images')

		cv2.imwrite("M.png", blank) # save image
		cv2.imwrite("MI.png", img) # save image




cv2.waitKey(0)









