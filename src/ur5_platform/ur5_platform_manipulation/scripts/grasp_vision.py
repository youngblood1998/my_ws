#!/usr/bin/env python
import rospy
import moveit_commander

rospy.init_node('vision_grasp')
arm = moveit_commander.MoveGroupCommander("manipulator")
grp = moveit_commander.MoveGroupCommander("gripper")

arm.set_joint_value_target([-0.21957805043352518, -1.097296859939564, 1.8945345194815335,
                            -2.366067038969164, -1.571228181260084, -1.8])
arm.go(wait=True)

number=0
while rospy.search_param("/cube_position_x"+str(number+1)):
    number=number+1
while number>0:
    position_x=rospy.get_param("/cube_position_x"+str(number))
    position_y=rospy.get_param("/cube_position_y"+str(number))

    pose = arm.get_current_pose().pose
    pose.position.x = position_x
    pose.position.y = position_y
    pose.position.z = 0.8
    arm.set_pose_target(pose)
    arm.go(wait = True)

    # if rospy.search_param("/cube_position_o"+str(number)):
    #     position_o=rospy.get_param("/cube_position_o"+str(number))
    #     orien=arm.get_current_joint_values()
    #     orien[5]=position_o
    #     arm.set_joint_value_target(orien)
    #     arm.go(wait=True)

    number=number-1

    grp.set_joint_value_target([0,0,0,0,0,0])
    grp.go(wait=True)

    pose = arm.get_current_pose().pose
    pose.position.z -=0.065
    arm.set_pose_target(pose)
    arm.go(wait = True)

    grp.set_joint_value_target([0,0,0.54,0,0,0])
    grp.go(wait=True)

    pose.position.z +=0.065
    arm.set_pose_target(pose)
    arm.go(wait = True)

    pose.position.x=0.6
    pose.position.y=-0.35
    pose.position.z +=0.045
    arm.set_pose_target(pose)
    arm.go(wait = True)

    grp.set_joint_value_target([0,0,0,0,0,0])
    grp.go(wait=True)

arm.set_named_target("home")
arm.go(wait = True)