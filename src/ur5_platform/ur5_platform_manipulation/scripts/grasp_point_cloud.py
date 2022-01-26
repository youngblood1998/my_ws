#!/usr/bin/env python
import rospy
import moveit_commander
import numpy as np
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)

def vision_grasp(arm,grp,pos,ori,wid):
    # orien = arm.get_current_pose().pose
    # q = quaternion_from_euler(np.deg2rad(180.0) ,0.0,0.0)
    # pose.orientation = Quaternion(*q)
    # arm.set_pose_target(pose)
    # arm.go(wait = True)

    pose = Pose()
    pose.position.x = pos[0]
    pose.position.y = pos[1]
    pose.position.z = pos[2]+0.25
    pose.orientation.x=-1
    pose.orientation.y=0
    pose.orientation.z=0
    pose.orientation.w=0
    arm.set_pose_target(pose)
    arm.go(wait = True)

    # pose = arm.get_current_pose().pose
    # pose.orientation.x=-1
    # pose.orientation.y=0
    # pose.orientation.z=0
    # pose.orientation.w=0
    # arm.set_pose_target(pose)
    # arm.go(wait = True)

    orien=arm.get_current_joint_values()
    orien[5]=orien[5]+ori
    arm.set_joint_value_target(orien)
    arm.go(wait=True)

    grp.set_joint_value_target([0,0,0,0,0,0])
    grp.go(wait=True)

    pose = arm.get_current_pose().pose
    pose.position.z -=0.075
    arm.set_pose_target(pose)
    arm.go(wait = True)

    width=round(9*(0.09-wid)+0.036,3)
    grp.set_joint_value_target([0,0,width,0,0,0])
    grp.go(wait=True)

    pose.position.z =1
    arm.set_pose_target(pose)
    arm.go(wait = True)

    # orien=arm.get_current_joint_values()
    # orien[5]=orien[5]-ori
    # arm.set_joint_value_target(orien)
    # arm.go(wait=True)

    pose.position.x=0.6
    pose.position.y=-0.34
    # pose.position.z =0.64
    arm.set_pose_target(pose)
    arm.go(wait = True)

    pose.position.z =0.84
    arm.set_pose_target(pose)
    arm.go(wait = True)

    grp.set_joint_value_target([0,0,0,0,0,0])
    grp.go(wait=True)

    pose.position.z =1
    arm.set_pose_target(pose)
    arm.go(wait = True)


def main():
    rospy.init_node('vision_grasp')
    arm = moveit_commander.MoveGroupCommander("manipulator")
    grp = moveit_commander.MoveGroupCommander("gripper")
    arm.set_goal_position_tolerance(0.005)
    arm.set_goal_orientation_tolerance(0.01)
    arm.set_planning_time(5)
    grp.set_planning_time(5)

    number=0
    while rospy.search_param("/cube_position"+str(number+1)):
        number = number + 1

    arm.set_joint_value_target([-0.21957805043352518, -1.097296859939564, 1.8945345194815335,
                            -2.366067038969164, -1.571228181260084, -1.8])
    arm.go(wait=True)

    while number>0:
        position=rospy.get_param("/cube_position"+str(number))
        position_o=rospy.get_param("/cube_position_o"+str(number))
        position_w=rospy.get_param("/cube_position_w"+str(number))
        vision_grasp(arm,grp,position,position_o,position_w)
        number = number - 1

    arm.set_named_target("home")
    arm.go(wait = True)


if __name__ == '__main__':
    main()

