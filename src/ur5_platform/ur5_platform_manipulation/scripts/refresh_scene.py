#!/usr/bin/env python
# encoding: utf-8

from gazebo_msgs.srv import DeleteModel
import rospy
import os
from random import *

def delete_model(row,col,model_name):
    rospy.wait_for_service('/gazebo/delete_model')
    try:
        remove_model_proxy = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
        for i in range(0,row*col):
            remove_model_proxy(model_name+"_"+str(i))
    except rospy.ServiceException, ex:
        print "Service call delete_model failed: %e" % ex

def add_model(row,col,model_name,x,width,y,height):
    # GAZEBO_MODEL_PATH = "~/.gazebo/models/"
    GAZEBO_MODEL_PATH = "~/my_ws/src/ur5_platform/ur5_platform_gazebo/meshes/"
    for i in range(0,row):
        for j in range(0,col):
            pos_x=x+float(i)/row*width+random()*width/row
            pos_y=y+float(j)/col*height+random()*height/col
            os.system("rosrun gazebo_ros spawn_model -file " + GAZEBO_MODEL_PATH + model_name +"/model.sdf -sdf -model " + model_name + "_" + str(i*col+j) +" -x "+str(pos_x)+" -y "+str(pos_y)+" -z 0.63 -Y "+str(3.14*random()))

def main():
    rospy.init_node('model_change', anonymous=True)
    delete_model(2,3,"wood_cube_5cm")
    add_model(2,3,"wood_cube_5cm",0.36,0.46,-0.2,0.62)

if __name__ == '__main__':
    main()