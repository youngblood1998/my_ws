#!/usr/bin/env python
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
arm.set_pose_reference_frame("base_link")
arm.set_goal_position_tolerance(0.05)
arm.set_goal_orientation_tolerance(0.05)
arm.allow_replanning(True)
arm.set_planning_time(50)
arm.set_max_velocity_scaling_factor(1)
arm.set_max_acceleration_scaling_factor(1)

arm.set_joint_value_target([2.5723202228546143, -1.704205338154928, -1.929758373891012, -1.058237377797262, -4.723835412655966, -6.103966091071264])
arm.go(wait=True)
