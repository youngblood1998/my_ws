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
import pandas as pd


rospy.init_node('set_joint')
arm = moveit_commander.MoveGroupCommander("manipulator")
# grp = moveit_commander.MoveGroupCommander("gripper")
arm.set_pose_reference_frame("base_link")
arm.set_goal_position_tolerance(0.05)
arm.set_goal_orientation_tolerance(0.05)
arm.allow_replanning(True)
arm.set_planning_time(50)

pose = arm.get_current_joint_values()
print(pose)
