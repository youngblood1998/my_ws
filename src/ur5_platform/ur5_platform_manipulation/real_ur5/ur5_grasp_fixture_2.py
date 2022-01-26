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
from time import sleep

INIT_POS = 150
INIT_JOINT = [2.5723202228546143, -1.704205338154928, -1.929758373891012, -1.058237377797262, -4.723835412655966, -6.103966091071264]
END_JOINT = [2.401400089263916, -2.1759164969073694, -1.7831547896014612, -0.721773926411764, -4.700668756161825, -5.845608297978536]
# qw: 0.9994347292050078
# qx: -0.010733231096187172
# qy: -0.0228922415663458
# qz: 0.022157731951095962
# x: -0.00176669771701
# y: -0.07014813811991
# z: 0.07326713482451

def genCommand(char, command):
    """Update the command according to the character entered by the user."""    
        
    if char == 'a':
        command = outputMsg.Robotiq2FGripper_robot_output();
        command.rACT = 1
        command.rGTO = 1
        command.rSP  = 50
        command.rFR  = 150

    if char == 'r':
        command = outputMsg.Robotiq2FGripper_robot_output();
        command.rACT = 0

    if char == 'c':
        command.rPR = 255

    if char == 'o':
        command.rPR = 0   

    #If the command entered is a int, assign this value to rPRA
    try: 
        command.rPR = int(char)
        if command.rPR > 255:
            command.rPR = 255
        if command.rPR < 0:
            command.rPR = 0
    except ValueError:
        pass                    
        
    if char == 'f':
        command.rSP += 25
        if command.rSP > 255:
            command.rSP = 255
            
    if char == 'l':
        command.rSP -= 25
        if command.rSP < 0:
            command.rSP = 0

            
    if char == 'i':
        command.rFR += 25
        if command.rFR > 255:
            command.rFR = 255
            
    if char == 'd':
        command.rFR -= 25
        if command.rFR < 0:
            command.rFR = 0

    return command

if __name__ == '__main__':
    rospy.init_node('robotiq_control')
    sleep(2)
    pub = rospy.Publisher('Robotiq2FGripperRobotOutput', outputMsg.Robotiq2FGripper_robot_output)

    command = outputMsg.Robotiq2FGripper_robot_output()

    command = genCommand('r', command)
    pub.publish(command)
    sleep(0.5)
    command = genCommand('a', command)
    pub.publish(command)

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

    sleep(1)

    arm.set_joint_value_target(END_JOINT)
    arm.go(wait = True)

    # raw_input("press enter to start")

    # command = genCommand(str(INIT_POS), command)
    # pub.publish(command)
    command = genCommand(str(INIT_POS), command)
    pub.publish(command)

    while not rospy.is_shutdown():
        rospy.spin()