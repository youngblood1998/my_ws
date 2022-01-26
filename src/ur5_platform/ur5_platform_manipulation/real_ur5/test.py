#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import numpy as np 
from math import *
import moveit_commander
from moveit_msgs.msg import MoveItErrorCodes
import tf
from tf.listener import xyzw_to_mat44
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Quaternion,
    Point
)
import pyquaternion
from visualization_msgs.msg import MarkerArray
from gpd.msg import GraspConfigList

LIMIT_HEIGHT = 0.245
INIT_JOINT = [4.627913475036621, -0.6059587637530726, 0.8184685707092285, -1.1355298201190394, -1.1078336874591272, -0.9894197622882288]
END_JOINT = [4.791444778442383, -0.7117999235736292, 0.8185887336730957, -1.1358402411090296, -0.9749496618853968, -0.9413073698626917]
FLAG_NUM = 1
# qw: 0.9994347292050078
# qx: -0.010733231096187172
# qy: -0.0228922415663458
# qz: 0.022157731951095962
# x: -0.00176669771701
# y: -0.07014813811991
# z: 0.07326713482451

class Gpd_grasp:
    def __init__(self):
        rospy.init_node("vision_manager")
        self.array_sub = rospy.Subscriber('/detect_grasps/clustered_grasps',GraspConfigList,self.callback,queue_size=1,buff_size=52428800)

    def callback(self,array):
        print array.grasps[0].width.data

if __name__ == "__main__":
    rospy.loginfo("start")
    Gpd_grasp()
    rospy.spin()