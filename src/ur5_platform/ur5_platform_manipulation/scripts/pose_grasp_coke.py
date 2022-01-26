#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random,math
from math import pi,cos,sin
import rospy, sys
import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose
from moveit_commander import MoveGroupCommander, PlanningSceneInterface
from moveit_msgs.msg import PlanningScene, ObjectColor
from moveit_msgs.msg import Grasp, GripperTranslation, MoveItErrorCodes
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from tf.transformations import quaternion_from_euler
from copy import deepcopy
import tf
from tf.listener import xyzw_to_mat44
import numpy as np 
import pyquaternion

GROUP_NAME_ARM = 'manipulator'
GROUP_NAME_GRIPPER = 'gripper'
GRIPPER_FRAME = 'gripper_base_link'
GRIPPER_OPEN = [0,0,0,0,0,0]
GRIPPER_CLOSED = [0,0,0.01,0,0,0]
REFERENCE_FRAME = 'world'

class MoveItPickAndPlaceDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)
        # 初始化ROS节点
        rospy.init_node('moveit_pick_and_place_demo')
        # 初始化场景对象
        scene = PlanningSceneInterface()
        # 创建一个发布场景变化信息的发布者
        self.scene_pub = rospy.Publisher('planning_scene', PlanningScene, queue_size=10)
        # 创建一个发布抓取姿态的发布者
        self.gripper_pose_pub = rospy.Publisher('gripper_pose', PoseStamped, queue_size=10)
        # 创建一个存储物体颜色的字典对象
        self.colors = dict()
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = MoveGroupCommander(GROUP_NAME_ARM)
        # 初始化需要使用move group控制的机械臂中的gripper group
        gripper = MoveGroupCommander(GROUP_NAME_GRIPPER)
        # 获取终端link的名称
        end_effector_link = arm.get_end_effector_link()
        # 设置位置(单位：米)和姿态（单位：弧度）的允许误差
        arm.set_goal_position_tolerance(0.01)
        arm.set_goal_orientation_tolerance(0.01)
        # 当运动规划失败后，允许重新规划
        arm.allow_replanning(True)
        # 设置目标位置所使用的参考坐标系
        arm.set_pose_reference_frame(REFERENCE_FRAME)
        # 设置每次运动规划的时间限制：5s
        arm.set_planning_time(50)
        # 设置pick和place阶段的最大尝试次数
        max_pick_attempts = 10
        max_place_attempts = 5
        rospy.sleep(2)
        # 控制机械臂先回到初始化位置
        arm.set_named_target('home')
        arm.go()
        # 控制夹爪张开
        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(1)

        box1_pose=self.addBox("box1",[0.05,0.05,0.123],scene)
        q=self.armPose(box1_pose.pose,[0,0.05,0.7])
        print(q)
        self.setPose(q[4:7],q[0:4],arm)
        self.setPose(q[7:10],q[0:4],arm)


        # mat44=xyzw_to_mat44(box1_pose.pose.orientation)
        # mat44[0][3]=box1_pose.pose.position.x
        # mat44[1][3]=box1_pose.pose.position.y
        # mat44[2][3]=box1_pose.pose.position.z
        # pointT=[[0],[0.3],[0],[1]]
        # destination=np.dot(mat44,pointT)

        # pose = Pose()
        # pose.position.x = destination[0][0]
        # pose.position.y = destination[1][0]
        # pose.position.z = destination[2][0]
        # pose.orientation.x=q[0]
        # pose.orientation.y=q[1]
        # pose.orientation.z=q[2]
        # pose.orientation.w=q[3]
        # arm.set_pose_target(pose)
        # arm.go(wait = True)

        # waypoints = []
        # start with the current pose
        # waypoints.append(arm.get_current_pose().pose)
        # first orient gripper and move forward (+x)
        # wpose = Pose()
        # wpose.orientation.x = q[0]
        # wpose.orientation.y = q[1]
        # wpose.orientation.z = q[2]
        # wpose.orientation.w = q[3]
        # wpose.position.x = destination[0][0]
        # wpose.position.y = destination[1][0]
        # wpose.position.z = destination[2][0]
        # waypoints.append(deepcopy(wpose))
        # second move down
        # wpose.position.z -= 0.10
        # waypoints.append(deepcopy(wpose))
        # # third move to the side
        # wpose.position.y += 0.05
        # waypoints.append(deepcopy(wpose))

        
        # rotate = self.eulerAnglesToRotationMatrix(angle)

        # mat44=xyzw_to_mat44(box1_pose.pose.orientation)
        # mat44[0][3]=box1_pose.pose.position.x
        # mat44[1][3]=box1_pose.pose.position.y
        # mat44[2][3]=box1_pose.pose.position.z
        # print(mat44)
        # # pointT=[[-0.3],[0],[0],[1]]
        # # destination=np.dot(mat44,pointT)
        # p1=self.eulerAnglesToRotationMatrix([0,pi,0])
        # print(p1)
        # point=np.dot(mat44[0:3,0:3],p1)
        # print(point)
        # quat= list(pyquaternion.Quaternion(matrix=point))
        # print(quat)
        # p=quaternion_from_euler(0,0,pi/2)
        # orien=ori(p[0],p[1],p[2],p[3])
        # rotate=xyzw_to_mat44(orien)
        # print(rotate)
        # posture=np.dot(mat44,rotate)
        # print(posture)
        # quat1= list(pyquaternion.Quaternion(matrix=posture[0:3,0:3]))
        # print(quat1)

        # # 追踪抓取成功与否，以及抓取的尝试次数
        # result = None
        # n_attempts = 0
        
        # # 重复尝试抓取，直道成功或者超多最大尝试次数
        # while result != MoveItErrorCodes.SUCCESS and n_attempts < max_pick_attempts:
        #     n_attempts += 1
        #     rospy.loginfo("Pick attempt: " +  str(n_attempts))
        #     result = arm.pick(target_id, grasps)
        #     rospy.sleep(0.2)
        
        # # 如果pick成功，则进入place阶段 
        # if result == MoveItErrorCodes.SUCCESS:
        #     result = None
        #     n_attempts = 0
            
        #     # 生成放置姿态
        #     places = self.make_places(place_pose)
            
        #     # 重复尝试放置，直道成功或者超多最大尝试次数
        #     while result != MoveItErrorCodes.SUCCESS and n_attempts < max_place_attempts:
        #         n_attempts += 1
        #         rospy.loginfo("Place attempt: " +  str(n_attempts))
        #         for place in places:
        #             result = arm.place(target_id, place)
        #             if result == MoveItErrorCodes.SUCCESS:
        #                 break
        #         rospy.sleep(0.2)
                
        #     if result != MoveItErrorCodes.SUCCESS:
        #         rospy.loginfo("Place operation failed after " + str(n_attempts) + " attempts.")
        # else:
        #     rospy.loginfo("Pick operation failed after " + str(n_attempts) + " attempts.")

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

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

    # 设置场景物体的颜色
    def setColor(self, name, r, g, b, a = 0.9):
        # 初始化moveit颜色对象
        color = ObjectColor()
        # 设置颜色值
        color.id = name
        color.color.r = r
        color.color.g = g
        color.color.b = b
        color.color.a = a
        # 更新颜色字典
        self.colors[name] = color

    # 将颜色设置发送并应用到moveit场景当中
    def sendColors(self):
        # 初始化规划场景对象
        p = PlanningScene()
        # 需要设置规划场景是否有差异     
        p.is_diff = True
        # 从颜色字典中取出颜色设置
        for color in self.colors.values():
            p.object_colors.append(color)
        # 发布场景物体颜色设置
        self.scene_pub.publish(p)

    def eulerAnglesToRotationMatrix(self,theta) :
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

    def addBox(self,name,size,scene):
        # 设置场景物体的名称 
        box1_id = name
        # 移除场景中之前运行残留的物体
        scene.remove_world_object(box1_id)
        # 移除场景中之前与机器臂绑定的物体
        # scene.remove_attached_object(GRIPPER_FRAME, target_id)  
        rospy.sleep(1)
        box1_size = size
        # 将三个物体加入场景当中
        box1_pose = PoseStamped()
        box1_pose.header.frame_id = REFERENCE_FRAME
        box1_pose.pose.position.x = 0.5+0.1*random.random()
        box1_pose.pose.position.y = -0.1+0.5*random.random()
        box1_pose.pose.position.z = 0.7
        angle=[2*pi*random.random(),2*pi*random.random(),2*pi*random.random()]
        q=quaternion_from_euler(angle[0],angle[1],angle[2])
        box1_pose.pose.orientation.w = q[0]
        box1_pose.pose.orientation.x = q[1]
        box1_pose.pose.orientation.y = q[2]
        box1_pose.pose.orientation.z = q[3]
        scene.add_box(box1_id, box1_pose, box1_size)
        # 将桌子设置成红色，两个box设置成橙色
        self.setColor(box1_id, 1, 0, 0, 1.0)
        return box1_pose

    def armPose(self,pose,point):
        mat44=xyzw_to_mat44(pose.orientation)
        mat44[0][3]=pose.position.x
        mat44[1][3]=pose.position.y
        mat44[2][3]=pose.position.z
        pointZ=[[0],[0],[1],[1]]
        dest1=np.dot(mat44,pointZ)
        if abs(dest1[2][0]-mat44[2][3])>=0.707:
            if (dest1[2][0]-mat44[2][3])>=0.707:
                rotate1=self.eulerAnglesToRotationMatrix([pi,0,0])
                matrix1=np.dot(mat44,rotate1)

                pointY=[[0],[1],[0],[1]]
                matrix2=deepcopy(matrix1)
                dest2=np.dot(matrix1,pointY)
                maximum=((dest2[0][0]-point[0])**2+(dest2[1][0]-point[1])**2)**0.5
                matrix3=deepcopy(matrix2)
                for i in range(1,4):
                    rotate2=self.eulerAnglesToRotationMatrix([0,0,pi/2])
                    matrix3=np.dot(matrix3,rotate2)
                    dest2=np.dot(matrix3,pointY)
                    if ((dest2[0][0]-point[0])**2+(dest2[1][0]-point[1])**2)**0.5>maximum:
                        maximum=((dest2[0][0]-point[0])**2+(dest2[1][0]-point[1])**2)**0.5
                        matrix2=deepcopy(matrix3)
                matrix=deepcopy(matrix2)
            else:
                pointY=[[0],[1],[0],[1]]
                matrix2=deepcopy(mat44)
                dest2=np.dot(matrix1,pointY)
                maximum=((dest2[0][0]-point[0])**2+(dest2[1][0]-point[1])**2)**0.5
                matrix3=deepcopy(matrix2)
                for i in range(1,4):
                    rotate2=self.eulerAnglesToRotationMatrix([0,0,pi/2])
                    matrix3=np.dot(matrix3,rotate2)
                    dest2=np.dot(matrix3,pointY)
                    if ((dest2[0][0]-point[0])**2+(dest2[1][0]-point[1])**2)**0.5>maximum:
                        maximum=((dest2[0][0]-point[0])**2+(dest2[1][0]-point[1])**2)**0.5
                        matrix2=deepcopy(matrix3)
                matrix=deepcopy(matrix2)
        else:
            pointZ1=[[0],[0],[-1],[1]]
            dest2=np.dot(mat44,pointZ1)
            if (dest2[0][0]-point[0])**2+(dest2[1][0]-point[1])>(dest1[0][0]-point[0])**2+(dest1[1][0]-point[1]):
                matrix1=deepcopy(mat44)
            else:
                rotate1=self.eulerAnglesToRotationMatrix([pi,0,0])
                matrix1=np.dot(mat44,rotate1)
            pointY=[[0],[1],[0],[1]]
            matrix2=deepcopy(matrix1)
            dest2=np.dot(matrix1,pointY)
            minimum=dest2[2][0]
            matrix3=deepcopy(matrix2)
            for i in range(1,4):
                rotate2=self.eulerAnglesToRotationMatrix([0,0,pi/2])
                matrix3=np.dot(matrix3,rotate2)
                dest2=np.dot(matrix3,pointY)
                if dest2[2][0]<minimum:
                    maximum=dest2[2][0]
                    matrix2=deepcopy(matrix3)
            matrix=deepcopy(matrix2)
        
        rotateY=self.eulerAnglesToRotationMatrix([0,-pi/2,0])
        rotateX=self.eulerAnglesToRotationMatrix([-pi/2,0,0])
        matrix=np.dot(np.dot(matrix,rotateY),rotateX)

        quat= list(pyquaternion.Quaternion(matrix=matrix))
        point1=np.dot(matrix,[[0],[0],[-0.25],[1]])
        point2=np.dot(matrix,[[0],[0],[-0.19],[1]])
        return [quat[0],quat[1],quat[2],quat[3],point1[0][0],point1[1][0],point1[2][0],point2[0][0],point2[1][0],point2[2][0]]

class ori:
    def __init__(self,x,y,z,w):
        self.x=x
        self.y=y
        self.z=z
        self.w=w

if __name__ == "__main__":
    MoveItPickAndPlaceDemo()