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

GRIPPER_OPEN = [0,0,0,0,0,0]
GRIPPER_CLOSED = [0,0,0.22,0,0,0]
HOME = [-0.0078, -2.2697, 2.3410, -1.6402, -1.5851, 1.5699]

class Gpd_grasp:
    def __init__(self):
        rospy.init_node("vision_manager")
        self.arm = moveit_commander.MoveGroupCommander("manipulator")
        self.gripper = moveit_commander.MoveGroupCommander("gripper")
        self.arm.set_goal_position_tolerance(0.01)
        self.arm.set_goal_orientation_tolerance(0.01)
        self.arm.allow_replanning(True)
        self.arm.set_pose_reference_frame("world")
        self.arm.set_planning_time(5)

        self.arm.set_named_target('home')
        self.arm.go()

        self.gripper.set_joint_value_target(GRIPPER_OPEN)
        self.gripper.go()
        rospy.sleep(1)

        self.array_sub = rospy.Subscriber('/detect_grasps/grasps_rviz',MarkerArray,self.callback,queue_size=1,buff_size=52428800)

    def callback(self,array):
        joint_val = self.arm.get_current_joint_values()
        flag = True
        for i in range(0,6):
            if abs(HOME[i] - joint_val[i] > 0.05):
                flag = False
                break

        if array and flag:
            for marker in array.markers:
                if marker.ns == "hand_base":
                    pose = marker.pose
                    matrix = self.matrix_from_quaternion(pose.orientation,pose.position)
                    listener = tf.TransformListener()
                    try:
                        (trans,rot) = listener.lookupTransform('/world', '/_kinect2_rgb_optical_frame', rospy.Time(0))
                        ori = oritation(rot[0],rot[1],rot[2],rot[3])
                        point = Point()
                        point.x = trans[0]
                        point.y = trans[1]
                        point.z = trans[2]
                        rotate1 = self.matrix_from_quaternion(ori,point)
                        rotate2 = self.eulerAnglesToRotationMatrix([0,pi/2,0])
                        matrix = np.dot(rotate1,np.dot(matrix,rotate2))
                        quat= list(pyquaternion.Quaternion(matrix=matrix))
                        pos1 = np.dot(matrix,[0,0,-0.22,1])
                        pos2 = np.dot(matrix,[0,0,-0.15,1])
                        self.setPose(pos1,quat,self.arm)
                        self.setPose(pos2,quat,self.arm)
                        self.gripper.set_joint_value_target(GRIPPER_CLOSED)
                        self.gripper.go()
                        break
                    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                        continue
        else:
            print "please wait or no object"

        self.arm.set_named_target('home')
        self.arm.go()

        self.gripper.set_joint_value_target(GRIPPER_OPEN)
        self.gripper.go()
        rospy.sleep(10)

    def setPose(self,point,posture,arm):
        pose = Pose()
        pose.position.x = point[0]
        pose.position.y = point[1]
        pose.position.z = point[2]
        pose.orientation.w=posture[0]
        pose.orientation.x=posture[1]
        pose.orientation.y=posture[2]
        pose.orientation.z=posture[3]
        arm.set_pose_target(pose)
        arm.go(wait = True)

    def matrix_from_quaternion(self,q,p):
        mat44 = xyzw_to_mat44(q)
        mat44[0][3]=p.x
        mat44[1][3]=p.y
        mat44[2][3]=p.z
        return mat44

    def eulerAnglesToRotationMatrix(self,theta) :
        R_x = np.array([[1,         0,             0              ,0],
                        [0,         cos(theta[0]), -sin(theta[0]) ,0],
                        [0,         sin(theta[0]), cos(theta[0])  ,0],
                        [0,0,0,1]
                        ])
        R_y = np.array([[cos(theta[1]),    0,      sin(theta[1])  ,0],
                        [0,                1,      0              ,0],
                        [-sin(theta[1]),   0,      cos(theta[1])  ,0],
                        [0,0,0,1]
                        ])
        R_z = np.array([[cos(theta[2]),    -sin(theta[2]),    0,0],
                        [sin(theta[2]),    cos(theta[2]),     0,0],
                        [0,                0,                 1,0],
                        [0,0,0,1]
                        ])
        R = np.dot(R_z, np.dot( R_y, R_x ))
        return R

class oritation:
    def __init__(self,x,y,z,w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w


if __name__ == "__main__":
    rospy.loginfo("start")
    Gpd_grasp()
    rospy.spin()