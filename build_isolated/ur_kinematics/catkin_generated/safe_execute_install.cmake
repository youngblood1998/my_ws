execute_process(COMMAND "/home/jay/my_ws/build_isolated/ur_kinematics/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jay/my_ws/build_isolated/ur_kinematics/catkin_generated/python_distutils_install.sh) returned error code ")
endif()