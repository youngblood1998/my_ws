# CMake generated Testfile for 
# Source directory: /home/jay/my_ws/src/robotiq/robotiq_85_gripper/robotiq_85_bringup
# Build directory: /home/jay/my_ws/build_isolated/robotiq_85_bringup
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_robotiq_85_bringup_roslaunch-check_launch "/home/jay/my_ws/build_isolated/robotiq_85_bringup/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/jay/my_ws/build_isolated/robotiq_85_bringup/test_results/robotiq_85_bringup/roslaunch-check_launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/jay/my_ws/build_isolated/robotiq_85_bringup/test_results/robotiq_85_bringup" "/opt/ros/kinetic/share/roslaunch/cmake/../scripts/roslaunch-check -o '/home/jay/my_ws/build_isolated/robotiq_85_bringup/test_results/robotiq_85_bringup/roslaunch-check_launch.xml' '/home/jay/my_ws/src/robotiq/robotiq_85_gripper/robotiq_85_bringup/launch' ")
subdirs(gtest)
