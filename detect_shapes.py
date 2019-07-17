import os
import imutils
import cv2
import time

def shapeFinder(image):	 
	# convert the image to grayscale, blur it slightly,
	# and threshold it
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	median = cv2.medianBlur(gray,5)
	blur = cv2.bilateralFilter(median,9,250,250)
	blurred = cv2.GaussianBlur(blur, (5, 5), 0)
	thresh = cv2.adaptiveThreshold(blurred,150,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY_INV,201,20)
	 
	# find contours in the thresholded image and initialize the
	# shape detector
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	#sd = ShapeDetector()
	sqrs = 0
	circs = 0
	lins = 0
	triangs = 0
	# loop over the contours
	for c in cnts:
		# compute the center of the contour, then detect the name of the
		# shape using only the contour
		x,y,w,h = cv2.boundingRect(c)

		shape = ""
		epsilon = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * epsilon, True)

		# if the shape is a triangle, it will have 3 vertices
	
		if len(approx) == 3:
			shape = "Triangle"

		elif len(approx) == 2:
			shape = "Line"
 
		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif len(approx) == 4:
			shape = "Square" 
		# otherwise, we assume the shape is a circle
		else:
			shape = "Circle"

		# multiply the contour (x, y)-coordinates by the resize ratio,
		# then draw the contours and the name of the shape on the image
		c = c.astype("float")
		#c *= ratio
		c = c.astype("int")

		area = cv2.contourArea(c)
		hull = cv2.convexHull(c)
		hull_area = cv2.contourArea(hull)
		#print(hull_area)
		if (hull_area > 0):
			solidity = float(area)/hull_area
		else:
			solidity = 0
		#print(solidity)

		#((w > 30) or (h > 30)) and ((w < 200) and (h < 100))
		#(solidity > 0.9)

		if (x > 0 and (x+w) < 640 and y > 0 and (y+h) < 480 and ((w > 40) or (h > 40)) and ((w < 120) and (h < 120))):
			#values are hard coded like the size of the screen and pixel length
			if (shape == "Line" and (solidity > 0.80)):
				cv2.drawContours(image, [c], -1, (0, 255, 0), 3)

			elif((solidity > 0.95)):
				cv2.drawContours(image, [c], -1, (0, 255, 0), 3)

			else:
				shape = ""

		else:
			shape = ""

		if (shape == "Square"):
			sqrs += 1

		if (shape == "Line"):
			lins += 1

		if (shape == "Triangle"):
			triangs += 1

		if (shape == "Circle"):
			circs += 1
		
		#cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		#	0.5, (255, 255, 0), 2)
	font = cv2.FONT_HERSHEY_DUPLEX
	cv2.putText(image,"Circles: " + str(circs),(10,30), font, 0.9,(0,30,255),2,cv2.LINE_AA)
	cv2.putText(image,"Squares: " + str(sqrs),(10,60), font, 0.9,(0,60,255),2,cv2.LINE_AA)
	cv2.putText(image,"Lines: " + str(lins),(10,90), font, 0.9,(0,90,255),2,cv2.LINE_AA)
	cv2.putText(image,"Triangles: " + str(triangs),(10,120), font, 0.9,(0,120,255),2,cv2.LINE_AA)	 
		# show the output image
	time.sleep(0.2)
		

#def matchShapesFromImage(image, shapePathFormat):
#return 0