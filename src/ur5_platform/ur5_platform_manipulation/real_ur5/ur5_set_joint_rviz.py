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
arm.set_max_velocity_scaling_factor(0.5)
arm.set_max_acceleration_scaling_factor(0.5)

arm.set_joint_value_target([2.177806854248047, -1.2385810057269495, 1.5798249244689941, -2.136148754750387, -2.3332021872149866, -0.8371146360980433])
arm.go(wait=True)
