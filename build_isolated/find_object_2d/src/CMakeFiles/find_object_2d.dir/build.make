# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jay/my_ws/src/find_object_2d

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jay/my_ws/build_isolated/find_object_2d

# Include any dependencies generated for this target.
include src/CMakeFiles/find_object_2d.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/find_object_2d.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/find_object_2d.dir/flags.make

src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o: src/CMakeFiles/find_object_2d.dir/flags.make
src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o: /home/jay/my_ws/src/find_object_2d/src/ros/find_object_2d_node.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jay/my_ws/build_isolated/find_object_2d/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o"
	cd /home/jay/my_ws/build_isolated/find_object_2d/src && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o -c /home/jay/my_ws/src/find_object_2d/src/ros/find_object_2d_node.cpp

src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.i"
	cd /home/jay/my_ws/build_isolated/find_object_2d/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jay/my_ws/src/find_object_2d/src/ros/find_object_2d_node.cpp > CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.i

src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.s"
	cd /home/jay/my_ws/build_isolated/find_object_2d/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jay/my_ws/src/find_object_2d/src/ros/find_object_2d_node.cpp -o CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.s

src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o.requires:

.PHONY : src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o.requires

src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o.provides: src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o.requires
	$(MAKE) -f src/CMakeFiles/find_object_2d.dir/build.make src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o.provides.build
.PHONY : src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o.provides

src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o.provides.build: src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o


# Object files for target find_object_2d
find_object_2d_OBJECTS = \
"CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o"

# External object files for target find_object_2d
find_object_2d_EXTERNAL_OBJECTS =

/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: src/CMakeFiles/find_object_2d.dir/build.make
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /home/jay/my_ws/devel_isolated/find_object_2d/lib/libfind_object_2d.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_stitching3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_superres3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_videostab3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_aruco3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_bgsegm3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_bioinspired3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_ccalib3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_cvv3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_dpm3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_face3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_fuzzy3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_hdf3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_img_hash3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_line_descriptor3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_optflow3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_reg3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_rgbd3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_saliency3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_stereo3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_structured_light3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_surface_matching3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_tracking3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_xfeatures2d3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_ximgproc3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_xobjdetect3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_xphoto3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libz.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libcv_bridge.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_core3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_imgproc3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_imgcodecs3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libimage_transport.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libtinyxml2.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libclass_loader.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/libPocoFoundation.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libdl.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libroslib.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/librospack.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libpython2.7.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libboost_program_options.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libtinyxml.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libtf.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libtf2_ros.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libactionlib.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libmessage_filters.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libroscpp.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libtf2.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/librosconsole.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/librostime.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/libcpp_common.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libQt5Network.so.5.5.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libQt5PrintSupport.so.5.5.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_photo3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_viz3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_phase_unwrapping3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_datasets3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_plot3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_text3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_dnn3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_ml3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_shape3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_video3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_calib3d3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_features2d3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_flann3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_highgui3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_videoio3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_imgcodecs3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_objdetect3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_imgproc3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_core3.so.3.3.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libQt5Widgets.so.5.5.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libQt5Gui.so.5.5.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: /usr/lib/x86_64-linux-gnu/libQt5Core.so.5.5.1
/home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d: src/CMakeFiles/find_object_2d.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jay/my_ws/build_isolated/find_object_2d/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d"
	cd /home/jay/my_ws/build_isolated/find_object_2d/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/find_object_2d.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/find_object_2d.dir/build: /home/jay/my_ws/devel_isolated/find_object_2d/lib/find_object_2d/find_object_2d

.PHONY : src/CMakeFiles/find_object_2d.dir/build

src/CMakeFiles/find_object_2d.dir/requires: src/CMakeFiles/find_object_2d.dir/ros/find_object_2d_node.cpp.o.requires

.PHONY : src/CMakeFiles/find_object_2d.dir/requires

src/CMakeFiles/find_object_2d.dir/clean:
	cd /home/jay/my_ws/build_isolated/find_object_2d/src && $(CMAKE_COMMAND) -P CMakeFiles/find_object_2d.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/find_object_2d.dir/clean

src/CMakeFiles/find_object_2d.dir/depend:
	cd /home/jay/my_ws/build_isolated/find_object_2d && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jay/my_ws/src/find_object_2d /home/jay/my_ws/src/find_object_2d/src /home/jay/my_ws/build_isolated/find_object_2d /home/jay/my_ws/build_isolated/find_object_2d/src /home/jay/my_ws/build_isolated/find_object_2d/src/CMakeFiles/find_object_2d.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/find_object_2d.dir/depend

