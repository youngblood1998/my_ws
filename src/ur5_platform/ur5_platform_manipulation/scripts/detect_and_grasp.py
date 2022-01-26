#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image,PointCloud2
from sensor_msgs import point_cloud2
import numpy as np 
from math import *
import moveit_commander
from moveit_msgs.msg import MoveItErrorCodes
import time
import message_filters
import tf
from tf.listener import xyzw_to_mat44
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)

class Image_converter:
    def __init__(self):
	self.image_pub = rospy.Publisher('/detect_test',Image,queue_size = 2)
	# self.image_pub = rospy.Publisher('detect_test',Image,queue_size = 1)
	self.bridge = CvBridge()
	self.image_sub = message_filters.Subscriber('/head_mount_kinect2/rgb/image_raw',Image,queue_size=1,buff_size=52428800)
	self.depth_sub = message_filters.Subscriber('/head_mount_kinect2/depth_registered/points', PointCloud2, queue_size=1,buff_size=52428800)
	sync = message_filters.ApproximateTimeSynchronizer([self.image_sub, self.depth_sub],1,0.005,allow_headerless=True)
	sync.registerCallback(self.callback)
    # self.image_sub = rospy.Subscriber('/head_mount_kinect2/rgb/image_raw',Image,self.callback,queue_size=1,buff_size=52428800)

    def callback(self,rgb,depth):
		try:
		    cv_image = self.bridge.imgmsg_to_cv2(rgb,"bgr8")
		except CvBridgeError as e:
		    print e
		size = self.detect_table(cv_image)
		detect_image = self.detect_box(size[0], size[1], size[2], size[3], size[4],depth)
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

    def detect_box(self,image, x, y, w, h , p_cloud):
		assert isinstance(p_cloud, PointCloud2)
		gen = point_cloud2.read_points(p_cloud, field_names=("x", "y", "z"), skip_nans=True)
		time.sleep(1)
		p = list(gen)
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
		while rospy.search_param("/cube_position"+str(number)):
			rospy.delete_param("/cube_position"+str(number))
			# rospy.delete_param("/point_y"+str(number))
			# rospy.delete_param("/point_z"+str(number))
			rospy.delete_param("/cube_position_o"+str(number))
			rospy.delete_param("/cube_position_w"+str(number))
			number=number+1
		number=0
		for cnt in cnts:
			rect = cv2.minAreaRect(cnt)
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			if (box[0][0]-box[1][0])**2+(box[0][1]-box[1][1])**2 >= 250 and (box[0][0]-box[3][0])**2+(box[0][1]-box[3][1])**2 >= 250:
				# rospy.loginfo(box)
				number=number+1
				image_y=int((box[0][1]+box[1][1]+box[2][1]+box[3][1])/4)
				image_x=int((box[0][0]+box[1][0]+box[2][0]+box[3][0])/4)
				point=p[image_y*640+image_x]
				w0_p=box[0][1]*640+box[0][0]
				w1_p=box[1][1]*640+box[1][0]
				w0=p[w0_p]
				w1=p[w1_p]
				while w0[2]-point[2] > 0.005:
					w0_p = w0_p-640
					w0=p[w0_p]
				while w1[2]-point[2] > 0.005:
					w1_p = w1_p+1
					w1=p[w1_p]
				width=((w1[1]-w0[1])**2+(w1[0]-w0[0])**2)**(1.0/2)+0.003
				rospy.set_param("/cube_position_w"+str(number),round(width,4))
				listener = tf.TransformListener()
				try:
					(trans,rot) = listener.lookupTransform('/world', '/_kinect2_rgb_optical_frame', rospy.Time(0))
					# (trans,rot) = listener.lookupTransform('/world', '/_kinect2_rgb_optical_frame', rospy.Time(0))
					ori = oritation()
					ori.x = rot[0]
					ori.y = rot[1]
					ori.z = rot[2]
					ori.w = rot[3]
					mat44 = xyzw_to_mat44(ori)
					mat44[0][3]=trans[0]
					mat44[1][3]=trans[1]
					mat44[2][3]=trans[2]
					pointT=[]
					cube_position=[]
					for i in point:
						pointT.append([i])
					pointT.append([1])
					# print(mat44)
					# print(pointT)
					print(np.dot(mat44,pointT))
					position=np.dot(mat44,pointT)
					cube_position.append(round(position[0][0],4))
					cube_position.append(round(position[1][0],4))
					cube_position.append(round(position[2][0],4))
					rospy.set_param("/cube_position"+str(number),cube_position)
				except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
					continue
				if box[0][0] == box[1][0]:
					rospy.set_param("/cube_position_o"+str(number),0)
				else:
					rospy.set_param("/cube_position_o"+str(number),round(atan(round(float(box[0][1]-box[1][1])/(box[0][0]-box[1][0]),3)),3))
				# if box[0][0] == box[1][0]:
				# 	rospy.set_param("/cube_position_o"+str(number),-1.8)
				# else:
				# 	rospy.set_param("/cube_position_o"+str(number),round(atan(round(float(box[0][1]-box[1][1])/(box[0][0]-box[1][0]),3)),3)-1.8)
				# pos = [(580-(box[0][1]+box[1][1]+box[2][1]+box[3][1])/4)*0.065/40,(290-(box[0][0]+box[1][0]+box[2][0]+box[3][0])/4)*0.065/40]
				# rospy.set_param("/cube_position"+str(number),pos)
				cv2.drawContours(image, [box], 0, (0, 255, 0), 1)
		try:
			if rospy.search_param("/cube_position1"):
				self.grasp()
		except MoveItErrorCodes as e:
			print e
		return image

    def vision_grasp(self,arm,grp,pos,ori,wid):
        # orien = arm.get_current_pose().pose
        # q = quaternion_from_euler(np.deg2rad(180.0) ,0.0,0.0)
        # pose.orientation = Quaternion(*q)
        # arm.set_pose_target(pose)
        # arm.go(wait = True)

        pose = Pose()
        pose.position.x = pos[0]
        pose.position.y = pos[1]
        pose.position.z = pos[2]+0.25
        pose.orientation.x=-1
        pose.orientation.y=0
        pose.orientation.z=0
        pose.orientation.w=0
        arm.set_pose_target(pose)
        arm.go(wait = True)

        # pose = arm.get_current_pose().pose
        # pose.orientation.x=-1
        # pose.orientation.y=0
        # pose.orientation.z=0
        # pose.orientation.w=0
        # arm.set_pose_target(pose)
        # arm.go(wait = True)

        orien=arm.get_current_joint_values()
        orien[5]=orien[5]+ori
        arm.set_joint_value_target(orien)
        arm.go(wait=True)

        grp.set_joint_value_target([0,0,0,0,0,0])
        grp.go(wait=True)

        pose = arm.get_current_pose().pose
        pose.position.z -=0.075
        arm.set_pose_target(pose)
        arm.go(wait = True)

        width=round(9*(0.09-wid)+0.036,3)
        grp.set_joint_value_target([0,0,width,0,0,0])
        grp.go(wait=True)

        pose.position.z =1
        arm.set_pose_target(pose)
        arm.go(wait = True)

        # orien=arm.get_current_joint_values()
        # orien[5]=orien[5]-ori
        # arm.set_joint_value_target(orien)
        # arm.go(wait=True)

        pose.position.x=0.6
        pose.position.y=-0.34
        # pose.position.z =0.64
        arm.set_pose_target(pose)
        arm.go(wait = True)

        pose.position.z =0.84
        arm.set_pose_target(pose)
        arm.go(wait = True)

        grp.set_joint_value_target([0,0,0,0,0,0])
        grp.go(wait=True)

        pose.position.z =1
        arm.set_pose_target(pose)
        arm.go(wait = True)

    def grasp(self):
        arm = moveit_commander.MoveGroupCommander("manipulator")
        grp = moveit_commander.MoveGroupCommander("gripper")
        arm.set_goal_position_tolerance(0.005)
        arm.set_goal_orientation_tolerance(0.01)
        arm.set_planning_time(5)
        grp.set_planning_time(5)

        number=0
        while rospy.search_param("/cube_position"+str(number+1)):
            number = number + 1

        arm.set_joint_value_target([-0.21957805043352518, -1.097296859939564, 1.8945345194815335,
                                -2.366067038969164, -1.571228181260084, -1.8])
        arm.go(wait=True)

        while number>0:
            position=rospy.get_param("/cube_position"+str(number))
            position_o=rospy.get_param("/cube_position_o"+str(number))
            position_w=rospy.get_param("/cube_position_w"+str(number))
            self.vision_grasp(arm,grp,position,position_o,position_w)
            number = number - 1

        arm.set_named_target("home")
        arm.go(wait = True)

class oritation:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0

if __name__ == "__main__":
    rospy.init_node("vision_manager")
    arm = moveit_commander.MoveGroupCommander("manipulator")
    arm.set_named_target("home")
    arm.go(wait = True)
    rospy.loginfo("start")
    Image_converter()
    rospy.spin()