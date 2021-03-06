# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/kinetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/kinetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/jay/my_ws/devel_isolated/universal_robot;/home/jay/my_ws/devel_isolated/si_utils;/home/jay/my_ws/devel_isolated/robotiq_ft_sensor;/home/jay/my_ws/devel_isolated/robotiq_85_simulation;/home/jay/my_ws/devel_isolated/robotiq_85_msgs;/home/jay/my_ws/devel_isolated/robotiq_85_moveit_config;/home/jay/my_ws/devel_isolated/robotiq_85_gripper;/home/jay/my_ws/devel_isolated/robotiq_85_gazebo;/home/jay/my_ws/devel_isolated/robotiq_85_driver;/home/jay/my_ws/devel_isolated/robotiq_85_description;/home/jay/my_ws/devel_isolated/robotiq_85_bringup;/home/jay/my_ws/devel_isolated/roboticsgroup_gazebo_plugins;/home/jay/my_ws/devel_isolated/gazebo_grasp_plugin;/home/jay/my_ws/devel_isolated/find_object_2d;/home/jay/my_ws/devel_isolated/controller_stopper;/home/jay/gpd_ws/devel;/home/jay/ork_ws/devel;/home/jay/realsense_ws/devel;/home/jay/my_ws/devel;/home/jay/ur_ws/devel;/home/jay/ros_web_ws/devel;/opt/ros/kinetic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/jay/my_ws/devel_isolated/universal_robots/env.sh')

output_filename = '/home/jay/my_ws/build_isolated/universal_robots/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
