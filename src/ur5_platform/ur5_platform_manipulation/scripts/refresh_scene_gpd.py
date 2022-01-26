#!/usr/bin/env python
# encoding: utf-8

from gazebo_msgs.srv import DeleteModel
import rospy
import os
from random import *

def main():
    os.system("rosrun gazebo_ros spawn_model -file ~/.gazebo/models/coke_can/model.sdf -sdf -model coke_can -x 0.62 -y 0.0 -z 0.7 -R 1.57 -P 1.2 -Y 2.2")

if __name__ == '__main__':
    main()