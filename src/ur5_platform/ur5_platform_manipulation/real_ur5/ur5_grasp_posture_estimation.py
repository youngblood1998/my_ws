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

LIMIT_HEIGHT = 0.21
INIT_JOINT = [2.5723202228546143, -1.704205338154928, -1.929758373891012, -1.058237377797262, -4.723835412655966, -6.103966091071264]
# qw: 0.9994347292050078
# qx: -0.010733231096187172
# qy: -0.0228922415663458
# qz: 0.022157731951095962
# x: -0.00176669771701
# y: -0.07014813811991
# z: 0.07326713482451

class Gpd_grasp:
    def __init__(self):
        rospy.init_node("vision_manager")
        self.arm = moveit_commander.MoveGroupCommander("manipulator")
        self.arm.set_goal_position_tolerance(0.01)
        self.arm.set_goal_orientation_tolerance(0.01)
        self.arm.allow_replanning(True)
        self.arm.set_pose_reference_frame("base_link")
        self.arm.set_max_velocity_scaling_factor(0.02)
        self.arm.set_max_acceleration_scaling_factor(0.02)
        self.arm.set_planning_time(3)
        self.pos = 0
        self.flag = True

        self.arm.set_joint_value_target(INIT_JOINT)
        self.arm.go(wait = True)

        if rospy.search_param("/init_pos"):
            rospy.delete_param("/init_pos")
        # rospy.set_param("/robotiq_command",'o')
        # rospy.sleep(1)

        self.pub = rospy.Publisher('Robotiq2FGripperRobotOutput', outputMsg.Robotiq2FGripper_robot_output)
        self.sub = rospy.Subscriber("Robotiq2FGripperRobotInput", inputMsg.Robotiq2FGripper_robot_input,self.setStatus)
        self.posture_sub = message_filters.Subscriber('/detect_grasps/grasps_rviz',MarkerArray,queue_size=1,buff_size=52428800)
        self.width_sub = message_filters.Subscriber('/detect_grasps/clustered_grasps', GraspConfigList, queue_size=1,buff_size=52428800)
        sync = message_filters.ApproximateTimeSynchronizer([self.posture_sub, self.width_sub],1,1,allow_headerless=True)
        sync.registerCallback(self.callback)

    def setStatus(self,data):
        self.pos = int(data.gPO)

    def callback(self,array,grasps):
        print 1
        if self.flag:

            flag2 = False
            min_height = 0.5
            for marker in array.markers:
                if marker.ns == "hand_base":

                    a = self.matrix_from_quaternion(marker.pose.orientation,marker.pose.position)
                    b = [1,0,0,1]
                    c = np.dot(a,b)

                    if marker.pose.position.z < min_height and c[2] - marker.pose.position.z > 0.95:
                        min_height = marker.pose.position.z
                        pose = marker.pose
                        angle = acos(c[2] - marker.pose.position.z)
                        flag2 = True
                        self.flag = False

            max_width = 0
            for grasp in grasps.grasps:
                if grasp.width.data > max_width:
                    max_width = grasp.width.data
            if max_width < 0.005:
                max_width = 0.02

            if flag2 and pose.position.z > LIMIT_HEIGHT:
                length = pose.position.z - LIMIT_HEIGHT
                a = self.matrix_from_quaternion(pose.orientation,pose.position)
                b = [-length/cos(angle),0,0,1]
                c = np.dot(a,b)
                pose.position.x = c[0]
                pose.position.y = c[1]
                pose.position.z = c[2]

            if flag2:
                matrix = self.matrix_from_quaternion(pose.orientation,pose.position)
                listener = tf.TransformListener()
                rate = rospy.Rate(30)
                while not rospy.is_shutdown():
                    try:
                        (trans,rot) = listener.lookupTransform('/base_link', '/wrist_3_link', rospy.Time(0))
                        ori = oritation(rot[0],rot[1],rot[2],rot[3])
                        point = Point()
                        point.x = trans[0]
                        point.y = trans[1]
                        point.z = trans[2]
                        rotate1 = self.matrix_from_quaternion(ori,point)

                        ori2 = oritation(-0.0107,-0.0228,0.0221,0.999)
                        point2 = Point()
                        point2.x = 0.03576669771701
                        point2.y = -0.06914813811991
                        point2.z = 0.07326713482451
                        rotate2 = self.matrix_from_quaternion(ori2,point2)

                        matrix = np.dot(rotate1,np.dot(rotate2,matrix))


                        pos_to_robotiq = [0,0,0.2,1]
                        pos_to_base = np.dot(matrix,pos_to_robotiq)
                        if (pos_to_base[0]**2+pos_to_base[1]**2)**(0.5) < (matrix[0][3]**2+matrix[1][3]**2)**(0.5):
                            rotate3 = self.eulerAnglesToRotationMatrix([pi,0,0])
                            matrix = np.dot(matrix,rotate3)


                        quat= list(pyquaternion.Quaternion(matrix=matrix))


                        pos1 = np.dot(matrix,[-0.16,0,0,1])
                        pos2 = np.dot(matrix,[-0.11,0,0,1])

                        print "find pose"

                        self.setPose(pos1,quat,self.arm)
                        self.setPose(pos2,quat,self.arm)

                        rospy.sleep(2)

                        set_pos = floor(-2.8934*(max_width+0.01)*1000+218.75)
                        rospy.set_param("/init_pos",str(int(floor(-2.8934*(max_width+0.005)*1000+218.75))))
                        # rospy.set_param("/robotiq_command",str(floor(-2.8934*(max_width+0.015)*1000+218.75)))
                        # rospy.sleep(5)

                        break
                    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                        continue
                    rate.sleep()
            else:
                print "no pose"

    def genCommand(self, char, command):
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
    rospy.spin()