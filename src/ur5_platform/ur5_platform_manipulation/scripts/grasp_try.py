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

def eulerAnglesToRotationMatrix(theta) :
    R_x = np.array([[1,         0,                  0                   ,0],
                    [0,         math.cos(theta[0]), -math.sin(theta[0]) ,0],
                    [0,         math.sin(theta[0]), math.cos(theta[0])  ,0],
                    [0,0,0,1]
                    ])
    R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])  ,0],
                    [0,                     1,      0                   ,0],
                    [-math.sin(theta[1]),   0,      math.cos(theta[1])  ,0],
                    [0,0,0,1]
                    ])
    R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0,0],
                    [math.sin(theta[2]),    math.cos(theta[2]),     0,0],
                    [0,                     0,                      1,0],
                    [0,0,0,1]
                    ])
    R = np.dot(R_z, np.dot( R_y, R_x ))
    return R


rospy.init_node('grasp_try')
arm = moveit_commander.MoveGroupCommander("manipulator")
grp = moveit_commander.MoveGroupCommander("gripper")
arm.set_pose_reference_frame("_kinect2_rgb_optical_frame")
arm.set_goal_position_tolerance(0.05)
arm.set_goal_orientation_tolerance(0.05)
arm.allow_replanning(True)
arm.set_planning_time(50)
# arm.set_named_target('home')
# arm.go(wait=True)
# arm.set_joint_value_target([-0.00786205588344302, -2.269759846087066, 2.3410297253816665, -1.6402946512897998, -1.5850574745620722, 1.57])
# arm.go(wait=True)
pose = arm.get_current_joint_values()
print(pose)
# (r,p,y)=euler_from_quaternion(pose)
# print(p)

# pose = Pose()
# pose.position.x=-0.131111323281
# pose.position.y=-0.112955614297
# pose.position.z=0.77178491284
# pose.orientation.x=-0.112955614297
# pose.orientation.y=-0.620430761316
# pose.orientation.z=-0.620430761316
# pose.orientation.w=0.627515341343


# mat44=xyzw_to_mat44(pose.orientation)
# mat44[0][3]=pose.position.x
# mat44[1][3]=pose.position.y
# mat44[2][3]=pose.position.z
# rotate1=eulerAnglesToRotationMatrix([0,pi/2,0])
# matrix1=np.dot(mat44,rotate1)
# quat= list(pyquaternion.Quaternion(matrix=matrix1))

# pose.orientation.x=quat[1]
# pose.orientation.y=quat[2]
# pose.orientation.z=quat[3]
# pose.orientation.w=quat[0]

# arm.set_pose_target(pose)
# arm.go(wait = True)


# (x,y,z,w) = quaternion_from_euler(np.deg2rad(-180.0) ,0.0,0.0)
# print(x)
# pose.orientation = Quaternion(*q)
# pose.orientation=q
# arm.set_pose_target(pose)
# arm.go(wait = True)
# pose = arm.get_current_pose().pose
# pose.position.z -= 0.05
# arm.set_pose_target(pose)
# arm.go(wait=True)
# #grp.set_named_target('close')
# grp.set_joint_value_target([0,0,0.3,0,0,0])
# grp.go(wait=True)
# pose = arm.get_current_pose().pose
# pose.position.z += 0.05
# arm.set_pose_target(pose)
# arm.go(wait=True)

# orien=arm.get_current_joint_values()
# rospy.loginfo(orien)

# pose = arm.get_current_pose().pose
# pose.position.x = 0.6
# pose.position.y = 0.01
# pose.position.z = 0.8
# # pose.orientation.z = 0
# arm.set_pose_target(pose)
# arm.go(wait = True)

# grp.set_joint_value_target([0,0,0,0,0,0])
# grp.go(wait=True)

# pose.position.z -=0.075
# arm.set_pose_target(pose)
# arm.go(wait = True)

# grp.set_joint_value_target([0,0,0.40,0,0,0])
# grp.go(wait=True)

# pose.position.z +=0.075
# arm.set_pose_target(pose)
# arm.go(wait = True)

# # pose.position.x +=0.2
# # arm.set_pose_target(pose)
# # arm.go(wait = True)

# pose.position.x=0.6
# pose.position.y=-0.36
# pose.position.z +=0.045
# arm.set_pose_target(pose)
# arm.go(wait = True)

# grp.set_joint_value_target([0,0,0,0,0,0])
# grp.go(wait=True)