#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from object_recognition_msgs.msg import RecognizedObjectArray, RecognizedObject
import tf
from tf.listener import xyzw_to_mat44
from geometry_msgs.msg import PoseStamped, Pose
import numpy as np 
import pyquaternion

class coke_detect:
    def __init__(self):
        self.image_sub = rospy.Subscriber('/recognized_object_array',RecognizedObjectArray,self.callback)
        self.image_pub = rospy.Publisher('/detect_pose',PoseStamped,queue_size = 1)
    
    def callback(self,array):
        if array.objects:
            pos = array.objects[0].pose.pose.pose
            mat = xyzw_to_mat44(pos.orientation)
            mat[0][3]=pos.position.x
            mat[1][3]=pos.position.y
            mat[2][3]=pos.position.z

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
                
                coke_pos = np.dot(mat44,mat)
                quat= list(pyquaternion.Quaternion(matrix=coke_pos))

                pose = PoseStamped()
                pose.header.frame_id = 'world'
                pose.pose.position.x = coke_pos[0][3]
                pose.pose.position.y = coke_pos[1][3]
                pose.pose.position.z = coke_pos[2][3]
                pose.pose.orientation.w = quat[0]
                pose.pose.orientation.x = quat[1]
                pose.pose.orientation.y = quat[2]
                pose.pose.orientation.z = quat[3]

                self.image_pub.publish(pose)
                print pose
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                print "have'n arm"

class oritation:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0

if __name__ == "__main__":
    rospy.init_node("vision_manager")
    rospy.loginfo("start")
    coke_detect()
    rospy.spin()