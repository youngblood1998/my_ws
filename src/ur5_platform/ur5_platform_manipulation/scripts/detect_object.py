#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import numpy as np 
from math import *
from geometry_msgs.msg import Pose

 
class Image_converter:
    def __init__(self):
	self.image_pub = rospy.Publisher('detect_test',Image,queue_size = 10)
	# self.image_pub = rospy.Publisher('detect_test',Image,queue_size = 1)
	self.bridge = CvBridge()
	self.image_sub = rospy.Subscriber('/head_mount_kinect2/rgb/image_raw',Image,self.callback)
    # self.image_sub = rospy.Subscriber('/head_mount_kinect2/rgb/image_raw',Image,self.callback,queue_size=1,buff_size=52428800)
    

    def callback(self,data):
		try:
		    cv_image = self.bridge.imgmsg_to_cv2(data,"bgr8")
		except CvBridgeError as e:
		    print e
		size = self.detect_table(cv_image)
		detect_image = self.detect_box(size[0], size[1], size[2], size[3], size[4])
		try:
			self.image_pub.publish(self.bridge.cv2_to_imgmsg(detect_image,"bgr8"))
		except CvBridgeError as e:
			print e


    def detect_table(self,image):
		b, g, r = cv2.split(image)
		binary_image = cv2.medianBlur(r, 3)
		for i in range (binary_image.shape[0]):
		    for j in range (binary_image.shape[1]):
				editValue = binary_image[i, j]
				editValue2 = g[i, j]
				if editValue >= 0 and editValue < 20 and editValue2 >= 0 and editValue2 < 20:
					binary_image[i, j] = 255	
				else:
					binary_image[i, j] = 0
	
		img, cnts, hierarchy = cv2.findContours(binary_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		x, y, w, h = cv2.boundingRect(binary_image)
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)
	        # loop over the contours
		# for c in cnts:
		# 	# compute the center of the contour
		# 	M = cv2.moments(c)

		# 	if int(M["m00"]) not in range(20000, 250000):
		# 		continue

		# 	cX = int(M["m10"] / M["m00"])
		# 	cY = int(M["m01"] / M["m00"])
		# 	cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)
		return image, x, y, w, h
   

    def detect_box(self,image, x, y, w, h):
		b, g, r = cv2.split(image)
		binary_image = cv2.medianBlur(g, 3)
		for i in range (binary_image.shape[0]):
		    for j in range (binary_image.shape[1]):
				editValue = binary_image[i, j]
				editValue2 = r[i,j]
				editValue3 = b[i,j]
				if  i < y or i > y+h or j < x or j > x+0.8*w:
					binary_image[i, j] = 0
				else:
					if editValue2 > 186 and editValue2 <= 246 and editValue > 96 and editValue <= 236 and editValue3 > 45 and editValue3 <= 196:
						binary_image[i, j] = 255
					else:
						binary_image[i, j] = 0
		img, cnts, hierarchy = cv2.findContours(binary_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		number=1
		while rospy.search_param("/cube_position_x"+str(number)):
			rospy.delete_param("/cube_position_x"+str(number))
			rospy.delete_param("/cube_position_y"+str(number))
			number=number+1
		number=0
		for cnt in cnts:
			x, y, w, h = cv2.boundingRect(cnt)
			if w>20 and h>20:
				cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)
				rospy.loginfo(str(x+0.5*w)+","+str(y+0.5*h))
				number=number+1
				rospy.set_param("/cube_position_y"+str(number),(290-(x+0.5*w))*0.065/40)
				rospy.set_param("/cube_position_x"+str(number),(580-(y+0.5*h))*0.065/40)
		# x1,y1,w1,h1 = cv2.boundingRect(binary_image)
		# cv2.rectangle(image, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 3)
		# cv2.drawContours(image, cnts, -1, (255, 0, 0), 2)
		# for c in cnts:
		# 	# compute the center of the contour
		# 	M = cv2.moments(c)

		# 	if int(M["m00"]) not in range(20000, 250000):
		# 		continue

		# 	cX = int(M["m10"] / M["m00"])
		# 	cY = int(M["m01"] / M["m00"])
		# 	cv2.circle(image, (cX, cY), 5, (255, 0, 0), -1)
		return image
    
	

if __name__ == "__main__":
    rospy.init_node("vision_manager")
    rospy.loginfo("start")
    Image_converter()
    rospy.spin()