# CMake generated Testfile for 
# Source directory: /home/jay/my_ws/src/fmauch_universal_robot/ur3_moveit_config
# Build directory: /home/jay/my_ws/build_isolated/ur3_moveit_config
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_ur3_moveit_config_roslaunch-check_tests_moveit_planning_execution.xml "/home/jay/my_ws/build_isolated/ur3_moveit_config/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/jay/my_ws/build_isolated/ur3_moveit_config/test_results/ur3_moveit_config/roslaunch-check_tests_moveit_planning_execution.xml.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/jay/my_ws/build_isolated/ur3_moveit_config/test_results/ur3_moveit_config" "/opt/ros/kinetic/share/roslaunch/cmake/../scripts/roslaunch-check -o '/home/jay/my_ws/build_isolated/ur3_moveit_config/test_results/ur3_moveit_config/roslaunch-check_tests_moveit_planning_execution.xml.xml' '/home/jay/my_ws/src/fmauch_universal_robot/ur3_moveit_config/tests/moveit_planning_execution.xml' ")
subdirs(gtest)
