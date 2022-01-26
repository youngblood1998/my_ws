#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib;roslib.load_manifest('robotiq_2f_gripper_control')
from robotiq_2f_gripper_control.msg import _Robotiq2FGripper_robot_output  as outputMsg
from robotiq_2f_gripper_control.msg import _Robotiq2FGripper_robot_input  as inputMsg
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
import message_filters
from time import sleep

LIMIT_HEIGHT = 0.21
INIT_JOINT = [2.5723202228546143, -1.704205338154928, -1.929758373891012, -1.058237377797262, -4.723835412655966, -6.103966091071264]
END_JOINT = [2.5368998050689697, -2.1411102453814905, -1.9300101439105433, -0.5002973715411585, -4.974742714558737, -5.774934295807974]
# qw: 0.9994347292050078
# qx: -0.010733231096187172
# qy: -0.0228922415663458
# qz: 0.022157731951095962
# x: -0.00176669771701
# y: -0.07014813811991
# z: 0.07326713482451

if rospy.search_param("/init_pos"):
    rospy.delete_param("/init_pos")

arm = moveit_commander.MoveGroupCommander("manipulator")
arm.set_goal_position_tolerance(0.01)
arm.set_goal_orientation_tolerance(0.01)
arm.allow_replanning(True)
arm.set_pose_reference_frame("base_link")
arm.set_max_velocity_scaling_factor(0.02)
arm.set_max_acceleration_scaling_factor(0.02)
arm.set_planning_time(3)

arm.set_joint_value_target(INIT_JOINT)
arm.go(wait = True)

sleep(2)

arm.set_joint_value_target(END_JOINT)
arm.go(wait = True)

rospy.set_param("/init_pos",60)
