#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import moveit_commander
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)
import numpy as np
import math
from math import pi
from tf.listener import xyzw_to_mat44
import pyquaternion


rospy.init_node('grasp_try')
arm = moveit_commander.MoveGroupCommander("manipulator")
# grp = moveit_commander.MoveGroupCommander("gripper")
arm.set_pose_reference_frame("base_link")
arm.set_goal_position_tolerance(0.005)
arm.set_goal_orientation_tolerance(0.005)
arm.set_max_velocity_scaling_factor(0.05)
arm.set_max_acceleration_scaling_factor(0.05)
arm.allow_replanning(True)
arm.set_planning_time(50)
# arm.set_named_target('home')
# arm.go(wait=True)
# arm.set_joint_value_target([-0.00786205588344302, -2.269759846087066, 2.3410297253816665, -1.6402946512897998, -1.5850574745620722, 1.57])
# arm.go(wait=True)
pose = arm.get_current_pose()
pose.pose.position.x -= 0.1
pose.pose.position.y += 0.1
arm.set_pose_target(pose)
arm.go(wait=True)
while not rospy.is_shutdown():
    pose = arm.get_current_pose()
    pose.pose.position.x += 0.2
    pose.pose.position.y -= 0.2
    arm.set_pose_target(pose)
    arm.go(wait=True)

    pose = arm.get_current_pose()
    pose.pose.position.x -= 0.2
    pose.pose.position.y += 0.2
    arm.set_pose_target(pose)
    arm.go(wait=True)