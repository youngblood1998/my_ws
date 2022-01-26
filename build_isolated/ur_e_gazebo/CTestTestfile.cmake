# CMake generated Testfile for 
# Source directory: /home/jay/my_ws/src/fmauch_universal_robot/ur_e_gazebo
# Build directory: /home/jay/my_ws/build_isolated/ur_e_gazebo
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_ur_e_gazebo_roslaunch-check_tests_roslaunch_test.xml "/home/jay/my_ws/build_isolated/ur_e_gazebo/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/jay/my_ws/build_isolated/ur_e_gazebo/test_results/ur_e_gazebo/roslaunch-check_tests_roslaunch_test.xml.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/jay/my_ws/build_isolated/ur_e_gazebo/test_results/ur_e_gazebo" "/opt/ros/kinetic/share/roslaunch/cmake/../scripts/roslaunch-check -o '/home/jay/my_ws/build_isolated/ur_e_gazebo/test_results/ur_e_gazebo/roslaunch-check_tests_roslaunch_test.xml.xml' '/home/jay/my_ws/src/fmauch_universal_robot/ur_e_gazebo/tests/roslaunch_test.xml' ")
subdirs(gtest)
