# CMake generated Testfile for 
# Source directory: /home/jay/my_ws/src/robotiq/robotiq_85_gripper/si_utils
# Build directory: /home/jay/my_ws/build_isolated/si_utils
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_si_utils_roslaunch-check_launch "/home/jay/my_ws/build_isolated/si_utils/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/jay/my_ws/build_isolated/si_utils/test_results/si_utils/roslaunch-check_launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/jay/my_ws/build_isolated/si_utils/test_results/si_utils" "/opt/ros/kinetic/share/roslaunch/cmake/../scripts/roslaunch-check -o '/home/jay/my_ws/build_isolated/si_utils/test_results/si_utils/roslaunch-check_launch.xml' '/home/jay/my_ws/src/robotiq/robotiq_85_gripper/si_utils/launch' ")
subdirs(gtest)
