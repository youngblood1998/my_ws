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
INIT_JOINT = [2.5181760787963867, -1.3653538862811487, 1.6055965423583984, -1.7357919851886194, -2.3966479937182825, -0.06622296968568975]

# qw: 0.9994347292050078
# qx: -0.010733231096187172
# qy: -0.0228922415663458
# qz: 0.022157731951095962
# x: -0.00176669771701
# y: -0.07014813811991
# z: 0.07326713482451
    #   position: 
    #     x: -0.047643946539
    #     y: 0.052875690967
    #     z: 0.32305570258
    #   orientation: 
    #     x: 0.516274683287
    #     y: -0.481561299223
    #     z: 0.497205967525
    #     w: 0.504326672251

class Gpd_grasp:
    def __init__(self):
        rospy.init_node("vision_manager")
        self.arm = moveit_commander.MoveGroupCommander("manipulator")
        self.arm.set_goal_position_tolerance(0.01)
        self.arm.set_goal_orientation_tolerance(0.01)
        self.arm.allow_replanning(True)
        self.arm.set_pose_reference_frame("base_link")
        self.arm.set_planning_time(5)
        self.arm.set_max_velocity_scaling_factor(0.5)
        self.arm.set_max_acceleration_scaling_factor(0.5)
        self.callback()

    def callback(self):
        orientation1 = oritation(0.516274683287,-0.481561299223,0.497205967525,0.504326672251)
        position1 = Point()
        position1.x = -0.047643946539
        position1.y = 0.052875690967
        position1.z = 0.32305570258
        matrix = self.matrix_from_quaternion(orientation1,position1)

        listener = tf.TransformListener()
        rate = rospy.Rate(30)
        rate.sleep()
        # listener.waitForTransform('/base_link','/tool0',rospy.Time(), rospy.Duration(4.0))
        (trans,rot) = listener.lookupTransform('/base_link', '/tool0', rospy.Time(0))
        ori = oritation(rot[0],rot[1],rot[2],rot[3])
        point = Point()
        point.x = trans[0]
        point.y = trans[1]
        point.z = trans[2]
        rotate1 = self.matrix_from_quaternion(ori,point)

        ori2 = oritation(-0.0107,-0.0228,0.0221,0.999)
        point2 = Point()
        point2.x = -0.04176669771701
        point2.y = -0.07014813811991
        point2.z = 0.07326713482451
        rotate2 = self.matrix_from_quaternion(ori2,point2)

        rotate3 = self.eulerAnglesToRotationMatrix([0,pi/2,0])

        rotate4 = self.eulerAnglesToRotationMatrix([0,0,-pi/2])

        matrix = np.dot(rotate1,np.dot(rotate2,np.dot(np.dot(matrix,rotate3),rotate4)))

        quat= list(pyquaternion.Quaternion(matrix=matrix))
        pos1 = np.dot(matrix,[0,0,-0.16,1])
        pos2 = np.dot(matrix,[0,0,-0.11,1])
        self.setPose(pos1,quat,self.arm)
        self.setPose(pos2,quat,self.arm)
        # except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        #     print "no"


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